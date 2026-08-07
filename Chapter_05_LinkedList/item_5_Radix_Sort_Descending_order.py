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
# This Python script solves Chapter 5 Item 5 (Radix Sort (Descending order)).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================