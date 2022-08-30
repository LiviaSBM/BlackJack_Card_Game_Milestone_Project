#Milestone Project of Python Bootcamp - From zero to hero
#BlackJack Card Game

#Definition of cards' suits, ranks and values for further hierarchy settings:
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    #Class for setting up all cards with their suits, ranks and values
    def __init__(self,suit,rank):
        self.suit = suit #Card's suit
        self.rank = rank #Card's rank
        self.value = values[rank] #Card's values
       
    def __str__(self):
        return self.rank+" of "+self.suit #Print card name (i.e: Three of Hearts)

class Deck:
    def __init__(self):
        
        self.all_cards = [] #Main deck (all cards) - empty object
        self.deckp1 = []    #Player 1 Deck
        self.deckp2 = []    #Player 2 Deck
        
        for item1 in suits:
            for item2 in ranks:
                self.all_cards.append(Card(item1,item2)) #Creating main deck
    
    def shuffleanddivide(self):
        
        random.shuffle(self.all_cards) #Shuffling the cards
     
        while len(self.all_cards)>0:
            #While there's cards within the main deck, allocate 1 for P1 and another for P2
            self.deckp1.append(self.all_cards.pop(0))
            self.deckp2.append(self.all_cards.pop(-1))
        
        return [self.deckp1, self.deckp2] #Return deck of P1 and P2

getbothdecks = Deck()
deckjogadores = getbothdecks.shuffleanddivide()