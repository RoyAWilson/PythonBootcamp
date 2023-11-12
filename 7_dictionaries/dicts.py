cntry = {
    'France': {'capital': 'Paris', 'language': 'French'},
    'England': {'capital': 'London', 'language': 'English'},
    'Spain': {'capital': 'Madrid', 'language': 'Spanish'},
    'Norway': {'capital': 'Oslo', 'language': 'Norweegian'},
    'Sweden': {'capital': 'Stockholm', 'language': 'Swedish'},
    'Australia': {'capital': 'Canberra', 'language': 'English'},
    'Germany': {'capital': 'Berlin', 'language': 'German'},
    'Austria': {'capital': 'Vienna', 'language': 'German'},
    'Russia': {'capital': 'Moscow', 'language': 'Russian'},
    'Iceland': {'capital': 'Rejkevik', 'language': 'Icelandic'},
    'Canada': {'capital': 'Torronto', 'language': 'French/English'},
    'Netherlands': {'capital': 'Amsterdam', 'language': 'Dutch'},
    'Portugal': {'capital': 'Lisbon', 'language': 'Portugese'}
}
print(cntry)

for key, value in cntry.items():
    print(f'The capital of {key} is {value['capital']}, they speak the {
          value['language']} language.')
