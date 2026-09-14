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
# A tiny stack-machine interpreter: each whitespace-separated token is either
# pushed as data or executed as an instruction against a single shared Stack.
#
# Core idea:
#   run() rebuilds self.stack fresh on every call (so a Calculator instance
#   is reusable across inputs), then walks tokens with a manual index `i`
#   instead of a for-loop because 'PSH' must consume the FOLLOWING token as
#   its argument (i += 1 inside the PSH branch, then i += 1 again at the
#   loop's end).
#
# Key Steps & Logic:
# 1. For '+', '-', '*', '/': x = stack.pop() is the TOP (most recently
#    pushed) value, y = stack.pop() is the value below it. The result
#    pushed back is x OP y, so '-' computes (top - second) and '/' computes
#    (top / second) -- pop order matters here, unlike for '+' and '*'.
# 2. 'DUP' pushes stack.peek() again without removing anything, duplicating
#    the top value in place.
# 3. 'POP' calls stack.pop() and discards the result, simply removing the
#    top element.
# 4. 'PSH' does NOT parse the current token as its number; it advances i to
#    look at the NEXT token and pushes that one as a float.
# 5. Any other token falls to the try/except: if it parses as a float it's
#    pushed as a bare number, otherwise run() returns
#    "Invalid instruction: {token}" immediately.
# 6. If the stack ends empty, run() returns 0 (a safe default instead of
#    crashing on stack.peek()). Otherwise the top value is returned,
#    coerced to int when it has no fractional part (result.is_integer()).
#
# Worked example -- Enter arguments : PSH 4 PSH 2 / DUP + POP
#   token | action                             | stack after
#   ------+------------------------------------+------------
#   PSH 4 | push 4.0                            | [4.0]
#   PSH 2 | push 2.0                            | [4.0, 2.0]
#     /   | x=pop()=2.0(top), y=pop()=4.0,      | [0.5]
#         | push(x/y)=0.5                       |
#    DUP  | push(peek())=0.5                    | [0.5, 0.5]
#     +   | x=pop()=0.5, y=pop()=0.5, push(1.0) | [1.0]
#    POP  | pop and discard                     | []
#   Stack is empty at the end -> run() returns 0
#   Printed: 0
# ================================================================================