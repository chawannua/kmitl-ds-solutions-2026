# ================================================================================
# Chapter 9 - Item 4: 26s1 Find the Running Median
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program that accepts input as a list to find the median value of the
# data in the list. It should start with only one element in the list, then
# gradually add more elements until complete. When finding the median value, the
# data must first be sorted in ascending order. Then display the results
# according to the example.
# Do not use built-in sorting functions such as sort, min, max, etc.
#
# Extra question (input "EX"): What is a suitable sort algorithm?
# ================================================================================



def insertionSort(arr):
    """Own sort - no built-in sort() / sorted() / min() / max() used."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def median(arr):
    ordered = insertionSort(arr[:])         # work on a copy, keep input order
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        return ordered[mid] / 1             # force float, e.g. 3.0
    return (ordered[mid - 1] + ordered[mid]) / 2


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "Insertion sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l = list(map(int, l))
    running = []
    for value in l:
        running.append(value)               # grow the list one element at a time
        print(f'list = {running} : median = {median(running)}')

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# A running median: after every arrival, report the median of everything so far.
#
# Core idea:
#   Two different orders are live at the same time and must not be confused.
#   The list is DISPLAYED in arrival order, but the median is computed from a
#   SORTED copy. Sorting the displayed list in place would corrupt the output.
#
# Key Steps & Logic:
# 1. `running` grows by one element per iteration, so iteration k prints the
#    prefix of the first k inputs -- exactly the "start with one element, then
#    gradually add more" requirement.
# 2. median() sorts `arr[:]`, a copy, precisely so `running` keeps arrival order
#    for the f-string. This is the subtle part of the exercise.
# 3. Median by parity of n:
#      - n odd  -> the single middle element, ordered[n // 2].
#      - n even -> the mean of the two middle elements, ordered[n//2 - 1] and
#                  ordered[n//2].
# 4. `/ 1` on the odd branch is deliberate: the expected output is always a
#    float (`median = 3.0`, never `median = 3`). The even branch already yields
#    a float from `/ 2`. Because the two middle values are integers, the result
#    can only ever end in .0 or .5.
# 5. insertionSort() is the hand-written sort -- no sort(), sorted(), min() or
#    max() anywhere, as the restriction demands.
# 6. The 'EX' branch is the supplied template. The answer is Insertion sort:
#    this problem inserts ONE new element into an already-sorted sequence each
#    round, which is precisely insertion sort's best case -- O(n) per insert,
#    versus re-sorting the whole prefix from scratch with a general algorithm.
#
# Worked example -- Enter Input : 4 3 1 5 2 7 9 8
#   [4]          sorted [4]          n=1 odd  -> 4 / 1          = 4.0
#   [4, 3]       sorted [3, 4]       n=2 even -> (3 + 4) / 2    = 3.5
#   [4, 3, 1]    sorted [1, 3, 4]    n=3 odd  -> 3 / 1          = 3.0
#   [4, 3, 1, 5] sorted [1, 3, 4, 5] n=4 even -> (3 + 4) / 2    = 3.5
#   ... and so on; note the printed list stays in arrival order throughout.
# ================================================================================
