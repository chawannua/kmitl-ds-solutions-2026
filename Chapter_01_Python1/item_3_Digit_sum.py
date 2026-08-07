# ================================================================================
# Chapter 1 - Item 3: Digit sum
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program to accept an integer number up to 30 digits and then find the sum of each digit.
# Example:
#     - Input number 123 => 1+2+3=6
#     - Input number 7892 => 7+8+9+2=26
#     - Input number 32189657 => 3+2+1+8+9+6+5+7=41
# ================================================================================

print(" *** Summation of each digit ***")

num = input("Enter a positive number : ")

if len(num) > 30 or not num.isdigit():
    print("Enter a positive number : ")
else:
    digit_sum = sum(int(ch) for ch in num)
    print("Summation of each digit = ", digit_sum)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 1 Item 3 (Digit sum).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================