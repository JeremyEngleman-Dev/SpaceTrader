from ware import *

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

    def buy_ware(self):
        station = self.get_current_station()
        if station.ware_to_buy_amount == 0:
            return
        ship = self.get_current_ship()
        player = self.get_player()
        player.account -= station.focused_ware.price * station.ware_to_buy_amount
        ship_cargo_index = ship.check_for_ware_in_cargo(station.focused_ware.name)
        if ship_cargo_index is None:
            ship.cargo.append(Ware(station.focused_ware.name,station.focused_ware.volume,0,0,0,station.ware_to_buy_amount, station.focused_ware.price))
        else:
            ship.cargo[ship_cargo_index].amount += station.ware_to_buy_amount
        station.focused_ware.amount -= station.ware_to_buy_amount
        station.ware_to_buy_amount = 0
        self.view.refresh_station_window()
        self.view.refresh_ship_window()

    def decrement_ware_to_sell_amount(self):
        ship = self.get_current_ship()
        if ship.ware_to_sell_amount == 0:
            return
        ship.ware_to_sell_amount -= 1
        self.view.refresh_ware_to_sell(ship.ware_to_sell_amount)

    def increment_ware_to_sell_amount(self):
        ship = self.get_current_ship()
        if ship.focused_ware is not None:
            station = self.get_current_station()
            station_stock_index = station.check_for_ware_in_stock(ship.focused_ware.name)
            if station_stock_index is None:
                return
            if ship.ware_to_sell_amount + 1 <= ship.focused_ware.amount:
                 ship.ware_to_sell_amount += 1
                 self.view.refresh_ware_to_sell(ship.ware_to_sell_amount)
        return

    def max_ware_to_sell_amount(self):
        ship = self.get_current_ship()
        if ship.focused_ware is not None:
            station = self.get_current_station()
            station_stock_index = station.check_for_ware_in_stock(ship.focused_ware.name)
            if station_stock_index is None:
                return
            ship.ware_to_sell_amount = ship.focused_ware.amount
            self.view.refresh_ware_to_sell(ship.ware_to_sell_amount)

    def sell_ware(self):
        ship = self.get_current_ship()
        if ship.ware_to_sell_amount == 0:
            return
        player = self.get_player()
        station = self.get_current_station()
        station_ware_index = station.check_for_ware_in_stock(ship.focused_ware.name)
        if station_ware_index is None:
            return
        player.account += station.stock[station_ware_index].price * ship.ware_to_sell_amount
        station.stock[station_ware_index].amount += ship.ware_to_sell_amount
        ship.focused_ware.amount -= ship.ware_to_sell_amount
        ship_ware_index = ship.check_for_ware_in_cargo(ship.focused_ware.name)
        if ship.cargo[ship_ware_index].amount == 0:
            ship.cargo.pop(ship_ware_index)
        ship.ware_to_sell_amount = 0   
        self.view.refresh_station_window()
        self.view.refresh_ship_window()

    def on_ship_ware_select(self, ship_ware):
        if ship_ware:
            ship = self.get_current_ship()
            ship.focused_ware = ship.cargo[int(ship_ware)]
            ship.ware_to_sell_amount = 0
            self.view.refresh_ware_to_sell(ship.ware_to_sell_amount)