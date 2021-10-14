import collections
from random import choice

Card = collections.namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(1,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)   for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def get_ranks(self):
        return self.ranks
    
    def get_suits(self):
        return self.suits


f = FrenchDeck()
# print(f[:])
# print(f.get_ranks())
# print(f.get_suits())

# beer_card = Card('7',['David','Turati'])
# print(beer_card)
# print(len(f))

# f_choice = choice(f)

# print(f_choice)

for card in f:
    print(card)