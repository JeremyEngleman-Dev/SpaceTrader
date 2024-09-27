

class Ware:
    def __init__(
        self,
        name,
        volume,
        low_price=0,
        high_price=0,
        max_stock=0,
        amount=0,
        price=0
    ):
        self.name = name
        self.volume = volume
        self.low_price = low_price
        self.high_price = high_price
        self.max_stock = max_stock
        self.amount = amount
        self.price = price
