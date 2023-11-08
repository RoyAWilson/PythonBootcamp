# Write code to calculate a list of the first 20 numbers in the fibonacci sequence

# First set variables to the first 2 numbers in the sequence and list to hold the results

fib_1st = 0
fib_2nd = 1
fib_lstd = []
n = 20

for i in range(n):
    fib_lstd.append(fib_1st)
    fib_1st, fib_2nd = fib_2nd, fib_1st + fib_2nd
print(fib_lstd)
