import sqlite3 as sql


# Global file path to database.
db_path = "./SQLiteDB/geocoding_data.db"


class DBConnect:
    def __init__(self):
        try:
            self.conn = sql.connect(db_path)
            self.cursor = self.conn.cursor()
            print("Connected to SQLite database")
        except sql.Error as e:
            print("Error while connecting to SQLite database :", e)

    def create_table(self):
        try:
            self.cursor.execute("CREATE TABLE GeoData(id INTEGER PRIMARY KEY AUTOINCREMENT," +
                                "query TEXT," +
                                "response TEXT);")
            self.conn.commit()
        except sql.OperationalError as e:
            print("Error while creating the Table :", e)
            self.conn.rollback()

    def insert_into_table(self, _query, _response):
        try:
            self.cursor.execute('''INSERT INTO GeoData(query, response) VALUES (?, ?)''',
                                (_query, _response))
            self.conn.commit()
        except sql.OperationalError as e:
            print("Error while inserting to database :", e)
            self.conn.rollback()

    def read_all(self):
        try:
            data = self.cursor.execute(
                "SELECT * FROM GeoData"
            ).fetchall()
            self.conn.commit()
            if data is not None:
                return data
            else:
                return ()
        except sql.OperationalError as e:
            print("Error while reading from database :", e)
            self.conn.rollback()

    def clear_all_history(self):
        try:
            self.cursor.execute("DELETE FROM GeoData")
            self.cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='GeoData';")
            self.conn.commit()
            print("All history Cleared Successfully")
        except sql.OperationalError as e:
            print("Error while clearing :", e)

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed")
