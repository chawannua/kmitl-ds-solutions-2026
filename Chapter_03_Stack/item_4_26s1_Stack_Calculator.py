# ================================================================================
# Chapter 3 - Item 4: 26s1 Stack Calculator
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a class calculator that operates through the function run(instructions) with the following instructions:
# +: Pop 2 values from the stack, add them, and push the result onto the stack.-: Pop 2 values from the stack, subtract the top value from the second value, and push the result onto the stack.*: Pop 2 values from the stack, multiply them, and push the result onto the stack./: Pop 2 values from the stack, divide the second value by the top value, and push the result onto the stack.DUP: Duplicate (not double) the top value of the stack.POP: Pop the top value from the stack and discard it.PSH: Push a number onto the stack.Note: Any other instructions (such as letters) should result in "Invalid instruction: [instruction]".
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


class Calculator:
    def __init__(self):
        self.stack = Stack()

    def run(self, instructions):
        self.stack = Stack()
        tokens = instructions.split()
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token == '+':
                x = self.stack.pop()
                y = self.stack.pop()
                self.stack.push(x + y)
            elif token == '-':
                x = self.stack.pop()
                y = self.stack.pop()
                self.stack.push(x - y)
            elif token == '*':
                x = self.stack.pop()
                y = self.stack.pop()
                self.stack.push(x * y)
            elif token == '/':
                x = self.stack.pop()
                y = self.stack.pop()
                self.stack.push(x / y)
            elif token == 'DUP':
                self.stack.push(self.stack.peek())
            elif token == 'POP':
                self.stack.pop()
            elif token == 'PSH':
                i += 1
                self.stack.push(float(tokens[i]))
            else:
                try:
                    num = float(token)
                    self.stack.push(num)
                except ValueError:
                    return f"Invalid instruction: {token}"
            i += 1

        if self.stack.is_empty():
            return 0

        result = self.stack.peek()
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return result


def main():
    print("* Stack Calculator *")
    instructions = input("Enter arguments : ")
    calc = Calculator()
    result = calc.run(instructions)
    print(result)


if __name__ == "__main__":
    main()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 3 Item 4 (26s1 Stack Calculator).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================