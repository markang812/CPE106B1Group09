#
#
# Card class code
class Card:

    SUITE = 'H D S C'.split() #this gives us a list of the 4 suits
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split() #this gives us a list of all the possible values of the deck

    def __init__(self, suite, rank): #self explanatory assignments
        self.suite, self.rank = suite, rank

    def __str__(self):
        return '{}-{}'.format(self.rank, self.suite)

    @property
    def value(self): 
        return self.RANKS.index(self.rank)
