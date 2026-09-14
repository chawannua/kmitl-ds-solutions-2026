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
# A single list-comprehension filter isolates odd numbers by their
# remainder when divided by 2.
#
# Core idea:
#   odd_list(alist) is a pure filter function: it never mutates alist, it
#   just builds and returns a brand-new list, so the caller can still print
#   the original ls afterward and see it unchanged.
#
# Key Steps & Logic:
# 1. def odd_list(alist): [x for x in alist if x % 2 != 0] iterates every
#    element x and keeps it only when x % 2 != 0 -- the remainder of
#    integer division by 2 is 1 for odd numbers and 0 for even ones, so
#    "!= 0" is the direct test for "is odd".
# 2. ls = [int(e) for e in input(...).split()] reads a space-separated line
#    and converts every token e to int, building the input list to test.
# 3. opls = odd_list(ls) calls the function once; the result is stored
#    separately from ls rather than overwriting it, so both the original
#    input list and the filtered output list can be printed afterward.
# 4. The two print() calls show "Input list" and "Output list" side by
#    side so the transformation is visible to whoever runs the program.
#
# Worked example -- Enter list numbers : 10 11 13 24 25
#   ls   = [10, 11, 13, 24, 25]
#   test : 10%2=0(even) 11%2=1(odd) 13%2=1(odd) 24%2=0(even) 25%2=1(odd)
#   opls = [11, 13, 25]
# ================================================================================