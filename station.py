import random

class Station:
    def __init__(self):
        self.stock = []
        self.fuel_price = None
        self.generate_stock(self.stock)

    def generate_stock(self, stock):
        self.fuel_price = random.randrange(2, 15)
        ware_variety = random.randrange(3,8)
        