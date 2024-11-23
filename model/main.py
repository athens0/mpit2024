import pandas as pd
import sqlite3
from sklearn.ensemble import RandomForestRegressor

def train_and_save_predictions(train_file, predict_file, database_file):
    
    df_train = pd.read_csv(train_file)
    data_to_predict = pd.read_csv(predict_file)

    target = df_train['result']

    train_data = df_train.drop(columns=['result'])


    #X_train, X_test, y_train, y_test = train_test_split(train_data, target, test_size=0.3)

    model = RandomForestRegressor()
    model.fit(train_data, target)

    predict = model.predict(data_to_predict)
    
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calendar (
        year INTEGER,
        month INTEGER,
        day INTEGER,
        prediction REAL,
        section TEXT
    )
    ''')
    
    data_to_save = data_to_predict[['year', 'month', 'day']]
    data_to_save['section'] = 'basketball'
    data_to_save['prediction'] = predict
    data_to_save.to_sql('calendar', conn, if_exists='append', index=False)
    print("Предсказания успешно добавлены в таблицу 'calendar'!")
    
    conn.close()

if __name__ == "__main__":
    
    train_file = 'training_basketball.csv'         
    predict_file = 'data_to_predict.csv'
    database_file = 'database.db'
    
    train_and_save_predictions(train_file, predict_file, database_file)
