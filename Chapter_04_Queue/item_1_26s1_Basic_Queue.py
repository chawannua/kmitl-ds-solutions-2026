# ================================================================================
# Chapter 4 - Item 1: 26s1 Basic Queue
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program that accepts two types of input using a QUEUE to solve the problem.
# E <value>
# Insert the value into the QUEUE.Display the value that was enqueued and the index of the newly added element.D
# Dequeue the front element of the QUEUE.Display the number that was removed and the size of the QUEUE after the dequeue operation.At the end, if there are still values in the QUEUE, display them. If the QUEUE is empty, display "Empty".
# ================================================================================

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)
        return len(self.items) - 1

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def getItems(self):
        return [str(item) for item in self.items]


inp = input("Enter Input : ")
commands = [cmd.strip() for cmd in inp.split(",")]

queue = Queue()

for cmd in commands:
    if cmd.startswith("E "):
        value = cmd.split()[1]
        index = queue.enqueue(value)
        print(f"Add {value} index is {index}")
    elif cmd == "D":
        if queue.isEmpty():
            print("-1")
        else:
            value = queue.dequeue()
            print(f"Pop {value} size in queue is {queue.size()}")

if queue.isEmpty():
    print("Empty")
else:
    print(f"Number in Queue is :  {queue.getItems()}")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 4 Item 1 (26s1 Basic Queue).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================