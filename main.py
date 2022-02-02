import sqlite3
import os
import importlib
import atexit
import sys
import Repository


def main():
    config = sys.argv[1]
    orders = sys.argv[2]
    global output
    output = sys.argv[3]
    connection = Repository(sys.argv[4])
    connection.create_tables()
    #TODO: read the orders


if __name__ == '__main__':
    main()


def order(hats, location, topping, suppliers):
    hat = hats.get_topping(topping)
    write_to_output_file(hat.topping + ',' + suppliers.find_supplier(hat.supplier) + ',' + location)


def write_to_output_file(x): #TODO: add '\n'
    file = open(output, 'a')
    file.write(x)
    file.close()






