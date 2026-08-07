# ================================================================================
# Chapter 6 - Item 5: 26s1 Draw stair
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program that displays output as shown in the example.
# Restrictions:
# Do not use for, while commands.Note:
# The function can have no more than 2 parameters.
# def staircase(n):    #code here
# print(" *** Stair case ***")
# print(staircase(int(input("Enter Input : "))))
# print("===== End of program =====")
# ================================================================================

def staircase(n, i=1):
    if n == 0:
        return "Not Draw!"
    
    if n > 0:
        if i > n:
            return ""
        line = "_" * (n - i) + "#" * i
        rest = staircase(n, i + 1)
        return line if rest == "" else line + "\n" + rest
        
    else:  # n < 0
        if i > abs(n):
            return ""
        line = "_" * (i - 1) + "#" * (abs(n) - i + 1)
        rest = staircase(n, i + 1)
        return line if rest == "" else line + "\n" + rest

if __name__ == "__main__":
    print(" *** Stair case ***")
    print(staircase(int(input("Enter Input : "))))
    print("===== End of program =====")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 6 Item 5 (26s1 Draw stair).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================