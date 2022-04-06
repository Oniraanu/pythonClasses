# user_input = int(input('Enter a number: '))

# factors = 1
# sum_of_factors = 0

# while factors < user_input:
#     if user_input % factors == 0:
#         print(factors, 'is a factor of ', user_input)
#     factors = factors + 1

# while factors < user_input:
# if user_input % factors == 0:
#      sum_of_factors += factors
#   factors += 1
# print(sum_of_factors)

# if sum_of_factors == user_input:
#   print(user_input, 'is a perfect number')
# elif sum_of_factors > user_input:
#  print(user_input, 'is an abundant number')
# else:
#    print(user_input, 'is a deficient number')

number = 0
while number < 100:
    number = number + 1
    if number % 15 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
