# def divide(a, b):
#     if b <= 0:
#         raise ValueError("Denominator cannot be 0 or less than 0")
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         raise TypeError("Use your head nowwww")
#     return int(a) / int(b)
#
#
# # print(divide(2, 0))
# # print(divide(2, -2))
# # print(divide(100, 100))
#
# num = int(input("Enter numerator: "))
# den = int(input("Enter denominator: "))
# while True:
#     try:
#         print(divide(num, den))
#         break
#     except (ValueError, TypeError):
#         print("Wrong Value")
#         num = int(input("Enter numerator: "))
#         den = int(input("Enter denominator: "))

try:
    print("Life's good")
    # print(4 / 0)
    print([1, 2, 3, 4][6])

except ZeroDivisionError as e:
    print("ZeroError", e)
except IndexError as e:
    print("IndexError", e)
else:
    print("I run only when theres no error")
finally:
    print("I run everytime")
