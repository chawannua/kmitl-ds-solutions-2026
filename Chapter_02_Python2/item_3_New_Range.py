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
# A float-capable reimplementation of range() that preserves the input's own
# decimal precision instead of trusting Python's raw float representation.
#
# Core idea:
#   RANGE receives the RAW STRINGS typed by the user (args are never
#   pre-converted to float before the call), so decimals(s) can count digits
#   after '.' in the original text. precision = max(decimals(start_str),
#   decimals(step_str)) tells format_value exactly how many decimal places
#   the output must show, avoiding float noise like "0.30000000000000004".
#
# Key Steps & Logic:
# 1. len(args) selects which of start_str/stop_str/step_str get real values,
#    mirroring range(a) / range(a, b) / range(a, b, c) overload semantics.
# 2. The while loop computes value = start + index*step and rounds it to
#    precision + 5 BEFORE comparing to stop -- the extra 5 digits absorb
#    binary float rounding error so a boundary case doesn't wrongly
#    include/exclude a value due to noise past the visible precision.
# 3. The stop test branches on the sign of step (step > 0 stops at
#    value >= stop, step < 0 stops at value <= stop), which is what lets a
#    single function support both ascending and descending sequences.
# 4. format_value formats to `precision` decimals then strips trailing zeros
#    and a trailing '.', re-adding ".0" only if precision > 0 -- this is why
#    whole numbers in a float range still print as "1.0" not "1".
#
# Worked example -- Enter Input : 1 5 2   (3-argument form: start=1, end=5, step=2)
#   start_str="1", step_str="2" -> precision = max(0, 0) = 0
#   index 0: value = 1 + 0*2 = 1  (1 < 5)  -> "1"
#   index 1: value = 1 + 1*2 = 3  (3 < 5)  -> "3"
#   index 2: value = 1 + 2*2 = 5  (5 >= 5) -> loop stops
#   Printed output: (1, 3)
# ================================================================================