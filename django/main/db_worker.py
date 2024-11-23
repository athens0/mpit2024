import datetime
import sqlite3
from .models import Match, Prediction

def update(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    Match.objects.all().delete()

    cursor.execute("SELECT year, month, day, prediction, section FROM calendar")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
        match = Prediction.objects.create(
            date = datetime.date(row[0], row[1], row[2]),
            result=row[3],
            section=row[4],
        )
        match.save()

    conn.close()
    print("Данные успешно обновлены из SQLite!")
