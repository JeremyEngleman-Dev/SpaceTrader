

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
        self.cargo_level = 1
        self.fuel_capacity = fuel_capacity
        self.fuel_current = fuel_capacity
        self.fuel_level = 1
        self.engine_burn = engine_burn
        self.engine_level = 1

        def get_total_cargo_size(self):
            total_cargo_size = 0
            for ware in self.cargo:
                total_cargo_size += ware.volume * ware.amount
            return total_cargo_size
