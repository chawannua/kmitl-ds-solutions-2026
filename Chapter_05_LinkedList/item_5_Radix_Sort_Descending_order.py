# ================================================================================
# Chapter 5 - Item 5: Radix Sort (Descending order)
# --------------------------------------------------------------------------------
# Problem Statement:
# Directions for Using Linked List to Perform Radix Sort in Descending OrderCreate a Linked List Class:
# Implement a Linked List class.Implement Radix Sort:
# Use the Linked List class to perform Radix Sort.Follow the algorithm steps as outlined in the last two slides of the lecture.Sort Order:
# Ensure the Radix Sort is done in descending order.Output Requirements:
# Display the result of each round of the Radix Sort.Ensure the sorting is done with the minimum number of rounds possible.In the last three lines of the output, include:The minimum number of rounds taken.The data before performing Radix Sort.The data after performing Radix Sort.Make sure to test your implementation to verify that it meets the above requirements.
# ================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def is_empty(self):
        return self.head is None
        
    def clear(self):
        self.head = self.tail = None
        
    def print_elements(self):
        cur = self.head
        elements = []
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        return " ".join(elements) + " " if elements else ""
        
    def to_arrow_string(self):
        cur = self.head
        elements = []
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        return " -> ".join(elements)

if __name__ == "__main__":
    inp = input("Enter Input : ").split()
    arr = [int(x) for x in inp]
    
    if not arr:
        exit(0)
        
    before_list = LinkedList()
    for num in arr:
        before_list.append(num)
        
    # Find max digits mathematically using absolute values to support negatives correctly
    max_abs_val = max(abs(x) for x in arr)
    if max_abs_val == 0:
        max_digits = 0
    else:
        max_digits = len(str(max_abs_val))
        
    main_list = LinkedList()
    for num in arr:
        if num >= 0:
            main_list.append(num)
    for num in arr:
        if num < 0:
            main_list.append(num)
        
    for rnd in range(1, max_digits + 1):
        print("-" * 60)
        print(f"Round : {rnd}")
        bins = [LinkedList() for _ in range(10)]
        
        cur = main_list.head
        while cur:
            val = cur.data
            digit = (abs(val) // (10 ** (rnd - 1))) % 10
            bins[digit].append(val)
            cur = cur.next
            
        for i in range(10):
            print(f"{i} : {bins[i].print_elements()}")
            
        main_list.clear()
        # Collect Positives (9 down to 0)
        for i in range(9, -1, -1):
            cur = bins[i].head
            while cur:
                if cur.data >= 0:
                    main_list.append(cur.data)
                cur = cur.next
                
        # Collect Negatives (0 up to 9)
        for i in range(10):
            cur = bins[i].head
            while cur:
                if cur.data < 0:
                    main_list.append(cur.data)
                cur = cur.next
                
    print("-" * 60)
    print(f"{max_digits} Time(s)")
    print(f"Before Radix Sort : {before_list.to_arrow_string()}")
    print(f"After  Radix Sort : {main_list.to_arrow_string()}")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# LSD (Least Significant Digit) Radix Sort, using linked lists as the 10
# digit "bins", producing DESCENDING order instead of the usual ascending.
#
# Core idea:
#   Sort one digit position at a time, starting from the ONES digit and
#   working up (`digit = (abs(val) // 10**(rnd-1)) % 10`). After sorting on
#   the least significant digit, then the next, ..., up through the most
#   significant digit, the whole list ends up fully ordered -- but ONLY if
#   each pass is STABLE (never reorders two values that land in the same
#   bin), because a later pass relies on the ordering left behind by earlier
#   passes for numbers sharing that digit.
#
# Key Steps & Logic:
# 1. max_digits = number of digits in the largest |value| (max_abs_val).
#    `for rnd in range(1, max_digits + 1)` runs EXACTLY max_digits passes --
#    no more, no fewer -- since a value's highest digit position is the last
#    one that can still change its bin placement.
#
# 2. Distribute pass: walk main_list once, compute `digit` for each node's
#    value, and bins[digit].append(val). Because this walks main_list IN
#    ORDER and append() only ever adds to the tail of a bin, two values
#    with the same digit keep their relative order from the previous
#    round -- this append-only, single left-to-right pass is what makes the
#    distribution step stable.
#
# 3. Collect pass rebuilds main_list from the bins, and this is where
#    DESCENDING order comes from:
#      - Positives are drained bins 9 -> 0 (`for i in range(9, -1, -1)`), so
#        a bigger digit (bigger magnitude) is placed first == descending.
#      - Negatives are drained bins 0 -> 9 (`for i in range(10)`), so a
#        SMALLER digit (closer to zero, i.e. less negative) is placed
#        first -- still descending, since less-negative > more-negative.
#      - All positives are emitted before any negative, matching that every
#        positive outranks every negative in descending order.
#    (Ascending radix sort would simply reverse both bin scan directions.)
#
# 4. before_list is a frozen snapshot of the input taken before any sorting,
#    kept only so the final "Before/After" report can show both states.
#
# Worked example -- Enter Input : 170 45 75 90 802 24 2 66  (3 rounds, since
# 802 has 3 digits)
#   Round 1 (ones digit)  bins: 0:[170,90] 2:[802,2] 4:[24] 5:[45,75] 6:[66]
#     rebuild descending by ones digit -> 66 24 802 2 45 75 170 90
#   Round 2 (tens digit)  regroups by tens digit, preserving round-1 order
#     within each bin -> 802 2 24 45 66 75 170 90
#   Round 3 (hundreds digit) bin 0 gets everything except 170 (bin1) and
#     802 (bin8); draining bins 9->0 puts 802, then 170, then the rest in
#     the stable order carried over from round 2
#   After Radix Sort : 802 -> 170 -> 90 -> 75 -> 66 -> 45 -> 24 -> 2
# ================================================================================