# ================================================================================
# Chapter 4 - Item 2: 26s1 Queue-2
# --------------------------------------------------------------------------------
# Problem Statement:
# Simulate queue shifting within a specified time using the class Queue.
# There is one main queue of any length.The queue in front of cashier 1 has a length of 5 people, with each person taking 3 minutes for service.The queue in front of cashier 2 has a length of 5 people, with each person taking 2 minutes for service.Customers move from the main queue every 1 minute. If cashier 1's queue is empty, they go there first; if it's full, they go to cashier 2.Display the minutes, the main queue, cashier 1 queue, and cashier 2 queue until the main queue is empty.
# ================================================================================

class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, value):
        self.items.append(value)
        
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None
        
    def isEmpty(self):
        return len(self.items) == 0
        
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    inp = input("Enter people : ")

    main_q = Queue()
    for char in inp:
        main_q.enqueue(char)
            
    q1 = Queue()
    q2 = Queue()
    
    time = 1
    q1_tick = 0
    q2_tick = 0
    
    while not main_q.isEmpty():
        if not q1.isEmpty():
            q1_tick += 1
            if q1_tick == 3:
                q1.dequeue()
                q1_tick = 0
                
        if not q2.isEmpty():
            q2_tick += 1
            if q2_tick == 2:
                q2.dequeue()
                q2_tick = 0
                
        person = main_q.dequeue()
        if q1.size() < 5:
            q1.enqueue(person)
        else:
            q2.enqueue(person)
            
        print(f"{time} {main_q} {q1} {q2}")
        time += 1

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Minute-by-minute simulation of three chained queues (main -> cashier 1/cashier 2).
#
# Core idea:
#   q1_tick / q2_tick are per-cashier "minutes elapsed on current customer"
#   counters. A dequeue only happens once a counter reaches that cashier's
#   fixed service time (3 for q1, 2 for q2), so each Queue never needs to know
#   about time itself -- the ticks live outside it.
#
# Key Steps & Logic:
# 1. Every character of the input string becomes one person; main_q.enqueue(char)
#    loads them all in arrival order before the simulation starts.
# 2. Each loop iteration is one minute. First, IF a cashier queue is non-empty,
#    its tick counter increments; hitting the service time triggers
#    q1.dequeue()/q2.dequeue() (pop(0) on the front) and resets the tick to 0.
#    This check runs BEFORE the new arrival below, so a just-served slot can be
#    refilled the same minute.
# 3. One person leaves main_q via dequeue() and joins q1 if q1.size() < 5 (still
#    has room), else falls through to q2 -- cashier 1 is always preferred.
# 4. print(f"{time} {main_q} {q1} {q2}") uses Queue.__str__ (== str(self.items))
#    so each line shows the front-to-rear contents of all three queues for that
#    minute; the loop stops the instant main_q is empty, even if q1/q2 still
#    have people waiting to be served.
#
# Worked example -- "ABCDEFG" (service times: q1=3 min, q2=2 min)
#   t | main_q            | q1                | q2 | note
#   --+-------------------+-------------------+----+----------------------------
#   1 | [B,C,D,E,F,G]     | [A]               | [] | A enters q1 (empty)
#   2 | [C,D,E,F,G]       | [A,B]             | [] | tick=1, no dequeue yet
#   3 | [D,E,F,G]         | [A,B,C]           | [] | tick=2
#   4 | [E,F,G]           | [B,C,D]           | [] | tick=3 -> A served, D in
#   7 | []                | [C,D,E,F,G]       | [] | tick=3 -> B served, G in
#   q2 stays empty the whole run because q1.size() never reaches 5 when checked.
# ================================================================================