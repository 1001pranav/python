class Food:
    all=[]
    discount_rate=0.2
    def __init__(self, name: str, price: float, quantity: int):

        #Basic Validation
        assert price>0, f"Price {price} should be more than 0"
        assert quantity > 0, f"Quantity {quantity} should be more than 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        Food.all.append(self)
        

    def calculate_price(self) -> float:
        return self.price * self.quantity
    
    def apply_discount(self) -> float:
        self.price = self.price * self.discount_rate 
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
class ReturnedFood:
    def __init__(self, name: str, price: float, quantity: int, returned_food: int):
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity
        self.returned_food = returned_food
    def calculate_price(self):
        return self.price * (self.quantity - self.returned_food)    

banana = Food('Banana', 3.5, 10)
apple = Food('apple', 7.6, 30)
grapes = ReturnedFood('grapes', 7.65, 40, 12)

print(f"Price for Banana - {banana.calculate_price()}") 
print(f"Price for Apple - {apple.calculate_price()}")
print(f"Price for Grapes - {grapes.calculate_price()}")
apple.apply_discount()
print(f'Price of apple after discount - {apple.calculate_price()}')
print(Food.all)


