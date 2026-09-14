# ================================================================================
# Chapter 6 - Item 5: 26s1 Draw stair
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program that displays output as shown in the example.
# Restrictions:
# Do not use for, while commands.Note:
# The function can have no more than 2 parameters.
# def staircase(n):    #code here
# print(" *** Stair case ***")
# print(staircase(int(input("Enter Input : "))))
# print("===== End of program =====")
# ================================================================================

def staircase(n, i=1):
    if n == 0:
        return "Not Draw!"
    
    if n > 0:
        if i > n:
            return ""
        line = "_" * (n - i) + "#" * i
        rest = staircase(n, i + 1)
        return line if rest == "" else line + "\n" + rest
        
    else:  # n < 0
        if i > abs(n):
            return ""
        line = "_" * (i - 1) + "#" * (abs(n) - i + 1)
        rest = staircase(n, i + 1)
        return line if rest == "" else line + "\n" + rest

if __name__ == "__main__":
    print(" *** Stair case ***")
    print(staircase(int(input("Enter Input : "))))
    print("===== End of program =====")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Recursion builds the staircase string one row at a time via an index counter.
#
# Core idea:
#   staircase(n, i=1) may take only 2 parameters, so the DEFAULT argument i is
#   reused as the "current row number", counting 1..n across recursive calls
#   instead of a loop variable.
#
# Key Steps & Logic:
# 1. Base case n == 0: returns "Not Draw!" immediately -- no recursion at all.
# 2. Base case i > n (for n > 0) or i > abs(n) (for n < 0): once the row
#    counter has passed the last row, return "" to stop generating more rows.
# 3. Recursive case: build this row's text (line), then call
#    staircase(n, i + 1) to build the remaining rows (rest). Because i grows
#    by exactly 1 and is bounded above by n (or abs(n)), it must eventually
#    exceed that bound and hit the base case, so recursion always terminates.
# 4. return line if rest == "" else line + "\n" + rest: the CURRENT row's line
#    is placed BEFORE rest, i.e. row i (built at THIS depth) sits ahead of rows
#    i+1..n (built at DEEPER calls that return later). So even though the
#    deepest call (i == n) finishes first, string concatenation keeps the
#    staircase printed top row first -- matching call order, not return order.
# 5. For n > 0 each row is "_"*(n-i) + "#"*i (triangle growing downward). For
#    n < 0 the roles flip: "_"*(i-1) + "#"*(abs(n)-i+1) (triangle shrinking
#    downward) -- same recursion shape, mirrored formula.
#
# Worked example -- Enter Input : 3
#   staircase(3, i=1)  line="__#"
#   +- staircase(3, i=2)  line="_##"
#      +- staircase(3, i=3)  line="###"
#         +- staircase(3, i=4) -> i > n, base case, returns ""
#         => "###" (rest == "", so just line)
#      => "_##" + "\n" + "###"
#   => "__#" + "\n" + "_##\n###"  =  "__#\n_##\n###"
#   Printed:
#     __#
#     _##
#     ###
# ================================================================================