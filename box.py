from dataclasses import dataclass

class Box:
    def add(self, item):
        raise NotImplementedError()
    def empty(self):
        raise NotImplementedError()
    def count(self):
        raise NotImplementedError()

@dataclass
class Item:
    name: str
    value: int

class ListBox(Box):
    def __init__(self, items=[]):
        self.items = items
    def add(self, item):
        self.items.append(item)
    def count(self):
        return len(self.items)
    def empty(self):
        items = []

class DictBox(Box):
    def __init__(self, items={}):
        self.items = items
    def add(self, item):
        self.items[item.name] = item
    def count(self):
        return len(self.items)
    def empty(self):
        items = {}


lb = ListBox()
lb.add(Item('left shoe', 1))
lb.add(Item('right shoe', 1))
print(lb.count())
print(lb.items)

db = DictBox()
db.add(Item('left shoe', 1))
db.add(Item('right shoe', 1))
print(db.count())
print(db.items)
