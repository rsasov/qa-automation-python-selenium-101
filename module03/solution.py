def sum_of_digits(number):
    """
    Calculates the sum of the digits of number
    :param number: input number
    :return: sum of the digits of number
    """
    sum = 0
    number = abs(number)
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum


def to_digits(number):
    """
    Calculates the digits of the number
    and return them as list
    :param number: input number
    :return: list of the digits of number
    """
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    digits.reverse()
    return digits


def to_number(digits):
    """
    Returns number containing the input digits
    :param digits: list of digits
    :return: number formed with the input digits
    """
    number = 0
    digits.reverse()
    for digit_index in range(0, len(digits)):
        number += digits[digit_index] * 10 ** digit_index
    return number


def count_vowels(string):
    """
    Calculates the count of all vowels in the string
    :param string: input string
    :return: count of the vowels in the string
    """
    vowels = "aeiouy"
    return calculate_char_occurrences_in_str(vowels, string)


def count_consonants(string):
    """
    Calculates the count of all consonants in the string
    :param string: input string
    :return: count of the consonants in the string
    """
    consonants = "bcdfghjklmnpqrstvwxz"
    return calculate_char_occurrences_in_str(consonants, string)


def calculate_char_occurrences_in_str(characters, string):
    """
    Calculates the occurrences of the input characters
    in the input string
    :param characters: characters to count
    :param string: input string
    :return: the count of all input characters in the string
    """
    occurrences = 0
    string = string.casefold()
    for character in characters:
        occurrences += string.count(character)
    return occurrences


def prime_number(number):
    """
    Checks if a number is prime
    :param number: input number
    :return: True if number is prime, False otherwise
    """
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return number >= 1


def fact_digits(number):
    """
    Calculates the sum of the factorials
    for each digit of number
    :param number: input number
    :return: the sum of the factorials
    for each digit of number
    """
    sum_fact = 0
    for digit in to_digits(number):
        sum_fact += fact(digit)
    return sum_fact


def fact(number):
    """
    Calculates the factorial of a number
    :param number: input number
    :return: The factorial of number
    """
    result = 1
    for number in range(1, number + 1):
        result *= number
    return result


def fibonacci(elements_num):
    """
    Calculates Fibonacci sequence for elements_num members
    :param elements_num: number of sequence members
    :return: Fibonacci sequence as list
    """
    sequence = []
    for i in range(1, elements_num + 1):
        if i <= 2:
            sequence.append(1)
            continue
        next_num = sequence[-2] + sequence[-1]
        sequence.append(next_num)
    return sequence


def fib_number(elements_num):
    """
    Calculates number based on members of Fibonacci sequence
    :param elements_num: number of sequence members
    :return: Number formed by concatenation of the sequence members
    """
    string = ""
    for number in fibonacci(elements_num):
        string += str(number)
    return int(string)


def palindrome(input):
    """
    Checks if the input is palindrome
    :param input:
    :return: True if the input is palindrome, else False
    """
    input = str(input)
    return input[::-1] == input


def char_histogram(string):
    """
    Returns a map with characters of the string as keys
    and their occurrences as values
    :param string: input string
    :return: Map populated with characters of string as keys
    and the occurrences of the characters in the string as values
    """
    result = {}
    for char in string:
        result[char] = string.count(char)
    return result
