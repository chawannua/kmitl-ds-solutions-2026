# ================================================================================
# Chapter 9 - Item 2: 26s1 Ascending sort
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Python program that accepts input and sort the input in ascending order
# of positive integers and zero. If there are negative integers, do not process
# them.
# Do not use built-in sorting functions. Write your own sort function instead.
# ================================================================================



def insertionSort(arr):
    """Own sort - no built-in sort() / sorted() used."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:      # shift the bigger ones right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = [int(x) for x in input("Enter Input : ").split()]

slots = []                                  # where the non-negative values sit
positives = []
for i, x in enumerate(arr):
    if x >= 0:
        slots.append(i)
        positives.append(x)

insertionSort(positives)

for i, value in zip(slots, positives):      # put them back, negatives untouched
    arr[i] = value

print(' '.join(str(x) for x in arr))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Sort a subsequence in place while the excluded elements never move.
#
# Core idea:
#   The negatives act as fixed walls. Collect the indices that hold non-negative
#   values, sort ONLY those values, then write them back into those same indices
#   in order. Every negative keeps the exact position it started in.
#
# Key Steps & Logic:
# 1. One pass with enumerate() builds two parallel lists: `slots` (the positions
#    of every value >= 0) and `positives` (the values themselves). Zero counts as
#    non-negative and is therefore sorted, per the problem statement.
# 2. insertionSort() orders `positives` ascending. It is a hand-written sort --
#    it walks left to right, lifts each element out as `key`, shifts every
#    larger element one cell right, and drops `key` into the gap. No sort(),
#    sorted(), min() or max() is used anywhere.
# 3. zip(slots, positives) pairs the k-th smallest value with the k-th
#    non-negative position, so writing them back restores ascending order in
#    exactly the cells that are allowed to change.
#
# Worked example -- Enter Input : 6 3 -2 5 -8 2 -2
#   index:      0   1   2   3   4   5   6
#   value:      6   3  -2   5  -8   2  -2
#   slots     = [0, 1, 3, 5]          (positions of 6, 3, 5, 2)
#   positives = [6, 3, 5, 2] -> insertionSort -> [2, 3, 5, 6]
#   write back: idx0=2, idx1=3, idx3=5, idx5=6
#   Output: 2 3 -2 5 -8 6 -2      (the -2, -8, -2 never moved)
# ================================================================================
