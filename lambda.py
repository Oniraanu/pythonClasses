# Lambdas are anonymous functions
# var = lambda x, y: x + y
# print(var.__name__)

# def add(a, b):
#     return a + b
#
#
# def sub(c, d):
#     return d - c
#
#
# def multiply(first_number, second_number):
#     return first_number * second_number
#
#
# def operate(x, y, func):
#     return func(x, y)
#
#
# val_sub = operate(5, 20, sub)
# val_add = operate(10, 27, lambda x, y: y + x)
# val_multiply = operate(10, 5, multiply)
# val_div = operate(3, 9, lambda x, y: y / x)
#
#
# print(val_sub)
# print(val_add)
# print(val_multiply)
# print(multiply(2, 5))
# print(val_add)
# print(val_div)

# def multiple(x, func):
#     return func(x)
#
#
# double = multiple(5, lambda x: x ** 2)
# print(double)
# triple = multiple(11, lambda x: x ** 3)
# print(triple)

# people = [
#     {"name": "Bakre Olubunmi", "age": 27, "languages": ["Java", "Python", "JavaScript", "GoLang"]},
#     {"name": "Love Orobola", "age": 12, "languages": ["Java", "Python", "JavaScript"]},
#     {"name": "Tolani Jinadu", "age": 24, "languages": ["HTML", "CSS", "JavaScript"]},
#     {"name": "Osula Ebube", "age": 25, "languages": ["Java", "C++"]},
# ]
#
# print([person["age"] >= 20 and "Java" in person["languages"] for person in people])
#
# map_object = map(lambda x: x ** 2 if x % 2 == 0 else x, range(1, 10))
# lst1 = list(map_object)
# lst2 = list(map_object)
#
# print("1", lst1)
# print("2", lst2)


# def is_even(x):
#     return x % 2 == 0
#
#
# filter_obj = list(filter(is_even, range(1, 10)))
# print(filter_obj)
#
# another_lambda = is_even(10)
# print(another_lambda)
#
# test_lambda = list(filter(lambda x: x % 2 == 0, range(1, 10)))
# print(test_lambda)
from functools import reduce
#
# test = reduce(lambda x,  y: x + y, range(1, 10))
# print(test)

fruits = ["Apple", "Pear", "Pineapple", "Orange", "Watermelon", "Banana", "Cucumber"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, fruits)
print(longest)

fruits = ["Apple", "Pear", "Pineapple", "Orange", "Watermelon", "Banana", "Cucumber"]
shortest = reduce(lambda x, y: x if len(x) < len(y) else y, fruits)
print(shortest)
print(max(fruits, key=len))
print(min(fruits, key=len))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(sorted(fruits))
print(sorted(fruits, key=lambda x: x[-1]))


