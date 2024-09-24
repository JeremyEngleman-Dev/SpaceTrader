

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
        station.fuel_to_buy_amount = (ship.fuel_capacity - ship.fuel_current)
        self.view.refresh_fuel_to_buy(station.fuel_to_buy_amount)

    def buy_fuel(self):
        ship = self.get_current_ship()
        
