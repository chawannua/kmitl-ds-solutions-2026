# ================================================================================
# Chapter 10 - Item 1: Binary Search
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Binary Search using recursion to determine whether a value exists in
# the list or not. If the value is found, return True; if not, return False.
#
# Inputs:
# - "<list of integers>/<value to find>", e.g. 33 2 11 82 77 28 15 76 9 64/28
# Outputs:
# - True if the value is in the list, otherwise False.
# ================================================================================

def bi_search(l, r, arr, x):
    # Empty range: the value is not in the list
    if l > r:
        return False
    mid = (l + r) // 2
    if arr[mid] == x:
        return True
    # Target is smaller -> search the left half, otherwise the right half
    elif arr[mid] > x:
        return bi_search(l, mid - 1, arr, x)
    else:
        return bi_search(mid + 1, r, arr, x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# 1. The list is sorted first (given code), so binary search is valid.
# 2. bi_search looks at the middle index of the range [l, r]:
#    - equal to x      -> found, return True
#    - greater than x  -> recurse on [l, mid - 1]
#    - less than x     -> recurse on [mid + 1, r]
# 3. When l > r the range is empty, so x is not present -> return False.
#
# Worked example -- Enter Input : 33 2 11 82 77 28 15 76 9 64/28
#   sorted = [2, 9, 11, 15, 28, 33, 64, 76, 77, 82]
#   [0,9] mid=4 -> 28 == 28 -> True
# ================================================================================
