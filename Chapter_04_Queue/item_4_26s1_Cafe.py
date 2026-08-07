# ================================================================================
# Chapter 4 - Item 4: 26s1 Cafe
# --------------------------------------------------------------------------------
# Problem Statement:
# Coffee Shop ScenarioAt a certain coffee shop, there are 2 baristas. Customers arrive at time si and order a coffee that takes pi minutes to make. If both baristas are busy, the customer has to wait in a queue.
# Your tasks:
# Simulate the order in which customers receive their coffee.
# Identify the customer who waited the longest before placing their order.
# If nobody had to wait, display: No waiting.
# Input date
# Log : 0,3/0,7/2,3/7,7/10,5/10,1
# ???? Explanation
# Customer 1 enters at time 0 and orders a coffee that takes 3 minutes to make.
# Customer 2 enters at time 0 and orders a coffee that takes 7 minutes to make.
# Customer 3 enters at time 2 and orders a coffee that takes 3 minutes to make.
# Customer 4 enters at time 7 and orders a coffee that takes 7 minutes to make.
# Customer 5 enters at time 10 and orders a coffee that takes 5 minutes to make.
# Customer 6 enters at time 10 and orders a coffee that takes 1 minute to make.
# ⏰ Timeline
# Time (t)Event0Customers 1 and 2 enter the shop and place their orders.2Customer 3 enters the shop.3Customer 1 gets their coffee. Customer 3 places an order after waiting 1 minute.6Customer 3 gets their coffee.7Customer 2 gets their coffee. Customer 4 enters and places an order.10Customers 5 and 6 enter the shop. Customer 5 places an order.14Customer 4 gets their coffee. Customer 6 places an order after waiting 4 minutes.15Customers 5 and 6 get their coffee.
# ================================================================================

class Customer:
    def __init__(self, cid, arr, prep):
        self.cid = cid
        self.arr = arr
        self.prep = prep
        self.finish = 0
        self.wait = 0

class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, value):
        self.items.append(value)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
        
    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    print(" ***Cafe***")
    inp = input("Log : ").split('/')
    
    q = Queue()
    for i, s in enumerate(inp):
        arr, prep = map(int, s.split(','))
        q.enqueue(Customer(i + 1, arr, prep))
        
    b1_free = 0
    b2_free = 0
    
    processed = []
    
    while not q.is_empty():
        c = q.dequeue()
        if b1_free <= b2_free:
            start = max(c.arr, b1_free)
            c.wait = start - c.arr
            c.finish = start + c.prep
            b1_free = c.finish
        else:
            start = max(c.arr, b2_free)
            c.wait = start - c.arr
            c.finish = start + c.prep
            b2_free = c.finish
        processed.append(c)
        
    max_wait = 0
    max_wait_cid = -1
    for c in processed:
        if c.wait > max_wait:
            max_wait = c.wait
            max_wait_cid = c.cid
            
    processed.sort(key=lambda x: (x.finish, x.cid))
    
    for c in processed:
        print(f"Time {c.finish} customer {c.cid} get coffee")
        
    if max_wait == 0:
        print("No waiting")
    else:
        print(f"The customer who waited the longest is : {max_wait_cid}")
        print(f"The customer waited for {max_wait} minutes")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 4 Item 4 (26s1 Cafe).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================