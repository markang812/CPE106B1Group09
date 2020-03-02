#Ang, Mark Christian
#CPE106/B1

#Game class code with class Hand

class Game:

    def __init__(self, players):
        self.players = [Player(name, Hand()) for name in players] #creaters a list of players for the game
        self.deck = CardDeck() #creates a deck for the game
        self.rounds = 0 #initially set the round to 0
    
    def printFormat(self,string, line):
        print('\n{}\n{}'.format(string, line * len(string))) #simple formatting for ease of use

    def dealCards(self): 
        self.deck.shuffle() #shuffles deck so that its random
        self.deck.setupPlayerHand(self.players) #gives each players their deck
        for player in self.players:
            player.showHand()  #this function shows the player's card to the others for comparison

    def playOnce(self, tied=None):
        if tied is None:
            self.roundCount() #incremets the round
        collection = Pile()
        for player in (self.players if tied is None else tied):
            player.placeCard(collection)
            if tied:
                player.placeBonus(collection, 3)
        winner = collection.winner
        if winner is not None:
            collection.reward(winner)
        else:
            winner = self.playOnce(collection.tied)
            collection.reward(winner)
        return winner

    def roundCount(self):
        self.rounds += 1
        self.printFormat('Starting round {}'.format(self.rounds), '=')

    def play(self):
        while not self.finished:  #this is a major part of the game loop
            self.playOnce()
        self.showWinner()

    def showWinner(self):
        for player in self.players:
            if player.hand.has_cards:
                print()
                print(player.name, 'wins!')  #simple function to indicate that a player has won
                break

    @property
    def finished(self):
        return sum(bool(player.hand.cards) for player in self.players) == 1


#added a hand class to make it easier 
class Hand:
    
    def __init__(self):
        self.cards = [] #list for all the cards in the player's hands

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def addCards(self, card):
        self.cards.append(card) #appends cards to the player's hands

    def take_top(self):
        return self.cards.pop(0) #pops the first card in the stack

    def add_all(self, cards):
        self.cards.extend(cards)

    @property
    def has_cards(self):
        return bool(self.cards) #checks if the player has cards