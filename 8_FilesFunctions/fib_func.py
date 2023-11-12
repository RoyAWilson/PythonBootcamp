# Code to produce a fibonacci sequence from user input

def fib(n):
    '''
    Calculates and returns the fibonacci sequence to input length
    '''
    a = 0
    b = 1
    seq = []
    for i in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


n = input('Enter a number: > ')
while not n.isdigit():
    print('please only enter numbers: > ')
    n = input('Try again: > ')
n = int(n)

print(fib(n))
