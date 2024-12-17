class Food:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self) -> float:
        return self.price * self.quantity

    def __str__(self):
        return f"Name - '{self.name}', Price - {self.price}, Quantity - {self.quantity}"

class ReturnedFood(Food):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.total_amount = 0

    def calculate_price(self) -> float:
        self.total_amount = ((super().calculate_price() * 18) / 100) + super().calculate_price()

    def get_price(self):
        print(f'total amount is {self.total_amount}')

    def __str__(self):
        return f'{super().__str__()} Total amount - {self.total_amount}'

banana = ReturnedFood('Banana', 3.5, 10)
apple = ReturnedFood('apple', 7.6, 30)
grapes = ReturnedFood('grapes', 7.65, 40)

print(f"Price for Banana - {banana.calculate_price()}") 
print(f"Price for Apple - {apple.calculate_price()}")
print(f"Price for Grapes - {grapes.calculate_price()}")


banana.get_price()
apple.get_price()

print('__str__', banana.__str__())
