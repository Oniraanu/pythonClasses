# # Exercise 8.1
# a = float(input("Enter amount:"))
# print(f'*****{a:>5}')
# a = float(input("Enter amount:"))
# print(f'*****{a:^5}')
# a = float(input("Enter amount:"))
# print(f'*****{a:<5}')
#
# # Exercise 8.2
# article = []
# noun = []
# verb = []
# preposition = []
#
#
# # Exercise 8.3
# my_str = input("Enter your sentence:")
# first, second, third = my_str.split()
# print(first + "ay" + " " + second + "ay" + " " + third + "ay")
#
# # Exercise 8.4
# my_str = input("Enter your sentence:")
# new_str = my_str[::-1]
# print(new_str)
#
# # Exercise 8.5
# str = "Someone exists below and above, we don't know who it is"
# print(str.count('b'))

# factorial


# def find_occurrence(s, count=None):
#     for i in s:
#         if s[0] == i:
#             count += 1
#             print(i, count)
#
#
# print(find_occurrence("google", 0))


# def sort_occurrence():
#     pass

set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]
new_set = []
for i in set2:
    if i not in set1:
        new_set.append(i)
for i in set1:
    if i not in set2:
        new_set.append(i)
print(new_set)
print(sum(new_set))














