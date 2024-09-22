

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
        self.game.jump_to_new_station()
        self.view.refresh_station_window()