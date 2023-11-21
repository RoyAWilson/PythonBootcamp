A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
B = [6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]

A = set(A)
B = set(B)
# Intersection
c = A & B
# Union
d = A | B
# Differemce
e = A - B

print(c, d, e)
