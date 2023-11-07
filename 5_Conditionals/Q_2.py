# Get user to input string number between one and five and print the digit

u_inp: str = input('Please spell a number between one and five:\n\t >> ')
if u_inp.lower() == 'one':
    print('The digit is \'1\'')
elif u_inp.lower() == 'two':
    print('The digit is \'2\'')
elif u_inp.lower() == 'three':
    print('The digit is \'3\'')
elif u_inp.lower() == 'four':
    print('The digit is \'4\'')
elif u_inp.lower() == 'five':
    print('The digit is \'5\'')
else:
    print(f'Sorry your input \'{u_inp} \'is not a string or is out of range.')
