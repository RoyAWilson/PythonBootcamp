def fun_mean(first, *remainder):
    # print(first + sum(remainder) / 1 + len(remainder))
    return (first + sum(remainder))/((1 + len(remainder)))


print(fun_mean(5, 5, 5, 5, 5))
