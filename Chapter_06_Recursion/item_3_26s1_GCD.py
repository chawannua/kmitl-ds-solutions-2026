# ================================================================================
# Chapter 6 - Item 3: 26s1 GCD
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program to find the GCD (Greatest Common Divisor) of two numbers.
# Restrictions:
# Do not use len, for, while commands.Note:
# The function must have only two parameters.Definition:
# The Greatest Common Divisor (GCD) of two integers, neither of which is zero, is the largest integer that divides both numbers without leaving a remainder.
# ================================================================================

def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)


num1 , num2 = input("Enter Input : ").split(" ")

a, b = int(num1), int(num2)


if a < b:
    a, b = b, a
    
if a == 0 and b == 0:
    print("Error! must be not all zero.")
else:
    result = gcd(a, b)
    print(f"The gcd of {a} and {b} is : {result}")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 6 Item 3 (26s1 GCD).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================