import sqlite3
import os
import importlib
import atexit
import sys

import Repository

if __name__ == '__main__':
    print('PyCharm')

def main():
    config = sys.argv[1]
    orders = sys.argv[2]
    output = sys.argv[3]
    connection = Repository(sys.argv[4])
    connection.create_tables()

def order(connection, location, topping):
    return

def write_to_output_file(x):
    file = open("output.txt", 'a')
    file.write(x)
    file.close()





