class Customer:
    __customers = [] 
    def __init__(self, name, age):
        Customer.__customers.append(self)
        self.name = name
        self.age = age
        self.customer_id = len(self.__customers) + 1

class Bank(Customer):
    def __init__(self, name, age, branch_name, branch_id):
        super().__init__(name, age)
        self.branch_name = branch_name
        self.branch_id = branch_id
        self.__balance = 0

    def _deposit(self, amount):
        assert amount > 0, "Amount must be greater than 0"
        self.__balance += amount 

    
    def _withdraw(self, amount):
        assert self.__balance >= amount, "Insufficient balance"
        self.__balance -= amount

class Branch(Bank):
    __branches = []
    def __init__(self, name, age, branch_name):
        Branch.__branches.append(self)
        self.__branch_id = len(self.__branches) + 1
        super().__init__(name, age, branch_name= branch_name, branch_id = self.__branch_id)
        
    