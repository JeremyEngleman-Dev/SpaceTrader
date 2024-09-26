

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
        if station.focused_ware is not None:
            ship = self.get_current_ship()
            ship_cargo_free_space = ship.get_current_cargo_free_space()
            if ship_cargo_free_space >= station.focused_ware.volume * (station.ware_to_buy_amount + 1):
                if station.focused_ware.amount >= (station.ware_to_buy_amount + 1):
                    player = self.get_player()
                    if player.account >= station.focused_ware.price * (station.ware_to_buy_amount + 1):
                        station.ware_to_buy_amount += 1
                        self.view.refresh_ware_to_buy(station.ware_to_buy_amount)
        return
    
    def max_ware_to_buy_amount(self):
        station = self.get_current_station()
        if station.focused_ware is not None:
            ship = self.get_current_ship()
            player = self.get_player()
            ship_cargo_free_space = ship.get_current_cargo_free_space()
            ship_cargo_space_max = ship_cargo_free_space // station.focused_ware.volume
            player_credit_max = player.account // station.focused_ware.price
            station.ware_to_buy_amount = min(ship_cargo_space_max, player_credit_max, station.focused_ware.amount)
            self.view.refresh_ware_to_buy(station.ware_to_buy_amount)

    def on_station_ware_select(self, station_ware):
        if station_ware:
            station = self.get_current_station()
            station.focused_ware = station.stock[int(station_ware)]
            station.ware_to_buy_amount = 0
            self.view.refresh_ware_to_buy(station.ware_to_buy_amount)    

        
