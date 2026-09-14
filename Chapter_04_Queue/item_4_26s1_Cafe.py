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
# Event-driven simulation of a 2-barista coffee shop using a FIFO queue.
#
# Core idea:
#   Instead of ticking the clock minute by minute, the simulation only tracks
#   WHEN each barista becomes free (b1_free / b2_free). This lets it jump
#   straight from one order to the next.
#
# Key Steps & Logic:
# 1. Parse "arr,prep/arr,prep/..." into Customer objects (cid = 1-based index)
#    and enqueue them in arrival order, so the queue enforces first-come,
#    first-served ORDERING (not first-served delivery).
#
# 2. For each customer popped off the queue:
#    a. Assign the barista who frees up earliest (b1_free <= b2_free).
#    b. start  = max(arr, barista_free)
#       The order starts only when BOTH conditions hold: the customer has
#       arrived AND the barista is free -- so the later of the two wins.
#       This single max() covers both cases (idle barista vs. waiting customer).
#    c. wait   = start - arr      (0 if the barista was already idle)
#       finish = start + prep
#    d. Update that barista's free time to finish.
#
# 3. Scan all customers for the largest wait. Using '>' (not '>=') means ties
#    resolve to the lowest customer id. max_wait staying 0 means nobody waited.
#
# 4. Sort by (finish, cid) before printing. This is required because the order
#    customers ORDER is not the order they RECEIVE: a short drink placed later
#    can overtake a long one (customer 3 finishes at t=6, customer 2 at t=7).
#    The cid tiebreaker keeps output stable when two drinks finish together.
#
# 5. Print each delivery time, then either "No waiting" or the longest waiter.
#
# Worked example -- Log : 0,3/0,7/2,3/7,7/10,5/10,1
#   cid  arr  prep  barista  start  wait  finish
#    1    0    3      B1       0      0      3
#    2    0    7      B2       0      0      7
#    3    2    3      B1       3      1      6    <- both busy on arrival
#    4    7    7      B1       7      0     14
#    5   10    5      B2      10      0     15
#    6   10    1      B1      14      4     15    <- longest wait
#   Delivery order after sorting: 1(3), 3(6), 2(7), 4(14), 5(15), 6(15)
# ================================================================================
