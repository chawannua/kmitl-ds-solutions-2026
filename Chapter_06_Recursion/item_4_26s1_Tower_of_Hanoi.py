# ================================================================================
# Chapter 6 - Item 4: 26s1 Tower of Hanoi
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program to solve the Tower of Hanoi problem. We have three rods: A, B, and C, and the input is the number of disks stacked on the rods. The program should display the sequence of moves required to transfer all the disks from rod A to rod C, ensuring that a smaller disk is always on top of a larger disk (a smaller disk must never be placed below a larger disk).
# Restrictions:
# Do not use for, while, or do while loops.Every function should have no more than 5 parameters.Guidelines:
# Create a separate function for displaying results.Use lists to store the state of each rod.Be careful when swapping lists.If you have any questions about the Tower of Hanoi, feel free to ask the TA for more information or try the game at Tower of Hanoi Game.
# def move(n,A,B,C,maxn):    #code heren = int(input("Enter Input : "))
# ================================================================================

rods = {'A': [], 'B': [], 'C': []}

def init_rods(current):
    if current == 0:
        return
    rods['A'].append(current)
    init_rods(current - 1)

def print_row(maxn, row):
    if row < 0:
        return
    val_a = str(rods['A'][row]) if len(rods['A']) > row else "|"
    val_b = str(rods['B'][row]) if len(rods['B']) > row else "|"
    val_c = str(rods['C'][row]) if len(rods['C']) > row else "|"
    print(f"{val_a}  {val_b}  {val_c}")
    print_row(maxn, row - 1)

def display(maxn):
    print_row(maxn, maxn)

def move(n, A, B, C, maxn):
    if n == 0:
        return
    move(n-1, A, C, B, maxn)
    print(f"move {n} from  {A} to {C}")
    rods[C].append(rods[A].pop())
    display(maxn)
    move(n-1, B, A, C, maxn)

if __name__ == "__main__":
    n = int(input("Enter Input : "))
    init_rods(n)
    display(n)
    move(n, 'A', 'B', 'C', n)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Classic Tower of Hanoi solved with the 3-step recursive decomposition.
#
# Core idea:
#   To move n disks from A to C (using B as spare), it is enough to: move the
#   top n-1 disks out of the way onto B, move disk n straight from A to C, then
#   move those n-1 disks from B onto C. Each sub-move is the SAME problem with
#   n-1 disks and the rod roles rotated, so move() calls itself with the
#   parameters permuted instead of writing three different functions.
#
# Key Steps & Logic:
# 1. Base case: n == 0 returns immediately -- "move zero disks" does nothing,
#    so every branch of the recursion bottoms out here.
# 2. Recursive case, move(n, A, B, C, maxn):
#    a. move(n-1, A, C, B, maxn) -- move the smaller stack from A to B, with
#       C (the final destination) temporarily used as the spare rod.
#    b. print(...) + rods[C].append(rods[A].pop()) -- physically move disk n
#       itself straight from A to C, then display(maxn) redraws all rods.
#    c. move(n-1, B, A, C, maxn) -- move the smaller stack from B to C, now
#       using A (the original source) as the spare rod.
#    Every nested call is made with n - 1, and the base case intercepts n == 0
#    before n can go negative, so the recursion always terminates.
# 3. init_rods(current) recursively stacks disks current..1 onto rod A first,
#    using the same shrink-by-1-to-0 base-case pattern.
# 4. print_row(maxn, row) recurses from row = maxn down to row = 0 (base case
#    row < 0) to draw the rods one row per call, top row first.
#
# Worked example -- Enter Input : 2   (moves printed = 2^2 - 1 = 3)
#   move(2, A, B, C)
#   +- move(1, A, C, B)              # get disk 1 out of the way: A -> B
#   |  +- move(0, A, B, C)           (base case, no-op)
#   |  +- disk 1: A -> B  =>  "move 1 from  A to B"
#   |  +- move(0, B, A, C)           (base case, no-op)
#   +- disk 2: A -> C     =>  "move 2 from  A to C"
#   +- move(1, B, A, C)              # bring disk 1 back on top: B -> C
#      +- move(0, B, C, A)           (base case, no-op)
#      +- disk 1: B -> C  =>  "move 1 from  B to C"
#      +- move(0, A, B, C)           (base case, no-op)
# ================================================================================