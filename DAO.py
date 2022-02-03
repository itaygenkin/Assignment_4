from DTO import Hat


class Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
                INSERT INTO hats (id, topping, supplier, quantity) VALUES(?, ?, ?, ?)
            """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def get_topping(self, _topping):
        cur = self._conn.cursor()
        cur.execute("""
            SELECT id, topping, supplier, quantity FROM hats WHERE topping = ?
            """, [_topping])
        return Hat(*cur.fetchone())

    def remove_one(self, _id):
        cur = self._conn.cursor()
        quant = cur.execute("""
            SELECT quantity FROM hats WHERE id = (?)
            """, [_id])
        self._conn.execute("""
            UPDATE hats SET quantity = (?) WHERE id = (?)
            """, [quant - 1, _id])
        if quant == 1:
            self._conn.execute("""
                DELETE FROM hats WHERE id = ?
                """, [_id])


class Suppliers:
    def __init__(self, _conn):
        self._conn = _conn

    def insert(self, supplier):
        self.conn.execute("""
                INSERT INTO suppliers(id, name) VALUES(?, ?)
            """, [supplier.id, supplier.name])

    def find_supplier(self, _id):
        cur = self._conn.cursor()
        cur.execute("""
            SELECT name FROM suppliers WHERE id = (?)
            """, [_id])
        return cur.fetchone()


class Orders:
    def __init__(self, _conn):
        self.conn = _conn
    def insert(self, order):
        self.conn.execute("""
                INSERT INTO orders(id, location, hat) VALUES(?, ?, ?)
            """, [order.id, order.location, order.hat])