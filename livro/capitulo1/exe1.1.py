import collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FreeDeck:
    ranks =  [ str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, key):
        return self._cards[key]

    def _choice(self):
        print(choice(self._cards))

suit_values = dict(spades=3, diamonds=2, clubs=1, hearts=0)

def spades_higth(card):
    rank_value = FreeDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

deck = FreeDeck()

for card in sorted(deck,key=spades_higth):
    print(card)
