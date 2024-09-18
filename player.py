from ship import *

class Player:
    def __init__(self, name, ship_name):
        self.name = name
        self.ship = Ship(ship_name,100,100,10)
        self.account = 1000