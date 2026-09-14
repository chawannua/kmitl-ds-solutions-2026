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
# Greedy digit-by-digit conversion using a table of value/symbol pairs.
#
# Core idea:
#   The subtractive Roman rule (IV, IX, XL, XC, CD, CM) is baked directly into
#   the `values`/`symbols` lists as extra composite entries (900, 400, 90, 40,
#   9, 4) placed between their neighboring "plain" values. This turns the
#   subtractive-pair problem into a single greedy pass with no special-casing.
#
# Key Steps & Logic:
# 1. deciToRoman walks `values`/`symbols` from largest to smallest. For each
#    pair, divmod(num, value) gives `count` (how many times that symbol fits)
#    and the new `num` (remainder). Because 900/400/90/40/9/4 are listed
#    before the plain values below them, a number like 197 never produces
#    "CCCCXCVIIII"; it is forced through XC and VII instead.
# 2. romanToDeci walks the string in reverse (`reversed(roman)`), comparing
#    each `value` to `prev_value` (the value just processed, i.e. the digit
#    to its right). If value < prev_value, that symbol is a subtractive
#    prefix (e.g. the C in "CM") so it is subtracted; otherwise it is added
#    and becomes the new `prev_value`.
# 3. Both functions validate their input first (isinstance/range checks) so
#    non-numeric or empty input raises ValueError instead of silently
#    producing garbage output.
#
# Worked example -- Enter number to translate : 197
#   deciToRoman(197): divmod against [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#     100 -> count 1, num 97   |  90 -> count 1, num 7   |  5 -> count 1, num 2
#     1   -> count 2, num 0
#     Result: "C" + "XC" + "V" + "I" + "I" = "CXCVII"
#   romanToDeci("CXCVII"): reversed = I,I,V,C,X,C
#     I(1)>=0 add ->1 | I(1)>=1 add ->2 | V(5)>=1 add ->7 | C(100)>=5 add ->107
#     X(10)<100 subtract ->97 | C(100)>=100 add ->197
#   Final printed output: CXCVII then 197.
# ================================================================================