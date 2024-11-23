import sqlite3
import csv

# Connect to the SQLite database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Query to fetch match data and join it with edu table dependencies
query = """
    SELECT 
        m.year, m.month, m.day, m.name, m.win, m.lose, m.section,
        e.average, e.is_exam, e.is_holiday, e.days_exam, e.days_holiday, e.week_day
    FROM matches AS m
    LEFT JOIN edu AS e
    ON m.year = e.year AND m.month = e.month AND m.day = e.day
"""

# Execute the query and fetch the data
cursor.execute(query)
rows = cursor.fetchall()

# Define the CSV columns
csv_columns = [
    "day",
             "month",
                      "year",         # Combined date (year, month, day)
    "name",         # Match name (opponent)
    "section",      # Match section
    "average",      # Average from edu
    "is_exam",      # Is exam day from edu
    "is_holiday",   # Is holiday from edu
    "days_exam",    # Days until next exam from edu
    "days_holiday", # Days until next holiday from edu
    "week_day",     # Weekday from edu
    "target"        # Calculated target (win / (win + lose))
]

# Prepare data for CSV
csv_data = []
for row in rows:
    year, month, day, name, win, lose, section, average, is_exam, is_holiday, days_exam, days_holiday, week_day = row
    
    # Calculate target: win / (win + lose)
    if win + lose > 0:
        target = win / (win + lose)
    else:
        target = 0.0  # Handle division by zero
    
    # Create a dictionary for the CSV row
    csv_row = {
        "day": day,
        "month": month,
        "year": year,
        "name": name,
        "section": section,
        "average": average,
        "is_exam": is_exam,
        "is_holiday": is_holiday,
        "days_exam": days_exam,
        "days_holiday": days_holiday,
        "week_day": week_day,
        "target": round(target, 3)  # Round to 3 decimal places
    }
    csv_data.append(csv_row)

# Write the data to a CSV file
csv_file = "matches_with_dependencies.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(csv_data)

print(f"CSV file '{csv_file}' has been generated successfully.")

# Close the database connection
connection.close()
