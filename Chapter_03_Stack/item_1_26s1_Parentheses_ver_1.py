# ================================================================================
# Chapter 3 - Item 1: 26s1 Parentheses ver.1
# --------------------------------------------------------------------------------
# Problem Statement:
#     Write a program to receive input in the form of brackets. 
#     The opening brackets are: ( and [ and the closing brackets are: ) and ]. 
#     Determine if the brackets can be paired correctly.    
#     Display the number of brackets needed to complete the pairs if they are incomplete.     If all pairs are complete, display "Perfect".
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
# Single-pass bracket balancer that counts how many brackets are missing to
# make the string a fully paired sequence of ( ) and [ ].
#
# Core idea:
#   A closing bracket only pops the stack if it actually matches the type on
#   top (via matching_open). If it does NOT match, it is not popped -- it is
#   simply counted as an unmatched closer and the stack is left untouched.
#   Whatever openers are still sitting on the stack after the scan are the
#   unmatched openers.
#
# Key Steps & Logic:
# 1. count_unmatched(s) walks the string once, character by character.
# 2. An opener '(' or '[' is always pushed -- we don't know yet if it will
#    find a partner later, so it must stay on the stack as a candidate.
# 3. A closer ')' or ']' only pops when stack.peek() equals
#    matching_open[ch]; otherwise unmatched_closers is incremented. This is
#    why a closer that doesn't match the top (e.g. '(' then ']') counts as
#    an error immediately, instead of searching deeper into the stack.
# 4. After the loop, unmatched_openers = stack.size() -- every opener still
#    on the stack never found a matching closer.
# 5. total = unmatched_closers + unmatched_openers is the number of
#    brackets that must be added to complete the pairing; 0 means "Perfect".
#
# Worked example -- Enter Input : ([)
#   char | action                            | stack after
#   -----+-----------------------------------+------------
#    (   | opener -> push                    | (
#    [   | opener -> push                    | (, [
#    )   | closer, peek='[' != '(' -> mismatch, unmatched_closers=1 | (, [
#   End of string: stack still holds 2 openers -> unmatched_openers = 2
#   total = 1 (closer) + 2 (openers) = 3  ->  printed: 3
# ================================================================================