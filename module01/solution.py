def f_c(x):
    """
    Function returning constant of 4
    :param x: input
    :return: value of 4
    """
    return 4


def f_x(x, a, b):
    """
    Function returning the result from the formula:
    a * x + b
    :param x: input x
    :param a: input a
    :param b: input b
    :return: result from a * x + b
    """
    return a*x + b


def sum(x):
    """
    Function returning the sum from executing f_x 3 times
    Inputs a and b that are used for the function calls: 1, 2, 3
    :param x: input
    :return: the sum of 3 executions for f_x
    """
    result = 0
    count = 1
    while count <= 3:
        result += f_x(x, count, count)
        count += 1
    return result
