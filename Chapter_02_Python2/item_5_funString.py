# ================================================================================
# Chapter 2 - Item 5: funString
# --------------------------------------------------------------------------------
# Problem Statement:
# Create a class funString that will accept a string and a command number as parameters, with the following functions:
# Find the length of the string.Toggle case in the string (do not use the upper and lower commands).Reverse the string (do not use the reversed command).Delete characters that appear earlier in the string."
# class funString():
#     def __init__(self,string = ""):
#         ### Enter Your Code Here ###
#     def __str__(self):
#         ### Enter Your Code Here ###
#     def size(self) :
#         ### Enter Your Code Here ###
#     def changeSize(self):
#         ### Enter Your Code Here ###
#     def reverse(self):
#         ### Enter Your Code Here ###
#     def deleteSame(self):
#        ### Enter Your Code Here ###
# str1, str2 = input("Enter String and Number of Function : ").split()
# res = funString(str1)
# if str2 == "1" :    print(res.size())elif str2 == "2":  print(res.changeSize())elif str2 == "3" : print(res.reverse())elif str2 == "4" : print(res.deleteSame())
# ================================================================================

class funString():

    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self):
        count = 0
        for _ in self.string:
            count += 1
        return count

    def changeSize(self):
        res = ""
        for c in self.string:
            val = ord(c)
            if 65 <= val <= 90:
                res += chr(val + 32)
            elif 97 <= val <= 122:
                res += chr(val - 32)
            else:
                res += c
        return res

    def reverse(self):
        res = ""
        for i in range(self.size() - 1, -1, -1):
            res += self.string[i]
        return res

    def deleteSame(self):
        res = ""
        for c in self.string:
            is_duplicate = False
            for seen_char in res:
                if c == seen_char:
                    is_duplicate = True
                    break
            if not is_duplicate:
                res += c
        return res


str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1":
    print(res.size())
elif str2 == "2":
    print(res.changeSize())
elif str2 == "3":
    print(res.reverse())
elif str2 == "4":
    print(res.deleteSame())

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Hand-rolled reimplementations of built-in string operations, since the
# problem statement forbids using upper()/lower()/reversed() directly.
#
# Core idea:
#   Every operation is done through manual character-code arithmetic or
#   index/loop scanning instead of calling the built-in that normally does
#   the job, then str2 (a command number "1"-"4") dispatches to one method.
#
# Key Steps & Logic:
# 1. size() counts characters with a manual `count += 1` loop instead of
#    len(), so it still works even if len() were unavailable.
# 2. changeSize() toggles case using ord()/chr() arithmetic on ASCII ranges:
#    65-90 is 'A'-'Z' (add 32 to lowercase it), 97-122 is 'a'-'z' (subtract
#    32 to uppercase it); anything outside those ranges (spaces, digits) is
#    copied unchanged. This avoids calling .upper()/.lower().
# 3. reverse() walks `range(self.size() - 1, -1, -1)` -- from the last index
#    down to 0 -- and appends self.string[i] each time, building the
#    reversed string without slicing ([::-1]) or reversed().
# 4. deleteSame() keeps only the FIRST occurrence of each character: for
#    every c, it linearly scans `res` (the output built SO FAR, not the
#    original string) with `is_duplicate`; if c is already in res it is
#    dropped, otherwise appended. This is O(n^2) but needs no set/dict.
#
# Worked example -- Enter String and Number of Function : programming <cmd>
#   cmd=1 size()       -> 11
#   cmd=2 changeSize()  -> "PROGRAMMING"
#   cmd=3 reverse()     -> "gnimmargorp"
#   cmd=4 deleteSame()  -> "progamin"  (repeated r, g, m, i are dropped
#                          after their first appearance)
# ================================================================================