# ================================================================================
# Chapter 4 - Item 3: 26s1 Concept Queue
# --------------------------------------------------------------------------------
# Problem Statement:
# Accept a single line of input where each sequence is indicated by a letter followed by the number of times the action should be performed. 'E' indicates an enqueue operation, and 'D' indicates a dequeue operation. If the letter is something else, count it as an error input.
# You must report how many ineffective dequeues occur in sequence and show how the queue changes at each step.
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
    inp_string = input("input : ")
    inp = inp_string.split(",")
    
    q = Queue()
    enq_counter = 0
    error_dequeue = 0
    error_input = 0
    
    for step in inp:
        step = step.strip()
        print(f"Step : {step}")
        if step.startswith('E') and step[1:].isdigit():
            count = int(step[1:])
            for _ in range(count):
                q.enqueue(f"*{enq_counter}")
                enq_counter += 1
            print(f"Enqueue : {q}")
        elif step.startswith('D') and step[1:].isdigit():
            count = int(step[1:])
            for _ in range(count):
                if q.isEmpty():
                    error_dequeue += 1
                else:
                    q.dequeue()
            print(f"Dequeue : {q}")
        else:
            error_input += 1
            print(q)
            
        print(f"Error Dequeue : {error_dequeue}")
        print(f"Error input : {error_input}")
        print("-" * 20)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 4 Item 3 (26s1 Concept Queue).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================