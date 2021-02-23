class Numbers:
    MULTIPLIER = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y
    @classmethod
    def multiply(cls, a):
        return  a * cls.MULTIPLIER
    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return x, y

    @value.setter
    def value(self, new):
        self.x = new[0]
        self.y = new[1]
    
    @value.deleter
    def value(self):
        del(self.x)
        del(self.y)

x = Numbers(1,2)
print(x.sum())
x.value = 2, 3
print(x.sum())