import sqlite3
import os
import importlib


class Repository:
    def __init__(self, db_location):
        self.connections = sqlite3.connect(db_location)

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

