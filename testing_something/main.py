# import  module_1
# import module_2
#
# module_1.greet("Bunmi")
# module_2.depart("Bunmi")

# import module_1 as one
# import  module_2 as two
#
# one.greet("Pythonista")
# two.depart("Pythonista")

# from testing_something import module_1, module_2
# module_1.greet("Ali")
# module_2.depart("Ali")
# from testing_something import module_1, module_2
# from testing_something.sub_package import module_3
# for person in module_3.people:
#     module_1.greet(person)
#
# for person in module_3.people:
#     module_2.depart(person)

from module_1 import greet
from module_2 import depart
from sub_package.module_3 import people

for person in people:
    greet(person)
for person in people:
    depart(person)

