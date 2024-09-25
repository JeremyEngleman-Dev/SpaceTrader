

class Controller:
    def __init__(self, game, view):
        self.game = game
        self.view = view

    def get_current_station(self):
        return self.game.current_station
    
    def get_current_ship(self):
        return self.game.player.ship
    
    def get_player(self):
        return self.game.player
    
    def jump_to_new_station(self):
        ship = self.get_current_ship()
        if ship.fuel_current < ship.engine_burn:
            return
        self.game.jump_to_new_station()
        self.view.refresh_station_window()
        self.view.refresh_ship_window()

    def decrement_fuel_to_buy_amount(self):
        station = self.get_current_station()
        if station.fuel_to_buy_amount == 0:
            return
        station.fuel_to_buy_amount -= 1
        self.view.refresh_fuel_to_buy(station.fuel_to_buy_amount)

    def increment_fuel_to_buy_amount(self):
        station = self.get_current_station()
        ship = self.get_current_ship()
        player = self.get_player()
        if station.fuel_to_buy_amount >= (ship.fuel_capacity - ship.fuel_current):
            return
        if (station.fuel_to_buy_amount + 1) * station.fuel_price > player.account:
            return
        station.fuel_to_buy_amount += 1
        self.view.refresh_fuel_to_buy(station.fuel_to_buy_amount)

    def max_fuel_to_buy_amount(self):
        station = self.get_current_station()
        ship = self.get_current_ship()
        player = self.get_player()
        max = (ship.fuel_capacity - ship.fuel_current)
        if max * station.fuel_price > player.account:
            max = player.account // station.fuel_price
        station.fuel_to_buy_amount = max
        self.view.refresh_fuel_to_buy(station.fuel_to_buy_amount)

    def buy_fuel(self):
        station = self.get_current_station()
        if station.fuel_to_buy_amount == 0:
            return
        ship = self.get_current_ship()
        player = self.get_player()
        player.account -= station.fuel_to_buy_amount * station.fuel_price
        ship.fuel_current += station.fuel_to_buy_amount
        station.fuel_to_buy_amount = 0
        self.view.refresh_station_window()
        self.view.refresh_ship_window()

    def decrement_ware_to_buy_amount(self):
        station = self.get_current_station()
        if station.ware_to_buy_amount == 0:
            return
        station.ware_to_buy_amount -= 1
        self.view.refresh_ware_to_buy(station.ware_to_buy_amount)

    def increment_ware_to_buy_amount(self):
        station = self.get_current_station()
        ship = self.get_current_ship()
        player = self.get_player()
        ship_cargo_size = ship.get_total_cargo_size()
        #if station.ware_to_buy_amount >= (ship.cargo_capacity - ship_cargo_size):
        #    return
        #if (station.ware_to_buy_amount + 1) * station.fuel_price > player.account:
        #    return
        #station.fuel_to_buy_amount += 1
        #self.view.refresh_fuel_to_buy(station.fuel_to_buy_amount)

        
