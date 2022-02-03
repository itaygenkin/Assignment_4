class Hat:
    def __init__(self, id, topping, supplier, quantity):
        self.id = id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity


class Supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Order:
    id = 1
    def __init__(self, location, hat):
        id = id + 1
        self.id = id
        self.location = location
        self.hat = hat
