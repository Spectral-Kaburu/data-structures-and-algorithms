from collections import deque


def is_balanced(string):
    braces = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    brackets = [']', '}', ')']
    check = []
    for char in string:
        if char in braces:
            check.append(char)
            continue
        if char not in brackets:
            continue
        if len(check) == 0:
            return False
        if char == braces[check[-1]]:
            check.pop()
            continue

    return len(check) == 0


def reverse_string(string):
    restr = ''
    for char in reversed(string):
        restr += char

    return restr


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def push_left(self, val):
        return self.container.appendleft(val)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return self.container == 0

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)


stack = Stack()
print(is_balanced("({[[{()}]]})"))
print(reverse_string("this is a cryptic looking sentence"))
