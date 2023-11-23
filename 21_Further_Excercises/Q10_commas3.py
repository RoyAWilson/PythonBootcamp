'''
Write a function def add_commas(numbers) that will add commas to an integer and return it as a string.
For example add_commas(1000000) will return 1,000,000 Do it first without using string fomratting
or f strings.
'''


def add_commas(numbers: int) -> str:
    num_list = []
    count: int = 1
    retstr: str = ''
    count: int = 1
    if numbers < 1000:
        return str(numbers)
    else:
        numbers = str(numbers)
        # num_list.append(numbers[-1])
        for digits in range(len(numbers), 0, -1):
            if count % 3 == 0 and digits > 1:
                num_list.append(numbers[digits - 1])
                num_list.append(',')
            else:
                num_list.append(numbers[digits - 1])
            count += 1
        for i in range(len(num_list), 0, -1):
            retstr += num_list[i-1]
    return retstr


x = add_commas(100000)
print(x)

# This one works.  Feel stupid to have not worked out
# that I needed to start at the back end and work to the front!
