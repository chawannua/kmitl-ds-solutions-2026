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
# Direct FIFO queue built on a Python list, driven by comma-separated "E"/"D" ops.
#
# Core idea:
#   enqueue() reports the index the value LANDED at, and dequeue() always removes
#   from the FRONT (index 0), so the printed indices/sizes double as a live trace
#   of the queue's front-to-rear layout without ever inspecting items directly.
#
# Key Steps & Logic:
# 1. inp.split(",") breaks "E 1,E 2,D,..." into individual commands; each is
#    stripped so stray spaces around commas don't break the "E "/"D" prefix check.
# 2. "E <value>": queue.enqueue(value) appends to self.items and returns
#    len(self.items) - 1 -- the index is computed AFTER the append, so it always
#    equals the value's rear position, matching "Add <value> index is <i>".
# 3. "D": isEmpty() is checked first because pop(0) on an empty list would raise
#    IndexError; if empty the command prints "-1" instead of crashing. Otherwise
#    dequeue() does self.items.pop(0), removing the FRONT element -- O(n) shift
#    cost, acceptable here since the queue stays small.
# 4. After all commands, isEmpty() decides between "Empty" and printing
#    getItems(), which stringifies whatever is left in front-to-rear order.
#
# Worked example -- "E 1,E 2,D,E 3,D,D,D"
#   op    | queue after | printed
#   ------+-------------+-----------------------------
#   E 1   | ['1']       | Add 1 index is 0
#   E 2   | ['1','2']   | Add 2 index is 1
#   D     | ['2']       | Pop 1 size in queue is 1
#   E 3   | ['2','3']   | Add 3 index is 1
#   D     | ['3']       | Pop 2 size in queue is 1
#   D     | []          | Pop 3 size in queue is 0
#   D     | []          | -1               <- isEmpty() caught the extra D
#   final:  Empty
# ================================================================================