import sqlite3


class Repository:
    def __init__(self, db_location):
        self.connections = sqlite3.connect(db_location)

    def create_tables(self):
        cur = self.connections.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id      INTEGER     PRIMARY KEY,
            name    STRING      NOT NULL
        )""")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS hats (
            id      INTEGER     PRIMARY KEY,
            topping STRING      NOT NULL,
            supplier INTEGER    NOT NULL,
            quantity INTEGER    NOT NULL,
            FOREIGN KEY(supplier) REFERENCES suppliers(id)
        )""")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id          INTEGER     PRIMARY KEY,
            location    STRING      NOT NULL,
            hat         INTEGER     NOT NULL,
            FOREIGN KEY(hat)        REFERENCES hats(id)
        )""")

    def close_db(self):
        self.connections.commit()
        self.connections.close()