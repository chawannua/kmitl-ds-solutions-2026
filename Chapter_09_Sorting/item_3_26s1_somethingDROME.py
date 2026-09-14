# ================================================================================
# Chapter 9 - Item 3: 26s1 somethingDROME
# --------------------------------------------------------------------------------
# Problem Statement:
# Receive a single integer input and display the result as follows:
# - If the input is in ascending order without any duplicate digits  -> "Metadrome"
# - If the input is in ascending order with duplicate digits         -> "Plaindrome"
# - If the input is in descending order without any duplicate digits -> "Katadrome"
# - If the input is in descending order with duplicate digits        -> "Nialpdrome"
# - If all digits in the input are the same                          -> "Repdrome"
# - If none of the above conditions are met                          -> "Nondrome"
# Do not use built-in sorting functions. Write your own sort function instead.
# ================================================================================



def insertionSort(arr):
    """Own sort - no built-in sort() / sorted() used."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


text = input("Enter Input : ").strip().lstrip('+-')
digits = [int(c) for c in text]

ascending = insertionSort(digits[:])        # sorted copy, small to large
descending = ascending[::-1]                # sorted copy, large to small

isAscending = digits == ascending
isDescending = digits == descending
hasDuplicate = len(set(digits)) != len(digits)
allSame = len(set(digits)) == 1

if allSame:
    print("Repdrome")
elif isAscending and not hasDuplicate:
    print("Metadrome")
elif isAscending:
    print("Plaindrome")
elif isDescending and not hasDuplicate:
    print("Katadrome")
elif isDescending:
    print("Nialpdrome")
else:
    print("Nondrome")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Six labels fall out of just two independent yes/no questions.
#
# Core idea:
#   "Is this ascending?" is answered by sorting a COPY and checking whether the
#   original already equals it. Reversing that same sorted copy answers
#   "is this descending?" for free. Duplicates are then the second axis, and the
#   two axes together pick one of the six names.
#
#         | no duplicates | has duplicates
#   asc   |   Metadrome   |   Plaindrome
#   desc  |   Katadrome   |   Nialpdrome
#   Repdrome is the overlap (every digit equal is both asc and desc), so it
#   must be tested FIRST or it would be misreported as Plaindrome.
#   Anything matching neither order is Nondrome.
#
# Key Steps & Logic:
# 1. .lstrip('+-') tolerates a signed integer; the digits themselves are what
#    the classification is about.
# 2. insertionSort() is the hand-written sort (no sort()/sorted()). It runs on
#    `digits[:]` -- a copy -- because the original order is the thing being
#    tested and must not be disturbed.
# 3. `descending = ascending[::-1]` costs nothing extra: the descending order of
#    a multiset is just its ascending order reversed. Note this stays correct
#    with duplicates, since reversing keeps equal digits adjacent.
# 4. set(digits) gives both remaining facts: len(set) != len(digits) means a
#    digit repeats, and len(set) == 1 means every digit is identical. A set is
#    not a sorting function, so the restriction still holds.
# 5. The if/elif chain is ordered so the stricter case is always checked before
#    the looser one it would otherwise be swallowed by.
#
# Worked examples
#   1357     -> asc, no dup                 -> Metadrome
#   12344    -> asc, dup (4 twice)          -> Plaindrome
#   7531     -> desc, no dup                -> Katadrome
#   9874441  -> desc, dup (4 three times)   -> Nialpdrome
#   666      -> all digits identical        -> Repdrome  (caught by the first test)
#   1985     -> neither asc nor desc        -> Nondrome
# ================================================================================
