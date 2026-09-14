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
# Stack-based bracket validator that pinpoints WHICH of three error types
# broke the expression, using early-exit checks during the scan.
#
# Core idea:
#   A closing bracket can only fail in two ways DURING the scan (nothing on
#   the stack to match, or the wrong opener on top); a leftover opener can
#   only be detected once the whole string has been read, since you can't
#   know it's "extra" until nothing ever closes it.
#
# Key Steps & Logic:
# 1. check_expression(s) pushes every opener '(', '[', '{' onto the stack.
# 2. On a closer, if stack.is_empty() the function returns immediately with
#    "close paren excess" -- nothing on the stack could ever match this
#    closer, so no more scanning is needed.
# 3. Otherwise it pops the top and compares it via pairs[ch]. A mismatch
#    (e.g. top='(' but ch==']') returns "Unmatch open-close" right away --
#    unlike item_1, this stops the scan instead of just counting the error.
# 4. If the loop finishes with the stack non-empty, those are openers that
#    were never closed -- only knowable after the last character, so this
#    check sits outside the for-loop and returns "open paren excess" plus
#    the count and the leftover characters (stack.to_string()).
# 5. An empty stack at the end means every opener found its closer -> MATCH.
#
# Worked example -- Enter expresion : (a+b]
#   char  | action                          | stack after
#   ------+---------------------------------+------------
#    (    | opener -> push                  | (
#   a,+,b | not a bracket -> ignored        | (
#    ]    | closer, pop top='(' , pairs[']']='[' != '(' -> fail
#   Result: "Unmatch open-close", returned the instant the mismatch is seen.
#   Printed: (a+b] Unmatch open-close
# ================================================================================