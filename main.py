import sqlite3
import os
import importlib
import atexit

import Repository

if __name__ == '__main__':
    print('PyCharm')

def main():
    connection = Repository()
    connection.create_tables()

def order(connection, location, topping):


def write_to_output_file(x):
    file = open("output.txt", 'a')
    file.write(x)
    file.close()





