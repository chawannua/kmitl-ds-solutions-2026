# ================================================================================
# Chapter 1 - Item 4: function
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a function:  odd_list(alist):
# The function should work as follows:
# # Returns a list that contains only the odd numbers from alist
# # For example, if alist = [10, 11, 13, 24, 25], the result should be [11, 13, 25]
# Please modify from the following part of the code:"
# def odd_list(al):    # put your code here
# print(" ***Function Odd List***")ls = [int(e) for e in input("Enter list numbers : ").split()]print(ls)opls = odd_list(ls)print("Input list : ", ls, "\nOutput list : ", opls)
# ================================================================================

def odd_list(alist):
    """Return a new list containing only the odd numbers from alist."""
    return [x for x in alist if x % 2 != 0]

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
print("Input list : ", ls)
opls = odd_list(ls)
print("Output list : ", opls)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 1 Item 4 (function).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================