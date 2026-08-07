# ================================================================================
# Chapter 2 - Item 2: Spherical
# --------------------------------------------------------------------------------
# Problem Statement:
# Create class Spherical that must have function [changeR , findVolume , findArea] and radius variable
# class Spherical:    def __init__(self,r):        ### Enter Your Code Here ###    def changeR(self,Radius):        ### Enter Your Code Here ###    def findVolume(self):        ### Enter Your Code Here ###    def findArea(self):        ### Enter Your Code Here ###    def __str__(self):        return "Radius =" + str(self.radius) + " Volumn = " + str(self.findVolume()) + " Area = " + str(self.findArea())
# print(" *** Spherical ***")r1, r2 = input("Enter R : ").split()PI = 3.1415926R1 = Spherical(int(r1))print(type(R1))print(R1)
# R1.changeR(int(r2))print(R1)
# ================================================================================

PI = 3.141592653589793


class Spherical:
    def __init__(self, r):
        self.radius = r

    def changeR(self, Radius):
        self.radius = Radius

    def findVolume(self):
        return (4 / 3) * PI * self.radius ** 3

    def findArea(self):
        return 4 * PI * self.radius ** 2

    def __str__(self):
        return "Radius =" + str(self.radius) + " Volumn = " + str(self.findVolume()) + " Area = " + str(self.findArea())


r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(R1)
R1.changeR(int(r2))
print(R1)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 2 Item 2 (Spherical).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================