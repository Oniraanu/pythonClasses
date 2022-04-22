from typing import List


def bracket_pair(brackets):
    stack: List[str] = []
    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        if bracket in "}])":
            if bracket == "}" and stack[-1] == "{":
                stack.pop()
            elif bracket == "]" and stack[-1] == "[":
                stack.pop()
            elif bracket == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return len(stack) == 0


# print(bracket_pair('{}[{{}}]({[]})'))
# print(bracket_pair('({}[]))'))

def reverse_string(words):
    thing = []
    for word in words:
        thing.pop(words)