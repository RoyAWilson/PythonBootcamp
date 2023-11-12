# Create a dictionary containing four suits of 13 cards, ace low

# Create list of cards and list of face values:

suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
face_vals = ['Ace', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = {}

# And zip them together - Zip work - the lists are different lengths

# deck = dict(zip(suits, face_vals))

for i in suits:
    deck[i] = face_vals
print(deck)
