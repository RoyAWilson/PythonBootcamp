
def division(num_1: float, num_2: float) -> float:
    """
    To divide 2 floats and return the result as a float
    Args:
        num_1 (float): numerator
        num_2 (float): denominator

    Returns:
        float: The result of dividing num_1 by num_2
    """
    print('Entering try block')
    print('Checking for division by zero and division by a string')
    try:
        return num_1/num_2
    except ZeroDivisionError as err:
        print(err)
        print('Cannot divide by zero')
    except TypeError as t_err:
        print(t_err)
        print('Cannot divide by a string')
    # else:
    #     print('All Done!')


print(division(2.12, 0))
# Could not get the tutor's way of doing it to work even when coppying the code from the download.
# Could be bexause he was using a jupyter notebook and was running in seperate cells.
