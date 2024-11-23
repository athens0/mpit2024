import sqlite3
import pandas as pd

def export_edu_for_2024(database_file, output_csv):
    # Подключение к базе данных
    conn = sqlite3.connect(database_file)
    
    # SQL-запрос для выборки данных из таблицы edu за 2024 год
    query = """
    SELECT *
    FROM edu
    WHERE year = 2024
    """
    
    # Выполнение запроса и загрузка данных в DataFrame
    edu_2024 = pd.read_sql_query(query, conn)
    
    # Переименование столбца id в opponent
    if 'id' in edu_2024.columns:
        edu_2024.rename(columns={'id': 'opponent'}, inplace=True)
    
    # Перемещение opponent в конец таблицы
    columns = [col for col in edu_2024.columns if col != 'opponent'] + ['opponent']
    edu_2024 = edu_2024[columns]
    
    # Сохранение данных в CSV
    edu_2024.to_csv(output_csv, index=False)
    print(f"Файл '{output_csv}' успешно создан с данными за 2024 год!")
    
    # Закрытие соединения
    conn.close()

if __name__ == "__main__":
    # Укажите имя файла базы данных и имя выходного файла CSV
    database_file = 'database.db'  # Замените на имя вашей базы данных
    output_csv = 'data_to_predict.csv'
    
    # Экспорт данных
    export_edu_for_2024(database_file, output_csv)
