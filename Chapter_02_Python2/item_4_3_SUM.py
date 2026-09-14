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
# Sort-then-two-pointer 3-SUM in O(n^2), instead of the brute-force O(n^3)
# triple loop.
#
# Core idea:
#   Once nums is sorted, fixing nums[i] as the smallest of the triplet turns
#   "find two numbers that sum to -nums[i]" into a classic two-pointer scan:
#   left starts just after i, right starts at the end, and they converge
#   based on whether the current sum is too small or too large.
#
# Key Steps & Logic:
# 1. nums.sort() is required for two things: it lets left/right move in a
#    single monotonic direction, and it groups equal values together so
#    duplicates can be skipped by just comparing to a NEIGHBOR.
# 2. tol = 1e-9 replaces every `== 0` / `==` comparison because the problem
#    allows real (float) numbers, and float arithmetic can miss exact zero
#    by a tiny epsilon (abs(s) <= tol, abs(diff) < tol).
# 3. `if i > 0 and abs(nums[i] - nums[i - 1]) < tol: continue` skips a
#    duplicate CHOICE of the first element so the same triplet value isn't
#    used as the anchor twice.
# 4. Inside the while left < right loop: s < -tol means the sum is too small
#    so left += 1 (grab a bigger number); s > tol means too large so
#    right -= 1; abs(s) <= tol is a match, and after recording it BOTH
#    pointers move inward with their own duplicate-skipping while-loops so
#    the same pair of values isn't recorded twice for this i.
# 5. _print_case is an unused batch-test helper for trying several arrays at
#    once; the __main__ block instead reads exactly one line and calls
#    three_sum(nums) directly.
#
# Worked example -- Enter Your List : -1 0 1 2 -1 -4
#   sorted nums = [-4, -1, -1, 0, 1, 2]
#   i=0 (-4): left/right scan finds no zero sum, left advances to 5, done.
#   i=1 (-1): left=2,right=5 -> -1-1+2=0 -> record [-1,-1,2]; then
#             left=3,right=4 -> -1+0+1=0 -> record [-1,0,1].
#   i=2 (-1): duplicate of nums[1] -> skipped by the tol check.
#   i=3 (0):  left=4,right=5 -> 0+1+2=3 (>tol) -> right shrinks, loop ends.
#   Printed output: [[-1, -1, 2], [-1, 0, 1]]
# ================================================================================