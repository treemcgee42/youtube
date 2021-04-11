from manimlib.imports import *
from manimlib.PlayingCard import PlayingCard
from random import randint

class CardDeck:
    def __init__(self):
        self.cards = []
        for suit in ["hearts", "spades", "diamonds", "clubs"]:
            for number in (list(range(2,11)) + ["J", "Q", "K", "A"]):
                self.cards.append(PlayingCard(suit, number))
    
    def shuffle(self):
        shuffled_cards = []
        while len(self.cards) != 0:
            random_index = randint(0, len(self.cards)-1)
            selected_card = self.cards.pop(random_index)
            shuffled_cards.append(selected_card)
        self.cards = shuffled_cards
    
    def get_hand(self, n=10):
        card_mobjects = []
        i = 0
        while i < n:
            the_card = self.cards[i].make_card()
            the_card.shift((.6*i)*RIGHT)
            card_mobjects.append(the_card.copy())
            i += 1
            
        return card_mobjects
