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
# Two separate recursions: get_len() counts characters, length() prints them.
#
# Core idea:
#   Neither function may use len()/for/while, and length() may take only ONE
#   parameter, so there is no explicit counter for "which index am I on".
#   get_len() is reused inside length() as a ruler to rebuild that index.
#
# Key Steps & Logic:
# 1. get_len(text): base case text == "" returns 0. Recursive case returns
#    get_len(text[1:]) + 1 -- slicing off the first character each call shrinks
#    the string by one, so it must reach "" and stop.
# 2. total_str_len = get_len(txt) is computed ONCE up front (module level), so
#    length() can refer to it without needing it as a second parameter.
# 3. length(text): base case text == "" returns 0 (same shrink-by-one pattern,
#    so it terminates for the same reason as get_len()).
# 4. current_index = total_str_len - get_len(text) + 1: since get_len(text)
#    shrinks by 1 each call, current_index rises by 1 each call -- this rebuilds
#    a 1-based position counter using only the two lengths, with no extra param.
# 5. current_index % 2 picks '*' (odd position) or '~' (even position); the
#    character is printed BEFORE recursing into length(text[1:]), so characters
#    appear on screen in original left-to-right order as the stack grows deeper.
# 6. Each call returns length(text[1:]) + 1, so the +1's add up while the stack
#    unwinds, giving the same total length get_len() would compute.
#
# Worked example -- Enter Input : AB  (total_str_len = 2)
#   length("AB")
#   +- current_index = 2 - get_len("AB")=2 + 1 = 1  -> odd  -> print "A*"
#   +- length("B")
#      +- current_index = 2 - get_len("B")=1 + 1 = 2 -> even -> print "B~"
#      +- length("")  -> 0                (base case)
#      => returns 0 + 1 = 1
#   => returns 1 + 1 = 2
#   Printed: A*B~   Final: length of 'AB' is 2
# ================================================================================