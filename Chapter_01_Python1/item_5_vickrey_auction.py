# ================================================================================
# Chapter 1 - Item 5: vickrey auction
# --------------------------------------------------------------------------------
# Problem Statement:
# Create a simulation of a Vickrey auction. A Vickrey auction is a type of auction where the winner is the person who submits the highest bid, but the actual price paid is the second-highest bid.
# Display output as examples.
# word"Enter All Bid : ""not enough bidder"
# "error : have more than one highest bid""winner bid is $ need to pay $"
# ================================================================================

try:
    bids = [int(x) for x in input("Enter All Bid : ").split()]
except ValueError:
    print("error : invalid bid value")
    raise SystemExit

if len(bids) < 2:
    print("not enough bidder")
else:
    highest = max(bids)
    count_highest = bids.count(highest)
    if count_highest > 1:
        print("error : have more than one highest bid")
    else:
        sorted_bids = sorted(bids, reverse=True)
        winner_bid = sorted_bids[0]
        second_highest = sorted_bids[1]
        print(f"winner bid is {winner_bid} need to pay {second_highest}")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 1 Item 5 (vickrey auction).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================