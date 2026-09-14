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
# A stateful object wrapping the sphere volume/area formulas, using a dunder
# method so `print(R1)` shows a live, recomputed summary.
#
# Core idea:
#   self.radius is the ONLY stored state. findVolume/findArea never cache a
#   result -- they recompute (4/3)*PI*r**3 and 4*PI*r**2 from self.radius on
#   every call, so calling changeR() and then printing again automatically
#   reflects the new radius with no extra bookkeeping.
#
# Key Steps & Logic:
# 1. __init__ just stores r in self.radius; changeR(Radius) overwrites it.
# 2. findVolume/findArea read self.radius directly, using the module-level
#    PI = 3.141592653589793 (more precise than the header's 3.1415926) so
#    both formulas share one constant.
# 3. __str__ is defined so `print(R1)` doesn't show a memory address; Python
#    calls it implicitly and it in turn calls findVolume()/findArea() to
#    build the string, which is why radius changes show up automatically.
# 4. r1, r2 = input(...).split() reads two numbers in one line: r1 builds the
#    initial sphere, r2 is only used later as the argument to changeR().
#
# Worked example -- Enter R : 3 5
#   R1 = Spherical(3)              -> print(type(R1)) : <class '__main__.Spherical'>
#   print(R1) uses r=3: Volume=(4/3)*PI*27=113.09733552923254
#                        Area  =4*PI*9   =113.09733552923255  (equal at r=3)
#   R1.changeR(5) sets self.radius = 5
#   print(R1) uses r=5: Volume=(4/3)*PI*125=523.5987755982989
#                        Area  =4*PI*25   =314.1592653589793
# ================================================================================