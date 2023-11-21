A = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
B = []
C = []

count = 0


def towers(A, B, C, n):
    global count
    if n == 1:
        disk = A.pop()
        C.append(disk)
        count += 1
    else:
        towers(A, C, B, n-1)
        towers(A, B, C, 1)
        towers(B, A, C, n-1)
    return count


print(towers(A, B, C, 14))
