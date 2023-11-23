'''
Write a function def add_commas(numbers) that will add commas to an integer and return it as a string.
For example add_commas(1000000) will return 1,000,000 Do it first without using string fomratting
or f strings.
'''


def add_commas(numbers: int) -> str:
    num_list = []
    count: int = 0
    retstr: str = ''
    if numbers < 1000:
        return str(numbers)
    numbers = str(numbers)
    for digits in numbers:
        if count == 0:
            num_list.append(digits + ',')
        elif count < 3:
            num_list.append(digits)
        elif count == 3:
            num_list.append(digits + ',')
        elif count == 6 and len(numbers) > 8:
            num_list.append(digits + ',')
        else:
            num_list.append(digits)
        count += 1
    for items in num_list:
        # print(items)
        retstr += items
    return retstr


x = add_commas(7000000)
print(x)

# It works up to a point, needs a rethink - not happy with the number of elif statements not at all sustainable.
