from ware import *

class Ship:
    def __init__(
        self,
        name,
        cargo_capacity,
        fuel_capacity,
        engine_burn
    ):
        self.name = name
        self.cargo_capacity = cargo_capacity
        self.cargo = []
        self.fuel_capacity = fuel_capacity
        self.fuel_current = fuel_capacity
        self.engine_burn = engine_burn
        self.ware_to_sell_amount = 0
        self.focused_ware = None

    def get_current_cargo_size(self):
        current_cargo_size = 0
        for ware in self.cargo:
            current_cargo_size += ware.volume * ware.amount
        return current_cargo_size
    
    def get_current_cargo_free_space(self):
        current_cargo = self.get_current_cargo_size()
        return self.cargo_capacity - current_cargo
    
    def check_for_ware_in_cargo(self, ware_name):
        for ware in self.cargo:
            if ware.name == ware_name:
                return self.cargo.index(ware)
        return None