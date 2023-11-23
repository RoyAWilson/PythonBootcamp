

def indices(num, targ):
    num_dict = {}
    for i in range(len(num)):
        if targ - num[i] in num_dict:
            return [num_dict[targt - num[i]], i]
        num_dict[num[i]] = i
    return -1


my_nums = [9, 4, 10, 8]
print(indices(my_nums, 7))
