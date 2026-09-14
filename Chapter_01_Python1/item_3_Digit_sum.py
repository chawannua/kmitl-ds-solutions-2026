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
# Treats the number as a string so each character can be summed as a digit,
# avoiding integer overflow/precision issues for numbers up to 30 digits long.
#
# Core idea:
#   num is deliberately kept as a str (never int(num)) because a 30-digit
#   number is still safe to index character-by-character, and str.isdigit()
#   gives a cheap, built-in way to validate every character is 0-9 without
#   writing a manual loop with try/except.
#
# Key Steps & Logic:
# 1. num = input(...) keeps the value as a string, not an int, so both its
#    length and its individual characters can be inspected directly.
# 2. len(num) > 30 enforces the "up to 30 digits" limit, and
#    not num.isdigit() rejects negative signs, decimals, letters, or
#    empty input -- isdigit() returns False for anything that is not a
#    plain sequence of digit characters, which is exactly "invalid".
#    Both checks are combined with "or" because either failure alone
#    should reject the input.
# 3. digit_sum = sum(int(ch) for ch in num) walks every character ch in the
#    string, converts each single character back to int, and sums them --
#    this is the actual digit-by-digit summation the problem asks for.
# 4. The result is printed with a trailing "= " matching the exact wording
#    used in the examples ("1+2+3=6" style, but as a labeled statement).
#
# Worked example -- Enter a positive number : 32189657
#   digits: 3+2+1+8+9+6+5+7 = 41
#   Printed output: "Summation of each digit =  41"
# ================================================================================