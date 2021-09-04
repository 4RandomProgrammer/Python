#Deck of cards
import random

class Card:
    #Criando as cartas
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    def show(self):
        print("{} de {}".format(self.value, self.suit))

class Deck:
    #Inicializando o  deck
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        #Criando um deque de 52 duas cartas
        for s in ["Paus", "Espadas", "Ouros", "Copas"]:
            for v in range(1,14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        if(len(self.hand) < 5)
            self.hand.append(deck.drawCard())
            return self

    def showHand(self):
        for card in self.hand:
            card.show()

deck = Deck()
deck.shuffle()
card = deck.drawCard()
card.show()

x = 1 