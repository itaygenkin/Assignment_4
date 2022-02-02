class Hats:
    def __init__(self, conn):
        self._conn = conn
    def insert(self, hat):
        self._conn.execute("""
                INSERT INTO hats (id, toppings, supplier, quantity) VALUES(?, ?, ?, ?)
            """, [hat.id, hat.topping, hat.supplier, hat.quantity])
    def get_topping(self, topping):

        return


class Suppliers:
    def __init__(self, _conn):
        self.conn = _conn
    def insert(self, supplier):
        self.conn.execute("""
                INSERT INTO suppliers(id, name) VALUES(?, ?)
            """, [supplier.id, supplier.name])


class Orders:
    def __init__(self, _conn):
        self.conn = _conn
    def insert(self, order):
        self.conn.execute("""
                INSERT INTO orders(id, location, hat) VALUES(?, ?, ?)
            """, [order.id, order.location, order.hat])