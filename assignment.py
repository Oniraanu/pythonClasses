# add numbers
sum = 0
total = 1
user_input = int(input("Enter number: "))
for i in range(1, user_input + 1):
    sum = sum + 1
    total = sum + 1
    print(total)


# factorial
import math

user_input = int(input("Enter number: "))
answer = math.factorial(user_input)
print(answer)

# fibonacci sequence
user_input = int(input("Enter number: "))
a, b = 0, 1
while a < user_input:
    print(a)
    a, b = b, a + b


