from collections import namedtuple
from dataclasses import dataclass

class Deck:
    ranks = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']
    suits = ['clubs','spades','hearts','diamonds']
    def __init__(self, name):
        Card = namedtuple('Card', 'rank suit')
        self.name = name
        self.cards = []
        for rank in self.ranks:
            for suit in self.suits:
                self.cards.append(Card(rank=rank, suit=suit))

@dataclass
class Card:
    rank: str
    suit: str

class Deck2:
    ranks = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']
    suits = ['clubs','spades','hearts','diamonds']
    def __init__(self, name):
        self.name = name
        self.cards = []
        for rank in self.ranks:
            for suit in self.suits:
                self.cards.append(Card(rank=rank, suit=suit))    

a = Deck2('one')
print(a.cards)
