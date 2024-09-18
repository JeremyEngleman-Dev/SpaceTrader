

class Ware:
    def __init__(
        self,
        name,
        volume,
        low_price,
        high_price,
        max_stock,
    ):
        self.name = name
        self.volume = volume
        self.low_price = low_price
        self.high_price = high_price
        self.max_stock = max_stock

        self.amount = 0
        self.price = 0
