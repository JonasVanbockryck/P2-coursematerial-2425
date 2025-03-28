class Money:
    def __init__(self, money, currency):
        self.amount = money
        self.currency = currency
    
    def __add__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount + other.amount, 
                self.currency
            )
        else:
            raise RuntimeError
    
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount - other.amount, 
                self.currency
            )
        else:
            raise RuntimeError
    
    def __mul__(self, amount):
        if isinstance(amount, int) or isinstance(amount, float):
            return Money(
                self.amount * amount,
                self.currency
            )
        else:
            raise RuntimeError
    
    @property
    def currency(self):
        return self.__currency
    
    @currency.setter
    def currency(self, value):
        if isinstance(value, str):
            self.__currency = value
        else:
            raise ValueError("currency needs to be a string!")

# usa = Money(20, "Dollarydoos")
# us2 = Money(40, "Dollarydoos")

# us3 = (usa + us2)
# print(us3.money)