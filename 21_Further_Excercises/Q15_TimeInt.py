''''
Write a function that takes a positive integer n and converts it into hours and minutes.
45 would return 0h:45mins 135 would return 2h:15mins
'''


def IntToTime(num: int) -> str:
    hours = ''
    mins = ''

    hours = hours + str(int(num/60))
    mins = mins + str(num % 60)

    return f'{hours}:{mins}'


x = IntToTime(135)
print(x)
