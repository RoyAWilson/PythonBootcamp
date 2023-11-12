# Using listzip function

my_list = [1, 2, 3, 4, 5]
my_list_3 = ['A', 'B', 'C', 'D']

joined = list(zip(my_list, my_list_3))

print(joined)
print(type(joined))

# zip is a class of it's own:

joined_1 = zip(my_list, my_list_3)
print(type(joined_1))

# zip used to separate the list into 2 tuples. Note the asterisk

i, j = zip(*joined)
print(i, j)
print(type(i), type(j))

capitals = {
    'France': 'Paris',
    'England': 'London',
    'Sapin': 'Madrid',
    'Norway': 'Oslo',
    'Sweden': 'Stockholm',
    'Australia': 'Canberra',
    'Germany': 'Berlin',
    'Austria': 'Vienna',
    'Russia': 'Moscow',
    'Iceland': 'Rejkevik',
    'Canada': 'Torronto',
    'Netherlands': 'Amsterdam',
    'Portugal': 'Lisbon'
}
print(capitals)
print(type(capitals))

# NB the .items() to unpack the dictionary

country, city = zip(*capitals.items())
print(country, city)
print(type(country), type(city))
