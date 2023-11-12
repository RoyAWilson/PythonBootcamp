# Create a dictionary to enumerate the first 12 values of the fibonacci sequence

# First generate the fibonacci sequence:
# create variables to hold the first 2 values of the sequence, number of iterations  and empty dictionary to hold sequence

a: int = 0
b: int = 1
num: int = 12
fib_seq: dict = {}

# Now create the sequence in a dictionary

for i in range(1, num + 1):
    fib_seq[i] = a
    a, b = b, a + b
print(fib_seq)
