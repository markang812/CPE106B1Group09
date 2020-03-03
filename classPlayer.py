# Loven Garcia
# CPE106/B1
# Group 9
# Player class code
class Player:

    def __init__(self, name, hand):
        self.name, self.hand = name, hand

    def placeCard(self, collection):
        if self.hand.has_cards:
            collection.addCards(self.hand.take_top(), self) #checks if a player have cards. If yes, the cards will be added to the pile of the player.


    def placeBonus(self, collection, count):
        collection.addBonuses(self.hand.cards[:count])
        self.hand.cards = self.hand.cards[count:]

    def giveCards(self, cards):
        self.hand.add_all(cards)  #gives the player their respective pile of cards

    def showHand(self):
        print(str(self.name)+ ' has ' + str(self.hand)) #prints out the card that is drawn by the player
