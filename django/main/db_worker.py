import datetime
import sqlite3
from .models import Match # type: ignore

def update(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    Match.objects.all().delete()

    cursor.execute("SELECT year, month, day, prediction, section FROM calendar")
    rows = cursor.fetchall()

    matches = []
    for row in rows:
        match = Match(
            date = datetime.date(row[0], row[1], row[2]),
            prediction=row[3],
            section=row[4],
        )
        matches.append(match)
    
    Match.objects.bulk_create(matches)

    conn.close()
    print("Данные успешно обновлены из SQLite!")
