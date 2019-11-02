def sum_of_digits(number):
    sum = 0
    number = abs(number)
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum


def to_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    digits.reverse()
    return digits


def to_number(digits):
    number = 0
    digits.reverse()
    for digit_index in range(0, len(digits)):
        number += digits[digit_index] * 10 ** digit_index
    return number


def count_vowels(string):
    vowels = "aeiouy"
    return calculate_char_occurrences_in_str(vowels, string)


def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxz"
    return calculate_char_occurrences_in_str(consonants, string)


def calculate_char_occurrences_in_str(characters, string):
    occurrences = 0
    string = string.casefold()
    for character in characters:
        occurrences += string.count(character)
    return occurrences


def prime_number(number):
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return number >= 1


def fact_digits(number):
    sum_fact = 0
    for digit in to_digits(number):
        sum_fact += fact(digit)
    return sum_fact


def fact(number):
    result = 1
    for number in range(1, number + 1):
        result *= number
    return result


def fibonacci(elements_num):
    sequence = []
    for i in range(1, elements_num + 1):
        if i <= 2:
            sequence.append(1)
            continue
        next_num = sequence[-2] + sequence[-1]
        sequence.append(next_num)
    return sequence


def fib_number(elements_num):
    string = ""
    for number in fibonacci(elements_num):
        string += str(number)
    return int(string)


def palindrome(input):
    input = str(input)
    return input[::-1] == input


def char_histogram(string):
    result = {}
    for char in string:
        result[char] = string.count(char)
    return result
