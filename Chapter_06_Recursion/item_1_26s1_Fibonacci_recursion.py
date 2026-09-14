# ================================================================================
# Chapter 6 - Item 1: 26s1 Fibonacci recursion
# --------------------------------------------------------------------------------
# Problem Statement:
# *** Do not use while or for loop ***Write Fibonacci program
# The function fibo(n) is defined to return the Fibonacci number for a given n.If n is 1 or 2, the function returns 1 (base cases).For any other n, the function recursively calls itself to compute the sum of fibo(n-1) and fibo(n-2).
# ================================================================================

print(" *** Find fibonacci sequence ***")
n = input("Enter n : ")
n = int(n)

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(f"fibo({n}) = {fibo(n)}")
print("===== End of program =====")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Plain recursive tree evaluation of the Fibonacci recurrence -- no memoization.
#
# Core idea:
#   fibo(n) is defined purely by the recurrence fibo(n) = fibo(n-1) + fibo(n-2),
#   so the function re-derives the two smaller Fibonacci numbers it needs instead
#   of looking them up, calling itself twice per non-base case.
#
# Key Steps & Logic:
# 1. Base case: n == 1 or n == 2 returns 1 directly, with NO further recursion.
#    This is where every branch of the call tree stops growing.
# 2. Recursive case (else): return fibo(n - 1) + fibo(n - 2). Each call spawns
#    two smaller calls whose arguments are strictly less than n, so every path
#    from fibo(n) down to a leaf shrinks n by at least 1 each step and must hit
#    n == 1 or n == 2 in a finite number of steps -- this guarantees termination.
# 3. Because both fibo(n-1) and fibo(n-2) are computed independently (no cache),
#    the same smaller values (e.g. fibo(2)) are recomputed many times -- this is
#    what makes the runtime exponential in n.
#
# Worked example -- Enter n : 5  ->  fibo(5) = 5   (9 total fibo() calls)
#   fibo(5)
#   +- fibo(4)
#   |  +- fibo(3)
#   |  |  +- fibo(2) -> 1           (base case)
#   |  |  +- fibo(1) -> 1           (base case)  => 2
#   |  +- fibo(2) -> 1              (base case)  => 3
#   +- fibo(3)
#      +- fibo(2) -> 1              (base case)
#      +- fibo(1) -> 1              (base case)  => 2
#   => fibo(5) = 3 + 2 = 5
# ================================================================================