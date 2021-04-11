from manimlib.imports import *

class PlayingCard:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
        card_rectangle = RoundedRectangle()
