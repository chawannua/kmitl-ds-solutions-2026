# ================================================================================
# Chapter 6 - Item 1: 26s1 Fibonacci recursion
# --------------------------------------------------------------------------------
# Problem Statement:
# *** Do not use while or for loop ***Write Fibonacci program
# The function fibo(n) is defined to return the Fibonacci number for a given n.If n is 1 or 2, the function returns 1 (base cases).For any other n, the function recursively calls itself to compute the sum of fibo(n-1) and fibo(n-2).
# ================================================================================

print(" *** Find fibonacci sequence ***")
n = input("Enter n : ")
n = int(n)

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(f"fibo({n}) = {fibo(n)}")
print("===== End of program =====")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 6 Item 1 (26s1 Fibonacci recursion).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================