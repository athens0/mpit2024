import calendar
from os import listdir, path
import csv
import sqlite3
import datetime as dt


connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def get_week_day(year, month, day):
    return dt.date(year, month, day).weekday() + 1


for year in range(2023, 2025):
    for month in range(1, 13):
        days_in_month = calendar.monthrange(year, month)[1]
        for day in range(1, days_in_month + 1):
            print(f"Month: {month}, Day: {day}")
            is_exam = 1 if ((month == 12 and day >= 17) or (month == 5 and day >= 24) or (month == 6 and day <= 26)) else 0
            is_holiday = 1 if ((month == 1 and day <= 8) or (month == 11 and day == 4) or (month == 2 and day == 23) or (month == 3 and day == 8) or (month == 5 and (day == 1 or day == 9))) else 0  # Пример: Новый год


            date = dt.date(year, month, day)  # 1st Jan 2024, 10:30
            date2 = dt.date(year, 12, 17)
            date3 = dt.date(year, 5, 25)

            date4 = dt.date(year, 1, 27)
            date5 = dt.date(year, 6, 30)
            date6 = dt.date(year + 1, 1, 27)


            if (date > date2):
                days_exam = 0
                days_holiday = (date6 - date).days
            elif (date > date3):
                if (date > date5):
                    days_exam = max(0, (date2 - date).days)
                    if (date > dt.date(year, 9, 1)):
                        days_holiday = (date6 - date).days
                    else:
                        days_holiday = 0
                else:
                    days_exam = max(0, (date2 - date).days)
                    if (date > dt.date(year, 9, 1)):
                        days_holiday = (date6 - date).days
                    else:
                        days_holiday = max(0, (date5 - date).days)
            else:
                days_exam = max(0, (date3 - date).days)
                days_holiday = max(0, (date5 - date).days)

            week_day = get_week_day(year, month, day)

            if (is_exam == 1): days_exam = 0
            if (is_holiday == 1): days_holiday = 0

            cursor.execute("""
                SELECT COUNT(*) FROM edu WHERE year = ? AND month = ? AND day = ?
            """, (year, month, day))
            exists = cursor.fetchone()[0] > 0

            if exists:
                cursor.execute("""
                    UPDATE edu
                    SET is_exam = ?, is_holiday = ?, days_exam = ?, days_holiday = ?, week_day = ?
                    WHERE year = ? AND month = ? AND day = ?
                """, (is_exam, is_holiday, days_exam, days_holiday, week_day, year, month, day))
            else:
                cursor.execute("""
    INSERT INTO edu (average, year, month, day, is_exam, is_holiday, days_exam, days_holiday, week_day)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (2, year, month, day, is_exam, is_holiday, days_exam, days_holiday, week_day))


connection.commit()
connection.close()