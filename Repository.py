import sqlite3
import os
import importlib
import atexit


class Repository:
    def __init__(self):
        self.connections = sqlite3.connect('myDB.db')

    def create_tables(self):
        self.connections.execute("""
        CREATE TABLE suppliers (
            id      INTEGER     PRIMARY KEY,
            name    STRING      NOT NULL
        );
        CREATE TABLE hats (
            id      INTEGER     PRIMARY KEY,
            topping STRING      NOT NULL,
            supplier INTEGER    NOT NULL,
            FOREIGN KEY(supplier) REFERENCES suppliers(id),
            quantity INTEGER NOT NULL
        );
        CREATE TABLE orders (
            id          INTEGER     PRIMARY KEY,
            location    STRING      NOT NULL,
            hat         INTEGER     NOT NULL,
            FOREIGN KEY(hat)        REFERENCES hats(id)
        );
        """)

    def close(self):
        self.connections.commit()
        self.connections.close()