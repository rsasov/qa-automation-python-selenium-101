IS_TRUE = True

IS_FALSE = False

PANCAKE_INGREDIENTS = {
    "flour" : 2,
    "eggs" : 4,
    "milk" : 200,
    "butter" : False,
    "salt" : 0.001
}

FIBONACCI_NUMBERS = [
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
]

def num_add(a, b):
    """Adds two numbers together"""
    return a + b


def num_sub(a, b):
    """Subtracts two numbers"""
    return a - b


def num_mul(a, b):
    """Multiplies two numbers"""
    return a * b


def num_div(a, b):
    """Divides two numbers"""
    return a / b


def num_floor(a, b):
    """Implements floor division"""
    return a // b


def num_rem(a, b):
    """Implements remainder division"""
    return a % b


def ingredient_exists(ingr, dict):
    """
    Checks if an ingredient exists
    :param ingr - ingredient to check
    :return True if ingredient exists, False otherwise
    """
    return ingr in dict


def fatten_pancakes(dict):
    """
    Makes a flatten pancake with the increasing of
    the eggs to 6 and adding butter
    :param dict: initial ingredients
    :return: resulting ingredients for fatten pancakes
    """
    result_dict = dict.copy()
    result_dict["eggs"] = 6
    result_dict["butter"] = True
    return result_dict


def add_sugar(dict):
    """Adds sugar to the ingredients"""
    result_dict = dict.copy()
    result_dict["sugar"] = True
    return result_dict


def remove_salt(dict):
    """Removes salt from the ingredients"""
    result_dict = dict.copy()
    del result_dict["salt"]
    return result_dict


def add_fibonacci(lst):
    """
    Adds next fibonacci number
    :param lst - initial fibonacci sequence
    :return extended sequence with next number
    """
    next_fibonacci_number = lst[-2] + lst[-1]
    lst.append(next_fibonacci_number)
    return lst


def fib_exists(lst, n):
    """
    Checks if a number is part of the fibonacci sequence
    :param lst - initial fibonacci sequence
    :param n - number to check
    :return True if n is present in lst, else False
    """
    return lst.count(n) > 0


def which_fib(lst, n):
    """
    Returns the index of n in the sequenct lst starting from 1
    :param lst: initial fibonacci sequence
    :param n: number to search for
    :return: index of n in the lst
    """
    return lst.index(n) + 1

