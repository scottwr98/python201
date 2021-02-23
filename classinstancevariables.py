class Demo:
    names = []
    def __init__(self, name):
        self.name = name
        self.names.append(name)

    def __del__(self):
        self.names.remove(self.name)
a = Demo('a')
b = Demo('b')
print(Demo.names)
del(a)
print(Demo.names)