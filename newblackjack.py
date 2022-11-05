import random

FACES = list(range(2,11)) + ["Jack", "Queen", "King", "Ace"]
SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]

class Card(object):
    """A BlackJack card"""
    def __init__(self, face, suit):
        assert face in FACES and suit in SUITS
        self.face = face
        self.suit = suit

    def __str__(self): # __str__ 을 사용하면 
        article = "a "
        if card.face in [8, "Ace"]:
            article = "an "
        return article + str(card.face) + " of " + card.suit 

    def value(self):
        if type(self.face) == int:
            return self.face
        elif self.face == "Ace":
            return 11
        else :
            return 10

def hand_value(hand):
    total = 0
    for card in hand :
        total += card.value()
    return total


hand = [ Card("Ace", "Spades"),
         Card(8, "Diamonds"),
         Card("Jack", "Hearts"),
         Card(10, "Clubs") ]

card = Card("Ace", "Spades")