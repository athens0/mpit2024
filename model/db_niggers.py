import sqlite3

# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Match data in a list of tuples (day, month, year, name, win, lose)
match_data = [
    (29, 10, 2023, "БГТУ_Военмех", 70, 82),
    (5, 11, 2023, "РАНХиГС_Невских_Титанов", 81, 63),
    (12, 11, 2023, "ИТМО", 90, 74),
    (19, 11, 2023, "РГПУ_им._Герцена", 99, 92),
    (10, 12, 2023, "СПБГУПТД-2", 69, 84),
    (24, 12, 2023, "НГУ", 20, 0),
    (21, 1, 2024, "СПБГУПТД-2", 68, 102),
    (28, 1, 2024, "МЧС_Невские_львы", 61, 88),
    (4, 2, 2024, "ЛГУ_Зенит", 73, 84),
    (4, 2, 2024, "СПБГАСУ", 117, 45),
    (11, 2, 2024, "СПБГЭтУ_ЛЭТИ", 74, 43),
    (17, 3, 2024, "РГПУ_им._Герцена", 69, 70),
    (22, 3, 2024, "НГУ", 65, 49),
    (29, 3, 2024, "МЧС_Невские_львы", 59, 64),
    (3, 4, 2024, "ЛГУ_Зенит", 64, 95),
    (22, 10, 2024, "ГУТИД", 68, 87),
    (5, 11, 2024, "РАНХиГС_Невских_Титанов", 59, 52),
    (12, 11, 2024, "Волки_ЛТУ", 75, 63),
    (19, 11, 2024, "ЛГУ_Зенит", 60, 77),
]

# Insert match data into the matches table
for match in match_data:
    day, month, year, name, win, lose = match
    section = "Basketball"  # Assuming a fixed section for now, change if needed
    cursor.execute("""
        INSERT INTO matches (day, month, year, name, win, lose, section)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (day, month, year, name, win, lose, section))

# Commit the transaction and close the connection
connection.commit()
connection.close()