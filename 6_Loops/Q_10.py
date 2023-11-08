# write code to determine the odd and even numbers between 1 and 100 and put them in lists odd and even

evens = []
odds = []

for i in range(1, 101):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print(f'Even numbers between 1 and 100: {
      evens}\nOdd numbers between 1 and 100: {odds}')
