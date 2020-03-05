#Jasper John D. Calambro
#CPE106 - B1
#Group09
# Pile class code
class Pile:

    def __init__(self): #This is a constructor that creates 3 lists namely: cards, players and bonus.
        self.cards = []	  #A list named cards is initialized and created.
        self.players = [] #A list named players is initialized and created.
        self.bonus = []	  #A list named bonus is initialized and created.

    def addCards(self, card, player): #This method accepts two parameters card and player
        self.cards.append(card)	      #The parameter card is added to the existing pile of cards
        self.players.append(player)   #The existing list of players is added with a parameter player
				      
"""
Few methods such as addCards and addBonuses
utilizes some built-in functions:
 a.append - this is used to add an element the end of the list.
 b.extend - this is almost acts as an append, but it adds multiple elements instead.
"""
    def addBonuses(self, cards): #This method accepts cards as its parameter.     
        self.bonus.extend(cards) #The parameter is then added by the built-in function 'extend' 
				 #to the existing bonus list

    @property
    def winner(self): 
        self.show_pile() #The function show_pile is called in this line
        values = [card.value for card in self.cards]
        self.best = max(values) #The maximum value is searched using the built-in function max
        if values.count(self.best) == 1:
            return self.players[values.index(self.best)]

    def show_pile(self):
        for player, card in zip(self.players, self.cards):
            print('{} laid down a {}.'.format(player.name, card))

    def reward(self, player): #This method accepts the player parameter
        player.giveCards(self.cards) 
        player.giveCards(self.bonus)

    @property
    def tied(self):
        for card, player in zip(self.cards, self.players):
            if card.value == self.best:
                yield player