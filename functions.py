# def get_digit(number, position):
#     """return digit at position in number, counting from right"""
#     return number // (10 ** position) % 10
#
#
# print(get_digit(12, 1))
# # help(get_digit)
#
# assert 4 == 2, "4 is not equal to 2"

def get_digit(number: int, position: int) -> int:
    """get the digit at a particular position

    >>> get_digit(234, 0)
    4
    >>> get_digit(234, 2)
    2
    >>> 3 == 4
    False
    >>> [1, 2, 3, 4, 5] [::-1]
    [5, 4, 3, 2, 1]
    >>> x #doctest : +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    NameError: name 'x' is not defined


    """
    return number // (10 ** position) % 10


print(get_digit(123, 2))
