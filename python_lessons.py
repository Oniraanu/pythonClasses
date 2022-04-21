# s = "spam"
# new_s = s[0:1] + 'l' + s[2:4]
# print(new_s)
# print(s)
# my_str = "Hello World"
# var = "e" in my_str
# print(var)
#
# a = 4
# b = 7
# print(a + b)
#
# a = '4'
# b = '9'
# print(a + b)
#
# user_input = int(input('Enter number between 1 and 100: '))
# while user_input != 1:
#     if user_input % 2 != 0:
#         user_input = (user_input * 3) + 1
#     else:
#         user_input = user_input / 2
#     print(user_input)
#
# my_str = input('Enter number: ')
# var = my_str[::-1]
# if my_str == var:
#     print("Palindrome")
# else:
#     print("Not palindrome")
#
# for i in range(11, 1, -1):
#     print('*' * i)
# for i in range(1, 11):
#     print('*' * i)
# user_input = int(input("Enter: "))
# a = range(1, user_input + 1)
# print(len(a))
#
# x = "Hello"
# print(len(x))

# my_str = 'python rules!'
# print(my_str.upper())
# print(my_str.find('r'))

# my_str = 'He had the bat'
# my_str.count('t')
# print(my_str.replace('t', 'd'))

# str = "This is the world of python"
# print(str.upper().count('T'))
# print(str.replace('python', 'java'))
# print(str.replace(' ', ' not ',1))

# print(str.title())

# print("1001001".translate(str.maketrans('01', '10')))
# import string
#
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_lowercase)
#
# print("73543635".translate(str.maketrans('3', '1')))
# print("hello".translate(str.maketrans('o', ' ')) + "is here")

# str = 'hello'
# new_str = 'to you'
# print(f'Bun mi is saying {str}')
# print('Bun mi is saying {} and well done {}'.format(str, new_str))
# print('Bun mi is saying {1} and well done {0}'.format(str, new_str))

# smiley = "\U0001f600"
# for i in range(1, 11, 2):
#     print(f'{smiley*i:>40}')
# dividend = int(input("Enter dividend: "))
# divisor = int(input("Enter divisor: "))
# a, b = div-mod(dividend, divisor)
# print(f"quotient {a} remainder {b}")

# my_dict = {
#     'name': "Bun mi",
#     'age': 18,
#     'sex': 'Male',
#     'hobby': ['Python', 'Java'],
#     'is_wife_beater': False
# }
# print(my_dict)
#
# print(my_dict['age'])
#
# for key in my_dict:
#     print(key, '-->', my_dict[key])
# for key, value in my_dict.items():
#     print(key, '-->', value)
# print(my_dict.items())

lst = ['Who', 'the', 'hell', 'are', 'you']
lst.append(['and', 'what', 'do', 'you', 'want'])
print(lst)
lst.extend(['and', 'wtf'])
print(lst)

