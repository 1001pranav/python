class Food:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self) -> float:
        return self.price * self.quantity
    
    def __str__(self):
        return f"Name - '{self.name}', Price - {self.price}, Quantity - {self.quantity}"

class Fruits(Food):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.total_amount = 0

    def calculate_price(self) -> float:
        self.total_amount = ((super().calculate_price() * 18) / 100) + super().calculate_price()
        return self.total_amount
    
    def get_price(self):
        return f'{super().__str__()} Total amount - {self.total_amount}'
    
class Vegetables(Food):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.total_amount = 0    

    def calculate_price(self) -> float:
        self.total_amount = ((super().calculate_price() * 12) / 100) + super().calculate_price()
        return self.total_amount
    
    def get_price(self):
        return f'{super().__str__()} Total amount - {self.total_amount}'
    

Mango = Fruits("Mango", 100, 2)
Apple = Fruits("Apple", 50, 3)
Tomato = Vegetables("Tomato", 20, 5)
Cabbage = Vegetables("Cabbage", 100, 4)

def print_price(obj):
    print(obj.get_price())

Mango.calculate_price()
Apple.calculate_price()
Tomato.calculate_price()
Cabbage.calculate_price()

print_price(Mango)
print_price(Apple)
print_price(Tomato)
print_price(Cabbage)

# print(Mango.__str__())
# print(Apple.__str__())
# print(Tomato.__str__())
# print(Cabbage.__str__())