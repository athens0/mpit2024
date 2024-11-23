import sqlite3
import csv

def export_training_basketball(database_path, csv_file_path):
    """
    Export a training dataset for basketball, combining matches and edu data.

    Parameters:
        database_path (str): Path to the SQLite database file.
        csv_file_path (str): Path to the output CSV file.
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # Query to join matches and edu tables
        query = """
            SELECT 
                m.day,
                m.month,
                m.year,
                e.average,
                e.is_exam,
                e.is_holiday,
                e.days_exam,
                e.days_holiday,
                e.week_day,
                m.name AS opponent,
                m.win,
                m.lose
            FROM matches AS m
            LEFT JOIN edu AS e
            ON m.year = e.year AND m.month = e.month AND m.day = e.day
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        opponent_mapping = {}
        opponent_index = 1

        for row in rows:
            opponent = row[9] #opponent
            if opponent not in opponent_mapping:
                opponent_mapping[opponent] = opponent_index
                opponent_index += 1

        csv_columns = [
            "day", "month", "year", "average", "is_exam", "is_holiday",
            "days_exam", "days_holiday", "week_day", "opponent", "result"
        ]

        csv_data = []
        for row in rows:
            month, day, average, year, is_exam, is_holiday, days_exam, days_holiday, week_day, opponent, win, lose = row
            result = win / (win + lose) if (win + lose) > 0 else 0.5
            opponent_index = opponent_mapping[opponent]
            csv_data.append([
                month, day, average, year, is_exam, is_holiday,
                days_exam, days_holiday, week_day, opponent_index, round(result, 3)
            ])

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_columns)
            writer.writerows(csv_data)

        print(f"Training dataset has been exported to {csv_file_path} successfully.")
        print("Opponent Mapping:", opponent_mapping)

    except sqlite3.Error as e:
        print(f"Error while accessing SQLite database: {e}")
    finally:
        if connection:
            connection.close()

database_path = 'database.db'
csv_file_path = 'training_basketball.csv'

export_training_basketball(database_path, csv_file_path)
