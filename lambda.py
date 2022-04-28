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

def multiple(x, func):
    return func(x)


double = multiple(5, lambda x: x ** 2)
print(double)
triple = multiple(11, lambda x: x ** 3)
print(triple)
