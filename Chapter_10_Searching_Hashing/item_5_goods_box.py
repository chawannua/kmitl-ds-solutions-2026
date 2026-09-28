# ================================================================================
# Chapter 10 - Item 5: goods box
# --------------------------------------------------------------------------------
# Problem Statement:
# There are n items, item i weighs Wi kilograms. Pack them into no more than k
# boxes so that each box's total weight does not exceed its capacity, and items
# in the same box are consecutive. All boxes have the same capacity. Find the
# minimum capacity that packs all the items. (Hint: Optimization Problem)
#
# Inputs:
# - "<weights separated by spaces>/<number of boxes k>", e.g. 6 2 4 3 7/3
# Outputs:
# - "Minimum weigth for k box(es) = <capacity>" (spelling as on the portal)
# ================================================================================

def solve():
    inp = input('Enter Input : ').split('/')
    weights = list(map(int, inp[0].split()))
    k = int(inp[1])

    def can_pack(capacity):
        # Greedy: fill each box until the next item would overflow it
        boxes = 1
        current_weight = 0
        for w in weights:
            if current_weight + w > capacity:
                boxes += 1
                current_weight = w
            else:
                current_weight += w
        return boxes <= k

    # Capacity is at least the heaviest item and at most the total weight
    low = max(weights)
    high = sum(weights)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_pack(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(f"Minimum weigth for {k} box(es) = {ans}")

if __name__ == '__main__':
    solve()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Binary search on the answer (the box capacity).
# 1. can_pack(c): walk the items in order, starting a new box whenever the next
#    item doesn't fit. Feasible if that uses <= k boxes. A bigger capacity is
#    never worse, so feasibility is monotonic -> binary search works.
# 2. Search range: [max(weights), sum(weights)]. Keep the smallest feasible c.
#
# Worked example -- Enter Input : 6 2 4 3 7/3
#   range [7, 22]. c=14 ok, c=10 ok, c=8 ok ([6,2][4,3][7]), c=7 needs 4 -> no.
#   Answer: Minimum weigth for 3 box(es) = 8
# ================================================================================
