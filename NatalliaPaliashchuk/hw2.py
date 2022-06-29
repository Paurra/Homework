# Homework-4_Python-Functions.md
# Совместный доступ
# P
# Свойства системы
# Тип
# Текст
# Размер
# 4 КБ
# Занимает
# 4 КБ
# Расположение
# Session 4
# Владелец
# Python Training
# Изменено
# 20 апр. 2022 г. (Python Training)
# Открыто
# 22:01 (я)
# Создано"
# 20 апр. 2022 г.
# Описания нет
# Читателям разрешено скачивать файл
# # Python Practice - Session 4


# ### Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.
def replacer(str_):
    table = str_.maketrans("'\"", "\"'")
    return str_.translate(table)



# ### Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
def palindrom_checker(str_): return str_[::-1].upper() == str_.upper()

# ### Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse).
def str_split(s, sep=None):
    if sep is None:
        sep = ' '
    list_, prvs = [], 0
    for indx, _ in enumerate(s):
        if _ == sep and s[indx - 1] != sep:
            list_.append(s[prvs:indx])
            prvs = indx + 1
        elif s[indx - 1] == sep:
            prvs = indx
    if s[prvs:]:
        list_.append(s[prvs:])
    return list_

# ### Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# ```python
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]

# >>> split_by_index("no luck", [42])dx
# ["no luck"]
# ```
def split_by_index(s, indexes):
    list_, prvs = [], 0
    for indx, _ in enumerate(s):
        if indx in indexes:
            list_.append(s[prvs:indx])
            prvs = indx
    list_.append(s[prvs:])
            
    return list_

# ### Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.
# Example:
# ```python
# >>> split_by_index(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
# ```
def get_digits(num):
    return tuple(int(digit) for digit in str(num))

# ### Task 4.6
# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.
# Example:
# ```python
def get_shortest_word(s):
    return max(s.split(), key=lambda word: len(word))


# >>> get_shortest_word('Python is simple and effective!')
# 'effective!'

# >>> get_shortest_word('Any pythonista like namespaces a lot.')
# 'pythonista'
# ```

# ### Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
# Example:
# ```python
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]

# >>> foo([3, 2, 1])
# [2, 3, 6]
# ```
def foo(list_):
    from math import prod
    prod_ = prod(list_) 
    return [prod_ // digit for digit in list_]

# ### Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# ```python
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]

# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

# >>> get_pairs([1])val
# None
# ```
def get_pairs(lst):
    return [(value, lst[index + 1]) for index, value in enumerate(lst[:-1])] 


# ### Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:

# 1) characters that appear ingsstrin all strings

# 2) characters that appear in at least one string

# 3) characters that appear at least in two strings

# 4) characters of alphabet, that were not used in any string

# Note: use `string.ascii_lowercase` for list of alphabet letters

# ```python
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
def test_1_1(*strings):
    return set(''.join(strings)).intersection(*strings)

# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
def test_1_2(*strings):
    return set(''.join(strings))
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
def test_1_4(*strings):
    from string import ascii_lowercase
    return set(ascii_lowercase).difference(*strings)
# ```

# ### Task 4.10
# Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.
# ```python
# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ```
def generate_squares(num):
    return {index: index**2 for index in range(1, num+1)}

# ### Task 4.11
# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
# Dict values ​​should be summarized in case of identical keys

# ```python
# def combine_dicts(*args):
#     ...

# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}

# print(combine_dicts(dict_1, dict_2)
# >>> {'a': 300, 'b': 200, 'c': 300}


# print(combine_dicts(dict_1, dict_2, dict_3)
# >>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}
# ```
def combine_dicts(*args):
    result = {}
    for dict_ in args:
        for key, value in dict_.items():
            result[key] = value + result.get(key, 0)
    return result


# ### Materials
# * [Scope](https://python-scripts.com/scope)
# * [Functions](https://python-scripts.com/functions-python)
# * [Defining your own python function](https://realpython.com/defining-your-own-python-function/)
# * [Python Lambda](https://realpython.com/python-lambda/)
