# Using the capitals dictionary find the capital of the user input country if it exists, if not print the country is not there.

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

print('To find the capital of a given country:')
question = input('Please enter the country of interest: > ')

# Seems I over-thought the solution to start with

# for k, v in cntry.items():
#     if question in k:
#         print(f'The capital of {question} is {v['capital']}')
#     else:
#         print('Sorry I do not know the captial of that country')

if question in cntry.keys():
    print(f'The capital of {question} is {cntry[question]['capital']}')
else:
    print(f'Sorry, I don\'t know the capital of {question}')
