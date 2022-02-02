import sqlite3
import os
import importlib
import atexit


if __name__ == '__main__':
    print('PyCharm')

def main():
    connections = sqlite3.connect('myDB.db')

    connections.execute("""
    CREATE TABLE suppliers (
        id INTEGER PRIMARY KEY,
        name STRING NOT NULL
    )""")

    connections.execute("""
    CREATE TABLE hats (
        id INTEGER PRIMARY KEY,
        topping STRING NOT NULL,
    supplier INTEGER,
        FOREIGN KEY(supplier) REFERENCES suppliers(id),
        quantity INTEGER NOT NULL
    )""")

    connections.execute("""
        CREATE TABLE orders (
            is INTEGER PRIMARY KEY,
            location STRING NOT NULL,
        )hat""")

