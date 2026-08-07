# ================================================================================
# Chapter 2 - Item 4: 3 SUM
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a function to find the sum of any three terms in an array that equal zero, for an array containing real numbers. The array must have a length of at least three elements."
# ================================================================================

def three_sum(nums):
    n = len(nums)
    if n < 3:
        raise ValueError("Array Input Length Must More Than 2")
    nums.sort()
    res = []
    tol = 1e-9

    for i in range(n - 2):
        if i > 0 and abs(nums[i] - nums[i - 1]) < tol:
            continue

        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if abs(s) <= tol:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and abs(nums[left] - nums[left - 1]) < tol:
                    left += 1
                while left < right and abs(nums[right] - nums[right + 1]) < tol:
                    right -= 1
            elif s < -tol:
                left += 1
            else:
                right -= 1

    return res


def _print_case(title, nums):
    print(f"{title}")
    try:
        out = three_sum(nums)
        print(out)
    except ValueError as exc:
        print(str(exc))
    print()


if __name__ == "__main__":
    arr = input("Enter Your List : ").split()
    nums = [int(x) for x in arr]
    try:
        out = three_sum(nums)
        print(out)
    except ValueError as exc:
        print(str(exc))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 2 Item 4 (3 SUM).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================