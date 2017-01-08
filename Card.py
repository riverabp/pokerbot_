class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def describe(self):
        if self.rank == 10:
            print 'T'
        elif self.rank == 11:
            print 'J'
        elif self.rank == 12:
            print 'Q'
        elif self.rank == 13:
            print 'K'
        elif self.rank == 14:
            print 'A'
        else:
            print self.rank

        print self.suit

Card('C', 12)



