"""
Exception Handling with Try 
"""


def division(num_1: float, num_2: float) -> float:
    """
    To divide 2 floats and return the result as a float
    Args:
        num_1 (float): numerator
        num_2 (float): denominator

    Returns:
        float: The result of dividing num_1 by num_2
    """
    try:
        return num_1/num_2
    except ZeroDivisionError as err:
        print(err)
        print('Cannot divide by zero')
    except TypeError as t_err:
        print(t_err)
        print('Cannot divide by a string')


print(division(2.12, 1.3))
