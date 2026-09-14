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
# Guarded pipeline of validation checks before computing the Vickrey
# auction's winner and clearing price via sorting.
#
# Core idea:
#   A Vickrey auction winner pays the SECOND-highest bid, not their own, so
#   the script cannot just take max(bids) -- it must sort all bids and look
#   at the top two, while first ruling out the two ways the auction can be
#   invalid: too few bidders, or a tie for first place.
#
# Key Steps & Logic:
# 1. The try/except around [int(x) for x in input(...).split()] catches
#    non-integer tokens up front; ValueError triggers an error message and
#    `raise SystemExit` stops the script immediately instead of crashing
#    with a traceback or continuing with bad data.
# 2. if len(bids) < 2: handles "not enough bidder" -- a Vickrey auction
#    needs at least 2 bids to have both a winner and a second price.
# 3. highest = max(bids) and count_highest = bids.count(highest) find the
#    top bid value and count how many bidders hit it. Using count() (not
#    just comparing sorted[0] to sorted[1]) makes the tie check explicit
#    and readable: count_highest > 1 means at least two people tied for
#    first, which is invalid for this auction ("more than one highest
#    bid" -- there is no well-defined single winner or second price).
# 4. Only when there is a unique highest bidder does sorted_bids =
#    sorted(bids, reverse=True) run; sorted_bids[0] is the winning (highest)
#    bid and sorted_bids[1] is the second-highest, i.e. the price the
#    winner actually pays under Vickrey rules.
#
# Worked example -- Enter All Bid : 100 50 30
#   bids = [100, 50, 30]; len=3 >= 2, so no "not enough bidder"
#   highest = 100, count_highest = 1 -> unique winner, no tie error
#   sorted_bids = [100, 50, 30] -> winner_bid=100, second_highest=50
#   Printed output: "winner bid is 100 need to pay 50"
# ================================================================================