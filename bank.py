import math

class Calculator(object):
    def __init__(self):
        self.value = 0
        self.history = []
    def add(self, a, b = None):
        b = b or self.value
        self.value =  a + b or self.value
        self.history.append(f"{a} + {b} = {self.value}")
        return self.value
    def sub(self, a, b = None):
        b = b or self.value
        self.value =  a - b
        self.history.append(f"{a} - {b} = {self.value}")        
        return self.value        
    def mult(self, a, b = None):
        b = b or self.value
        self.value =  a * b
        self.history.append(f"{a} * {b} = {self.value}")        
        return self.value        
    def div(self, a, b = None):
        b = b or self.value
        self.value =  a / b 
        self.history.append(f"{a} / {b} = {self.value}")        
        return self.value        
    def pow(self, a, b = None):
        b = b or self.value
        self.value =  a ** b
        self.history.append(f"{a} ** {b} = {self.value}")        
        return self.value        
    def log(self, a):        
        self.value =  math.log(a)
        self.history.append(f"log({a}) = {self.value}")
        return self.value
    def ac(self):
        self.value = 0
        self.history = []
        return self.value                
    def showcalc(self):
        return self.history

class BankAccount2(object):
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def __repr__(self):
        '''unambiguous representation of the object'''
        return self.__class__.__name__ + '(' + repr(self.name) + ', ' + repr(self.balance) + ')'

    def __str__(self):
        '''string representation of object, for humans
        __repr__ is used if __str__ does not exist'''
        return self.name + ' has ₹' + str(self.balance) + ' in the bank'
   
    def __add__(self, other):
        return self.__class__(self.name + ' + ' + other.name, 
                           self.balance + other.balance - 5.95)

    def __eq__(self, other):
        '''implementation of =='''
        return self.balance == other.balance

    def __mul__(self, other):
        '''implementation of *'''
        return BankAccount2(f"{self.name} * {other.name}", self.balance * other.balance)

    def __len__(self):
        '''implementation of len'''
        return 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("can't deposit nonpositive amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("can't withdraw", amount, "or you would be overdrawn!")
        else:
            print("can't withdraw nonpositive amount!")


calc = Calculator()
print(calc.add(1,2))
print(calc.add(1))
print(calc.mult(2))
print(calc.showcalc())

