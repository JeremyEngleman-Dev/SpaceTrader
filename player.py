

class Player:
    def __init__(self, name):
        self.name = name

        self.player_account = 500
        self.player_score = 0

    def add_money(self, amount):
        self.player_account += amount

    def remove_money(self, amount):
        self.player_account -= amount

    def add_score(self, amount):
        self.player_score += amount