from lxml import etree
from urllib.request import urlopen
import csv
import datetime
from os import mkdir, path

YEAR = 2024
MONTHS = {
    'янв': 1,
    'февр': 2,
    'мар': 3,
    'апр': 4,
    'мая': 5,
    'июн': 6,
    'июл': 7,
    'авг': 8,
    'сент': 9,
    'окт': 10,
    'нояб': 11,
    'дек': 12
}

main_url = "https://ruz.spbstu.ru/"
req = urlopen(main_url)
parser = etree.HTMLParser()
tree = etree.parse(req, parser)
institutes = tree.xpath("//a[@class='faculty-list__link']/@href")

for institute in institutes:
    institute_url = main_url + institute
    req = urlopen(institute_url)
    parser = etree.HTMLParser()
    tree = etree.parse(req, parser)
    urls = tree.xpath("//a[@class='groups-list__link']/@href")
    groups = tree.xpath("//a[@class='groups-list__link']/text()")
    name = tree.xpath("//li[@class='breadcrumb-item active']/text()")[0]

    if path.exists(f'{name}/'):
        continue

    for i in range(len(urls)):
        month = 9
        day = 1

        url = urls[i]
        
        if not path.exists(f'{name}/'):
            mkdir(f'{name}/')
        csvfile = open(f'{name}/{name}-{groups[i].replace('/', '-')}-{YEAR}.csv', 'w')
        writer = csv.writer(csvfile, delimiter=';', quotechar='|')

        date = datetime.date(YEAR, month, day)

        group_url = 'https://ruz.spbstu.ru' + url

        while date.year == YEAR:
            url = group_url + f'?date={date.year}-{date.month}-{date.day}'
            req = urlopen(url)
            parser = etree.HTMLParser()
            tree = etree.parse(req, parser)

            print(url)

            for day in range(1, 8):
                cur_date = tree.xpath(f"//li[@class='schedule__day'][{day}]/div/text()")
                if not cur_date:
                    break
                cur_date = cur_date[0].split(' ')
                cur_day = int(cur_date[0])
                cur_month = MONTHS[cur_date[1].replace('.', '').replace(',', '')]
                classes = tree.xpath(f"//ul[@class='schedule']/li[@class='schedule__day'][{day}]//li")
                writer.writerow([cur_day, cur_month, len(classes)])
            
            date += datetime.timedelta(days=7)

        csvfile.close()
