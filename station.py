import random
from library import *

class Station:
    def __init__(self, wares):
        self.stock = []
        self.fuel_price = None
        self.fuel_to_buy_amount = 0
        self.ware_to_buy_amount = 0
        self.generate_stock(wares)
        self.focused_ware = None

    def generate_stock(self, wares):
        self.fuel_price = random.randrange(2, 15)
        station_ware_count = random.randrange(3,8)
        stock_list = [x for x in wares]
        while len(self.stock) != station_ware_count:
            self.stock.append(stock_list.pop(random.randrange(len(stock_list) - 1)))
        for ware in self.stock:
            ware.amount = random.randrange(ware.max_stock)
            ware.price = random.randrange(ware.low_price, ware.high_price)

    def check_for_ware_in_stock(self, ware_name):
        for ware in self.stock:
            if ware.name == ware_name:
                return self.stock.index(ware)
        return None
        
