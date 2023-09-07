import sqlite3
 
class ClientDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
 
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            visits INTEGER,
            month TEXT
        )''')
        self.conn.commit()
 
    def insert_client(self, name, visits, month):
        self.cursor.execute('''INSERT INTO clients (name, visits, month) VALUES (?, ?, ?)''', (name, visits, month))
        self.conn.commit()
 
    def fetch_data(self):
        self.cursor.execute('''SELECT month, SUM(visits) FROM clients GROUP BY month''')
        data = self.cursor.fetchall()
        return data
 
    def close(self):
        self.conn.close()
