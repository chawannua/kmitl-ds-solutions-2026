# ================================================================================
# Chapter 9 - Item 5: 26s1 Quick sort
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Python program that accepts a sequence of integers.
# Use the Quick Sort algorithm to sort them using three different pivot selection
# strategies:
# - First element
# - Last element
# - Middle element
# Output the number of comparisons, as shown in the examples.
# ================================================================================


comparisons = 0


def partition(arr, low, high, strategy):
    global comparisons

    if strategy == 'first':
        pivotIndex = low
    elif strategy == 'last':
        pivotIndex = high
    else:
        pivotIndex = (low + high) // 2

    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]    # park pivot at low
    pivot = arr[low]
    i = low

    for j in range(low + 1, high + 1):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]                      # pivot to its place
    return i


def quickSort(arr, low, high, strategy):
    if low < high:
        p = partition(arr, low, high, strategy)
        quickSort(arr, low, p - 1, strategy)
        quickSort(arr, p + 1, high, strategy)


def countComparisons(data, strategy):
    global comparisons
    comparisons = 0
    quickSort(data[:], 0, len(data) - 1, strategy)           # sort a copy
    return comparisons


print(' *** Quick sort ***')
data = [int(x) for x in input('Enter a sequence of integers : ').split()]
print()
print('Number of comparisons for each pivot strategy:')
print(f'First Pivot: {countComparisons(data, "first")} comparisons')
print(f'Last Pivot: {countComparisons(data, "last")} comparisons')
print(f'Middle Pivot: {countComparisons(data, "middle")} comparisons')
print('===== End of program =====')

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# One quicksort, run three times, counting element-vs-pivot comparisons.
#
# Core idea:
#   Quicksort's cost is dominated by how evenly the pivot splits the array. The
#   point of this exercise is that the SAME data gives three different totals
#   depending only on which element is chosen as pivot -- a balanced split costs
#   O(n log n), a degenerate one O(n^2).
#
# Key Steps & Logic:
# 1. partition() picks the pivot index from the strategy, then immediately swaps
#    that element to `low`. Parking the pivot at a fixed end means the scanning
#    loop below is identical for all three strategies -- only the chosen index
#    differs. Middle uses (low + high) // 2, the lower middle on even spans.
# 2. The scan runs j over low+1..high and counts EXACTLY ONE comparison per
#    element examined, so a partition of m elements costs m - 1 comparisons.
#    `i` tracks the boundary of the "< pivot" region; every element smaller than
#    the pivot is swapped up behind that boundary.
# 3. After the scan, swapping arr[low] with arr[i] drops the pivot into its
#    final sorted position, and partition returns that index.
# 4. quickSort() recurses on low..p-1 and p+1..high. The pivot itself is excluded
#    -- it is already final and must never be compared again.
# 5. countComparisons() resets the global counter and sorts `data[:]`, a COPY.
#    This matters: all three strategies must run against the SAME original
#    ordering, so the first run must not leave the array sorted for the next.
#
# Why the counts differ -- Enter Input : 9 8 7 6 5 4 3 2 1 0
#   First Pivot : pivot 9 is the maximum, so every element goes to its left and
#                 the split is 9 + 0. The next call faces 8, and so on -- the
#                 worst case, 9 + 8 + ... + 1 = 45 comparisons.
#   Last Pivot  : pivot 0 is the minimum, split 0 + 9. Also degenerate, also 45.
#   Middle Pivot: pivot 4 sits near the true median, splitting roughly in half
#                 each time, which collapses the total to 22.
#
#   On 1 2 3 4 5 6 7 8 9 0 the picture flips: First = 25, Last = 45, Middle = 20.
#   No single strategy is best for all inputs -- that is the lesson here.
# ================================================================================
