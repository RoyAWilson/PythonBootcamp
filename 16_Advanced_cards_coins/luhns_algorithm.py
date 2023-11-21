'''
Code to use Luhn's algorithm to check if credit card number is valid.
'''


def luhns(cc_n) -> str:
    '''
    To take a CC number run it through luhn's algorithm and return a valid or invalid response
    A string of numbers should be passed to the function

    '''

    rev_str: str = ''
    rev_sum: int = 0
    other_nums: int = 0
    num: list = []
    rev: list = []

    for dig in range(0, len(cc_n)):
        num.append(cc_n[dig])
    for digi in range(len(num)-2, -1, -2):
        rev.append(num[digi])
    for i in range(len(rev)):
        rev[i] = int(rev[i])*2
    for j in range(len(rev)):
        rev_str += str(rev[j])
    for k in rev_str:
        rev_sum += int(k)
    for l in range(0, len(cc_n) + 1, 2):
        other_nums += int(cc_n[l])
    if (other_nums + rev_sum) % 10 == 0:
        return True
    else:
        return False


x = luhns('371449635398431')
print(f'The result of running Luhn\' algorithm on your number is:\n {
      x}.  If True then it is a good number; if falise it is a bad number')

# Could be tidied up considerably.
# Maybe use fewer loops and do additions and multiplications on list members
# using something along the lines of x = cc_n[i] + z or  cc_n[i] *2
# Should really have an input string to hold allow input of the CC no
# But it works on tested CCNs
