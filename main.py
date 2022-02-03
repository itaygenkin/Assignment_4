import os
import sys

import DTO
import Repository
from DAO import Hats, Suppliers, Orders
from DTO import Hat, Supplier


def close_db(connections):
    connections.connections.commit()
    connections.connections.close()


def main():
    if os.path.exists("database.db"):
        os.remove("database.db")
    config = sys.argv[1]
    orders = sys.argv[2]
    global output
    output = sys.argv[3]
    connection = Repository.Repository(sys.argv[4])
    connection.create_tables()

    #reading the config file
    config_reader = open(config, 'r')
    line = config_reader.readline()

    num_of_hats = line[0:line.find(',')]
    num_of_hats = int(num_of_hats)
    num_of_suppliers = line[line.find(',') + 1:]
    num_of_suppliers = int(num_of_suppliers)

    hats = Hats(connection)
    for i in range(0, num_of_hats):
        line = config_reader.readline()
        line = line[:-1]
        arg = line.split(',')

        id = int(arg[0])
        topping = arg[1]
        supplier = int(arg[2])
        quantity = int(arg[3])
        hat = Hat(id, topping, supplier, quantity)
        hats.insert(hat)

    suppliers = Suppliers(connection)
    for i in range(num_of_suppliers):
        line = config_reader.readline()
        line = line[:-1]
        args = line.split(',')
        supplier = Supplier(int(args[0]), args[1])
        suppliers.insert(supplier)

    config_reader.close()

    # reading the orders file
    order_reader = open(orders, 'r')
    order_list = order_reader.readlines()
    order_table = Orders(connection)
    for l in range(0, len(order_list)-1):
        line = order_list[l]
        line = line[:-1]
        args = line.split(',')
        location = args[0]
        topping = args[1]
        add_n = (l < len(order_list) - 2)
        order(hats, location, topping, suppliers, add_n, order_table, l)

    connection.close_db()


def order(hats, location, topping, suppliers, add_n, order_table, order_id):
    hat = hats.get_topping(topping)
    hats.remove_one(hat.id)
    str = hat.topping + ',' + suppliers.find_supplier(hat.supplier)[0] + ',' + location
    ord = DTO.Order(location, hat.id, order_id)
    order_table.insert(ord)
    if add_n:
        str = str + '\n'
    write_to_output_file(str)


def write_to_output_file(x):
    file = open(output, 'a')
    file.write(x)
    file.close()


if __name__ == '__main__':
    main()