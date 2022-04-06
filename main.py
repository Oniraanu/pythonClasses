user_input = int(input('Enter number between 1 and 100: '))
while user_input != 1:
    if user_input % 2 != 0:
        user_input = (user_input * 3) + 1
    else:
        user_input = user_input / 2
    print(user_input)

my_str = input('Enter number: ')
var = my_str[::-1]
if my_str == var:
    print("Palindrome")
else:
    print("Not palindrome")
