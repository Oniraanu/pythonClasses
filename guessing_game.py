user_input = int(input('Enter number between 1 and 100: '))
if 0 < user_input < 73:
    print("Too Low")
elif 73 < user_input < 101:
    print("Too High")
else:
    print("Correct")
