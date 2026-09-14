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
# Euclidean algorithm implemented as direct recursion on the remainder.
#
# Core idea:
#   gcd(a, b) == gcd(b, a % b) for any a, b (with b != 0): the pair (b, a % b)
#   has the exact same set of common divisors as (a, b), so recursing on it
#   never changes the answer while shrinking the numbers involved.
#
# Key Steps & Logic:
# 1. Base case: b == 0 returns abs(a) -- once the second number reaches 0, a
#    itself IS the greatest common divisor (dividing by 0 is undefined, so this
#    is also where the recursion MUST stop).
# 2. Recursive case: return gcd(b, a % b). The second argument becomes a % b,
#    which by definition of modulo satisfies 0 <= a % b < b -- it is strictly
#    smaller than the previous second argument (b). Since it is a non-negative
#    integer that strictly decreases every call, it is guaranteed to hit 0.
# 3. Before calling gcd(), main swaps a and b if a < b, but this only saves a
#    step -- gcd() itself works in either order since a % b handles it.
#
# Worked example -- Enter Input : 48 18
#   gcd(48, 18)
#   +- gcd(18, 48 % 18 = 12)
#      +- gcd(12, 18 % 12 = 6)
#         +- gcd(6, 12 % 6 = 0)
#            +- b == 0 -> base case, return abs(6) = 6
#         => 6
#      => 6
#   => 6
#   Output: The gcd of 48 and 18 is : 6
# ================================================================================