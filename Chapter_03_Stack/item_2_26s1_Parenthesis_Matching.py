# ================================================================================
# Chapter 3 - Item 2: 26s1 Parenthesis Matching
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program to check if an expression has complete parentheses using a Stack to solve the problem.
# The program should be able to indicate the cause of the error, if any:
# Mismatched opening and closing parenthesesExcess closing parenthesesExcess opening parenthesesThen display the result according to the example.
# ================================================================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def to_string(self):
        return ''.join(self.items)


def check_expression(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = Stack()

    for ch in s:
        if ch in '([{':
            stack.push(ch)
        elif ch in ')]}':
            if stack.is_empty():
                return "close paren excess", None, None
            top = stack.pop()
            if top != pairs[ch]:
                return "Unmatch open-close", None, None

    if not stack.is_empty():
        return "open paren excess", stack.size(), stack.to_string()

    return "MATCH", None, None


def main():
    s = input("Enter expresion : ")
    status, count, chars = check_expression(s)

    if status == "open paren excess":
        print(f"{s} {status}   {count} : {chars}")
    else:
        print(f"{s} {status}")


if __name__ == "__main__":
    main()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 3 Item 2 (26s1 Parenthesis Matching).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================