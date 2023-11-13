# Create a class that when instantiated returns a playing card and displays it.
import random


class Playing_Card(object):
    '''
    Define a class to pick a playing card
    '''

    suit_int = random.randint(1, 4)

    def __init__(self):

        # Define suits:
        self.a = 'Diamonds'
        self.b = 'Hearts'
        self.c = 'Spades'
        self.d = 'Clubs'
        self.suit = ''
        self.sI = 0
        vI = 0

        # Define Value:
        self.value = ['Duece', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'Jack', 'Queen', 'King']
        self.face = ''
        # Get randomised suit:
        self.sI = random.randint(1, 4)
        if self.sI == 1:
            self.suit = self.a
        elif self.sI == 2:
            self.suit = self.b
        elif self.sI == 3:
            self.suit = self.c
        else:
            self.suit = self.d

        # Get random face value:

        vI = random.randint(1, 13)
        self.face = self.value[vI]
        print(f'Your card is {self.face} of {self.suit}')


Playing_Card()
