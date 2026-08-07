# ================================================================================
# Chapter 6 - Item 2: 26s1 Length of a String EXTRA
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a function that works like the len() function to find the length of a string and display the result as shown in the example (printing each character alternated with special symbols in odd and even positions).
# Restrictions:
# Do not use len, for, while, do while, or split commands.The function must have only one parameter.Note:
# The function should only have one parameter.
# def length(txt):         #Code Hereprint("\n",length(input("Enter Input : ")),sep="")#print(you can modify this line)
# ================================================================================

print(" *** Length of string (Recursion) ***")

txt = input("Enter Input : ")

def get_len(text):
    if text == "":
        return 0
    return get_len(text[1:]) + 1

total_str_len = get_len(txt)

def length(text):     
    if text == "":   
        return 0
    
    current_index = total_str_len - get_len(text) + 1
    
    if current_index % 2 != 0:
        print(text[0] + "*", end="")
    else:
        print(text[0] + "~", end="")
        
    return length(text[1:]) + 1

total_len = length(txt)
print()
print(f"length of '{txt}' is {total_len}")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 6 Item 2 (26s1 Length of a String EXTRA).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================