s = "spam"
new_s = s[0:1] + 'l' + s[2:4]
print(new_s)
print(s)
my_str = "Hello World"
var = "e" in my_str
print(var)

a = 4
b = 7
print(a + b)

a = '4'
b = '9'
print(a + b)

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

for i in range(11, 1, -1):
    print('*' * i)
for i in range(1, 11):
    print('*' * i)
