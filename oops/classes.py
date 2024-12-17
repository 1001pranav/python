class Food:
    all=[]
    def __init__(self, name: str, price: float, quantity: int, discount=1):

        #Basic Validation
        """
        Initialize a Food object with name, price and quantity.
        
        Args:
            name (str): Name of the food.
            price (float): Price of the food. Should be more than 0.
            quantity (int): Quantity of the food. Should be more than 0.
        
        Raises:
            AssertionError: If the price or the quantity is not more than 0.
        """
        assert price>0, f"Price {price} should be more than 0"
        assert quantity > 0, f"Quantity {quantity} should be more than 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__discount_rate = discount
        Food.all.append(self)
    

    def calculate_price(self) -> float:
        return self.price * self.quantity - (self.price * self.quantity * self.__discount_rate)
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    def __str__(self):
        return f"Name - '{self.name}', Price - {self.price}, Quantity - {self.quantity} Discount price - {self.calculate_price()}  Initial Price - {self.price * self.quantity} Discount % - {self.__discount_rate * 100}"
    
banana = Food('Banana', 3.5, 10, 0.0134)
apple = Food('apple', 7.6, 30, 0.43)

print(f"Price for Banana - {banana.calculate_price()}") 
print(f"Price for Apple - {apple.calculate_price()}")

print(f'Price of apple after discount - {apple.calculate_price()}')
print(Food.all)

print('__str__', banana.__str__())
print('__str__',apple.__str__())
print('__repr__',apple.__repr__())

