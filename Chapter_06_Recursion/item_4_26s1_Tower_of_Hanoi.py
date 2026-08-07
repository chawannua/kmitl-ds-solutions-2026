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
# This Python script solves Chapter 6 Item 4 (26s1 Tower of Hanoi).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================