# ================================================================================
# Chapter 10 - Item 2: First Greater Value
# --------------------------------------------------------------------------------
# Problem Statement:
# Find the smallest value (in the left list) that is greater than each target
# value (in the right list). If no such value exists, display
# "No First Greater Value". Numbers do not exceed 1,000,000.
#
# Inputs:
# - "<left list>/<right list of targets>", e.g. 3 2 7 6 8/5 6 12
# Outputs:
# - One line per target: the first greater value, or "No First Greater Value".
# ================================================================================

def find_first_greater(arr, target):
    l, r = 0, len(arr) - 1
    ans = None
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > target:
            # Candidate answer; keep looking left for a smaller one
            ans = arr[mid]
            r = mid - 1
        else:
            l = mid + 1
    return ans if ans is not None else "No First Greater Value"

inp = input('Enter Input : ').split('/')
left = sorted(list(map(int, inp[0].split())))
right = list(map(int, inp[1].split()))

for target in right:
    print(find_first_greater(left, target))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# 1. Sort the left list once.
# 2. For each target, binary search for the leftmost value > target
#    (an "upper bound" search): every time arr[mid] > target, remember it and
#    move right boundary left; otherwise move left boundary right.
# 3. If nothing was remembered, print "No First Greater Value".
#
# Worked example -- Enter Input : 3 2 7 6 8/5 6 12
#   sorted left = [2, 3, 6, 7, 8]
#   5  -> 6
#   6  -> 7
#   12 -> No First Greater Value
# ================================================================================
