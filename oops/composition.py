# “has-a” relationship where an object contains other objects.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.car = None

    def start(self):
        if self.car is None:
            print(f"Engine with {self.horsepower} HP started.")
        else:
            print(f"Engine with {self.horsepower} HP started. {self.car.brand} {self.car.model}")

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine  # Has-a relationship
        self.engine.car = self

    def start(self):
        print(f"Starting {self.brand} {self.model}.")
        self.engine.start()

# Usage
engine = Engine(200)
car = Car("Toyota", "Camry", engine)

car.start()
# Output:
# Starting Toyota Camry.
# Engine with 200 HP started. 