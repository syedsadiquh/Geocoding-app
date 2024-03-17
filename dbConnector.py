import sqlite3 as sql


class DBConnect:
    def __init__(self, file_name):
        try:
            self.conn = sql.connect(file_name)
            self.cursor = self.conn.cursor()
            print("Connected to SQLite database")
        except sql.Error as e:
            print("Error while connecting to SQLite database :", e)

    def create_table(self, table_name):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS ? (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            query TEXT, response TEXT''',
                                (table_name,))
        except sql.OperationalError:
            pass

    def insert_into_table(self, table_name, _query, _response):
        try:
            self.cursor.execute("INSERT INTO ?(query, response) VALUES (?, ?)",
                               [(table_name, _query, _response)])
        except sql.OperationalError:
            print("Error while inserting to database.")

    def read_all(self, table_name):
        data = self.cursor.execute(
            "SELECT * FROM ?",
            (table_name,)
        ).fetchall()
        return data

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed")
