import sqlite3
import csv

database_path = "database.db"

csv_file_path = "matches.csv"

def insert_matches_from_csv(database_path, csv_file_path):
    """
    Reads match data from a CSV file and inserts it into the 'matches' table.

    Parameters:
        database_path (str): Path to the SQLite database file.
        csv_file_path (str): Path to the input CSV file.
    """
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        with open(csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = []

            for line in reader:
                year = int(line['year'])
                month = int(line['month'])
                day = int(line['day'])
                name = line['name'].strip().replace(" ", "_")
                win = int(line['win'])
                lose = int(line['lose'])
                section = line['section'].strip().lower()
                
                rows.append((month, day, year, name, win, lose, section))

        cursor.executemany("""
            INSERT INTO matches (month, day, year, name, win, lose, section)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, rows)

        connection.commit()
        print(f"Inserted {len(rows)} matches into the database.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

insert_matches_from_csv(database_path, csv_file_path)
