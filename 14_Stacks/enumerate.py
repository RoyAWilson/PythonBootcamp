alphabet: str = 'abcdefghijklmnopqrstuvwxyz'

alpha_list: list = list(alphabet)

for i in range(len(alpha_list)):
    print(i, alpha_list[i])

for count, item in enumerate(alpha_list, start=12):
    print(item)
