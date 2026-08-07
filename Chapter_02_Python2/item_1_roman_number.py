# ================================================================================
# Chapter 2 - Item 1: roman number
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a function to convert decimal number to Roman
# M=1000    CM=900    D=500    CD=400,
# C=100    XC=90    L=50    XL=40, 
# X=10    IX=9    V=5    IV=4    I=1
# For example 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I
# (https://roman-numerals.info/)
# class translator:
#     def deciToRoman(self, num):
#         ### Enter Your Code Here ###        pass
#     def romanToDeci(self, s):
#         ### Enter Your Code Here ###        pass
# print(" *** Decimal to Roman ***")num = int(input("Enter number to translate : "))
# print(translator().deciToRoman(num))
# print(translator().romanToDeci(translator().deciToRoman(num)))
# ================================================================================

class translator:
    def deciToRoman(self, num):
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Number must be a positive integer")

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []
        for value, symbol in zip(values, symbols):
            count, num = divmod(num, value)
            result.append(symbol * count)

        return "".join(result)

    def romanToDeci(self, s):
        if not isinstance(s, str) or not s:
            raise ValueError("Roman numeral must be a non-empty string")

        roman = s.upper().strip()
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        prev_value = 0
        for ch in reversed(roman):
            value = values[ch]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value

        return total


if __name__ == "__main__":
    print(" *** Decimal to Roman ***")
    num = int(input("Enter number to translate : "))

    translator_obj = translator()
    roman = translator_obj.deciToRoman(num)
    print(roman)
    print(translator_obj.romanToDeci(roman))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 2 Item 1 (roman number).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================