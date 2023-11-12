# Create a dictionary to hold the open, high, low and close of 4 imaginary companies:
# Python D5, Pythonsoft, Pythazon and Pybook.
# The four sets of data are:
# [12.87, 13.23, 11.42, 13.10]
# [23.54, 25.76, 21.87, 22.33]
# [98.99, 102.34, 97.21, 100.065]
# [203.63, 207.54, 202.43, 205.24]

# set up a list of companies:

company = ['Python D5', 'Pysoft', 'Pythazon', 'Pybook']

# set up the keys:

keys = ['Open', 'High', 'Low', 'Close']

# Set up empty dictionary

co_dict = {}

# set up list containing all data lists

data = [[12.87, 13.23, 11.42, 13.10], [23.54, 25.76, 21.87, 22.33], [
    98.99, 102.34, 97.21, 100.065], [203.63, 207.54, 202.43, 205.24]]

for key in range(len(keys)):
    co_dict[company[key]] = dict(zip(keys, data[key]))
print(co_dict)
