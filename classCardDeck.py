#Trisha Anne Santos
#CPE106/B1
#Group09
# CardDeck class code
class CardDeck:

    def __init__(self):
        self.cards = [Card(s, r) for s in Card.SUITE for r in Card.RANKS] #perform list comprehension to add all Card objects to a list called cards

    def shuffle(self):
        random.shuffle(self.cards) #shuffles deck

    def setupPlayerHand(self, players):
        hands = [player.hand for player in players] #gives player the deck
        while len(self.cards) >= len(players):
            for hand in hands:
                hand.addCards(self.cards.pop()) #adds the cards to the player while also removing a card from the stack
        return hands
