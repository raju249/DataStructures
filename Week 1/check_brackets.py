# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def isBalanced(text):
    stack = []
    for index, next in enumerate(text, start = 1):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            stack.append(Bracket(next, index))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if not stack:
                return index

            top = stack.pop()

            if not top.Match(next):
                return index
    if stack:
        return stack.pop().position
    return "Success"

if __name__ == "__main__":
    text = sys.stdin.read()
    print (isBalanced(text))
