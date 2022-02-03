import sqlite3
import os
import importlib
import atexit
import sys
import Repository
from DAO import Hats, Suppliers
from DTO import Hat, Supplier, Order


def close_db(connections):
    connections.commit()
    connections.close()


def main():
    config = sys.argv[1]
    orders = sys.argv[2]
    global output
    output = sys.argv[3]
    connection = Repository(sys.argv[4])
    connection.create_tables()

    #reading the config file
    config_reader = open(config, 'r')
    line = config_reader.readline()

    num_of_hats = line[0:line.find(',')]
    hats = Hats(connection)
    for i in num_of_hats:
        line = config_reader.readline()
        end = line.find(',')
        id = line[:end]
        start = end + 1
        end = line.find(',', start, end)
        topping = line[start:end]
        start = end + 1
        end = line.find(',', start, end)
        supplier = line[start:end]
        start = end + 1
        quantity = line[start:]
        hat = Hat(id, topping, supplier, quantity)
        hats.insert(hat)

    num_of_suppliers = line[line.find(',')+1:]
    suppliers = Suppliers(connection)
    for i in num_of_suppliers:
        line = config_reader.readline()
        id = line[:line.find(',')]
        name = line[line.find(',')+1:]
        supplier = Supplier(id, name)
        suppliers.insert(supplier)
    config_reader.close()

    # reading the orders file
    order_reader = open(orders, 'r')
    order_list = order_reader.readlines()
    for l in range(0, len(order_list)):
        line = order_list[l]
        location = line[:line.find(',')]
        topping = line[line.find(',') + 1:]
        add_n = (l < len(order_list) - 1)
        order(hats, location, topping, suppliers, add_n, orders)


    atexit.register(close_db)


if __name__ == '__main__':
    main()


def order(hats, location, topping, suppliers, add_n, orders):
    hat = hats.get_topping(topping)
    hats.remove_one(hat.id)
    str = hat.topping + ',' + suppliers.find_supplier(hat.supplier) + ',' + location
    ord = Order(location, hat)
    orders.insert(ord)
    if add_n:
        str = str + '\n'
    write_to_output_file(str)



def write_to_output_file(x):
    file = open(output, 'a')
    file.write(x)
    file.close()

