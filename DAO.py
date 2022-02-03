from DTO import Hat


class Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        cur = self._conn.connections.cursor()
        cur.execute("""
                INSERT INTO hats (id, topping, supplier, quantity) VALUES(?, ?, ?, ?)
            """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def get_topping(self, _topping):
        cur = self._conn.connections.cursor()
        cur.execute("""
            SELECT id, topping, supplier, quantity FROM hats WHERE topping = ?
            """, [_topping])
        a = cur.fetchall()
        id = 110
        index = 0
        for i in range(len(a)):
            if id > a[i][2]:
                id = a[i][2]
                index = i
        return Hat(*a[index])

    def remove_one(self, _id):
        cur = self._conn.connections.cursor()
        quant = cur.execute("""
            SELECT quantity FROM hats WHERE id = (?)
            """, [_id])
        x = int(*quant.fetchone())
        cur.execute("""
            UPDATE hats SET quantity = (?) WHERE id = (?)
            """, [x - 1, _id])
        if x == 1:
            cur.execute("""
                DELETE FROM hats WHERE id = ?
                """, [_id])


class Suppliers:
    def __init__(self, _conn):
        self._conn = _conn

    def insert(self, supplier):
        cur = self._conn.connections.cursor()
        cur.execute("""
                INSERT INTO suppliers(id, name) VALUES(?, ?)
            """, [supplier.id, supplier.name])

    def find_supplier(self, _id):
        cur = self._conn.connections.cursor()
        cur.execute("""
            SELECT name FROM suppliers WHERE id = (?)
            """, [_id])
        x = cur.fetchone()
        return x


class Orders:
    def __init__(self, _conn):
        self._conn = _conn
    def insert(self, order):
        cur = self._conn.connections.cursor()
        cur.execute("""
                INSERT INTO orders(id, location, hat) VALUES(?, ?, ?)
            """, [order.id, order.location, order.hat])