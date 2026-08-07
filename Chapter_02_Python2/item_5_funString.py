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
# This Python script solves Chapter 2 Item 5 (funString).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================