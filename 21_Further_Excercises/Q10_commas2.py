'''
Write a function def add_commas(numbers) that will add commas to an integer and return it as a string.
For example add_commas(1000000) will return 1,000,000 Do it first without using string fomratting
or f strings.
'''


def add_commas(numbers: int) -> str:
    num_list = []
    count: int = 1
    retstr: str = ''
    if numbers < 1000:
        return str(numbers)
    numbers = str(numbers)
    for digits in numbers[:len(numbers)]:
        if count == 1:
            num_list.append(digits + ',')
        elif (count - 1) % 3 != 0:
            num_list.append(digits)
        else:
            num_list.append(digits)
            num_list.append(',')
        count += 1
    if num_list[-1] == ',':
        num_list = num_list[:-1]
        print(123)
    for items in num_list:
        # print(items)
        retstr += items
    return retstr


x = add_commas(10000000)

print(x)

# This isn't working need to reverse the number and add comma at every third space from back end
