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
# This Python script solves Chapter 4 Item 2 (26s1 Queue-2).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================