# ================================================================================
# Chapter 1 - Item 2: multiplication or sum
# --------------------------------------------------------------------------------
# Problem Statement:
# รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง
# ================================================================================

print("*** multiplication or sum ***")

num1, num2 = input("Enter num1 num2 : ").split()

num1 = int(num1)
num2 = int(num2)

if num1 * num2 <= 1000:
    print("The result is", num1 * num2)
else:
    print("The result is", num1 + num2)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 1 Item 2 (multiplication or sum).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================