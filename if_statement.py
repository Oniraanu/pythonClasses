a = int(input('Enter number: '))
if a % 2 == 0:
    print(a, 'is even')
if a % 2 != 0:
    print(a, 'is not even')

# Trying else statement

a = int(input('Enter number: '))
if a % 2 == 0:
    print(a, 'is even')
else:
    print(a, 'is not even')

# Grade

grade = int(input('Enter grade: '))
if grade > 70 and grade == 100:
    print('A')
elif 70 > grade > 59:
    print('B')
elif 60 > grade > 49:
    print('C')
elif 50 > grade > 39:
    print('D')
elif 0 < grade < 40:
    print('F')
else:
    print('Out of range')

# Print one to ten - while

a = 0
while a < 10:
    a = a + 1
    print(a)

x_int = 0

while x_int < 10:
    print(x_int, end='')

    x_int = x_int + 1

print()
print('Final value of x_int: ', x_int)

# For loop

word = "hello"
for letter in word:
    print(letter.upper())

numbers = '123456'
for number in numbers:
    print(number)
