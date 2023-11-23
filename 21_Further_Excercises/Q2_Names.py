'''
To input five names separated by a comma and print the five names as a list
'''

inp_names: str = ''
lst_names: list = []

inp_names = input('Please input 5 names seperated by a comma: > ')

lst_names = inp_names.split(',')

print(lst_names)
