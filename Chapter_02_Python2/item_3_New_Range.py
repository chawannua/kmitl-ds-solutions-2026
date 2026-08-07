# ================================================================================
# Chapter 2 - Item 3: New Range
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a python program  to creaet a new range() function using just one function
# - if there is 1 argument -> range(a)                | start = 0 , end = a , step = 1
# - if there are 2 argument -> range(a, b)            | start = a , end = b , step = 1
# - if there are 3 argument -> range(a, b, c)        | start = a , end = b , step = c
# def RANGE(*args):    pass
# print('*** New Range ***')n = [float(i) for i in input('Enter Input : ').split()]if len(n) == 1:    k = RANGE(n[0])    print(RANGE(n[0]))elif len(n) == 2:    print(RANGE(n[0], n[1]))elif len(n) == 3:    print(RANGE(n[0], n[1], n[2]))
# ================================================================================

def RANGE(*args):
    def decimals(s):
        return len(s.split('.')[-1]) if '.' in s else 0

    if len(args) == 1:
        start_str, stop_str, step_str = '0.0', str(args[0]), '1.0'
    elif len(args) == 2:
        start_str, stop_str, step_str = str(args[0]), str(args[1]), '1.0'
    elif len(args) == 3:
        start_str, stop_str, step_str = str(args[0]), str(args[1]), str(args[2])
    else:
        raise TypeError("RANGE expects 1 to 3 arguments")

    start = float(start_str)
    stop = float(stop_str)
    step = float(step_str)
    precision = max(decimals(start_str), decimals(step_str))

    def format_value(v):
        text = format(v, f'.{precision}f').rstrip('0').rstrip('.')
        if '.' not in text and precision > 0:
            text += '.0'
        return text

    values = []
    index = 0
    while True:
        value = round(start + index * step, precision + 5)
        if step > 0 and value >= stop:
            break
        if step < 0 and value <= stop:
            break
        values.append(format_value(value))
        index += 1

    return f"({', '.join(values)})"


print('*** New Range ***')
args = input('Enter Input : ').split()
if len(args) == 1:
    print(RANGE(args[0]))
elif len(args) == 2:
    print(RANGE(args[0], args[1]))
elif len(args) == 3:
    print(RANGE(args[0], args[1], args[2]))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 2 Item 3 (New Range).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================