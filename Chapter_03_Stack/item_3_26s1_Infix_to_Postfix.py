# ================================================================================
# Chapter 3 - Item 3: 26s1 Infix to Postfix
# --------------------------------------------------------------------------------
# Problem Statement:
# Receive input in Infix notation and display the result in Postfix notation. The operators used are: +, -, *, /, ^.
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


def infix_to_postfix(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_associative = {'^'}
    output = []
    stack = Stack()

    for ch in expr:
        if ch.isalnum():
            output.append(ch)
        elif ch == '(':
            stack.push(ch)
        elif ch == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        elif ch in precedence:
            while (not stack.is_empty() and stack.peek() != '(' and
                   (precedence[stack.peek()] > precedence[ch] or
                    (precedence[stack.peek()] == precedence[ch] and ch not in right_associative))):
                output.append(stack.pop())
            stack.push(ch)

    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)


def main():
    expr = input("Enter Infix : ")
    result = infix_to_postfix(expr)
    print(f"Postfix : {result}")


if __name__ == "__main__":
    main()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 3 Item 3 (26s1 Infix to Postfix).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================