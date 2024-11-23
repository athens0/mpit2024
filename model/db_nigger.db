from os import listdir, path
import csv
import sqlite3
import datetime

DEFAULT_AVERAGE = 1.0

folders = [i for i in listdir() if path.exists(i + '/')]

edu_days = dict()

for institute in folders:
    files = listdir(institute)
    for group in files:
        csvfile = open(institute + '/' + group, 'r')
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            if not row:
                continue
            if (row[0], row[1]) not in edu_days:
                edu_days[(row[0], row[1])] = (0, 0)
            edu_days[(row[0], row[1])] = (edu_days[(row[0], row[1])][0] + int(row[2]), edu_days[(row[0], row[1])][1] + 1)
        csvfile.close()

sorted_edu = []
for i in edu_days:
    sorted_edu.append((int(i[1]), int(i[0]), edu_days[i][0] / edu_days[i][1]))
sorted_edu.sort()

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS edu (
id INTEGER PRIMARY KEY,
month INTEGER NOT NULL,
day INTEGER NOT NULL,
average REAL NOT NULL
)
''')

cur = datetime.date(2024, 9, 1)
for i in sorted_edu:
    while cur.month != i[0] or cur.day != i[1]:
        cursor.execute('INSERT INTO edu (month, day, average) VALUES (?, ?, ?)', (cur.month, cur.day, DEFAULT_AVERAGE))
        cur += datetime.timedelta(days=1)
    cursor.execute('INSERT INTO edu (month, day, average) VALUES (?, ?, ?)', (cur.month, cur.day, i[2]))
    cur += datetime.timedelta(days=1)
print(sorted_edu)

connection.commit()
connection.close()