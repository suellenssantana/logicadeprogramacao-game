import sqlite3

class DBProxy:
    def __init__(self, db_name='DBScore'):
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')

    def save(self, score_data):
        self.connection.execute('INSERT INTO scores (name, score, date) VALUES (?, ?, ?)', score_data)
        self.connection.commit()

    def retrieve_top10(self):
        return self.connection.execute('SELECT name, score, date FROM scores ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        self.connection.close()