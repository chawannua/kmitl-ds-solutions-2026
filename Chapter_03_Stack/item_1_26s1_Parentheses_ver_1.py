# ================================================================================
# Chapter 3 - Item 1: 26s1 Parentheses ver.1
# --------------------------------------------------------------------------------
# Problem Statement:
#     Write a program to receive input in the form of brackets. The opening brackets are: ( and [ and the closing brackets are: ) and ]. 
#     Determine if the brackets can be paired correctly.     Display the number of brackets needed to complete the pairs if they are incomplete.     If all pairs are complete, display "Perfect".
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


def count_unmatched(s):
    matching_open = {')': '(', ']': '['}
    stack = Stack()
    unmatched_closers = 0

    for ch in s:
        if ch in '([':
            stack.push(ch)
        elif ch in ')]':
            if not stack.is_empty() and stack.peek() == matching_open[ch]:
                stack.pop()
            else:
                unmatched_closers += 1

    unmatched_openers = stack.size()
    return unmatched_closers + unmatched_openers


def main():
    s = input("Enter Input : ")
    total = count_unmatched(s)
    print(total)
    if total == 0:
        print("Perfect ! ! !")


if __name__ == "__main__":
    main()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 3 Item 1 (26s1 Parentheses ver.1).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================