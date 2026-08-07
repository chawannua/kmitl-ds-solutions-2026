# ================================================================================
# Chapter 5 - Item 1: Singly Linked List
# --------------------------------------------------------------------------------
# Problem Statement:
# Instructions for Implementing a Singly Linked List ClassWrite a class for a Singly Linked List that includes the following methods:
# __init__(self): Initializes the head to indicate the starting point of the Linked List.__str__(self): Returns a string representation of the Linked List, showing all elements from head to tail.isEmpty(self): Checks if the Linked List is empty and returns True or False.append(self, data): Adds an item to the end of the Linked List. Does not return a value.addHead(self, data): Adds an item to the front of the Linked List. Does not return a value.search(self, data): Searches for the desired item in the Linked List and returns Found or Not Found.index(self, data): Searches for the desired item in the Linked List and returns its index (0, 1, 2, 3, 4, ...). If not found, returns -1.size(self): Returns the size of the Linked List.pop(self, pos): Removes the item at the given index pos from the Linked List and returns Success or Out of Range.Input Format:append -> APaddHead -> AHsearch -> SEindex -> IDsize -> SIpop -> PO
# class Node:    def __init__(self, value):        self.value = value        self.next = None
# class LinkedList:    def __init__(self):        self.head = None
#     def __str__(self):        if self.isEmpty():            return "Empty"        cur, s = self.head, str(self.head.value) + " "        while cur.next != None:            s += str(cur.next.value) + " "            cur = cur.next        return s
#     def isEmpty(self):        return self.head == None
#     def append(self, item):        # Code Here
#     def addHead(self, item):        # Code Here
#     def search(self, item):        # Code Here
#     def index(self, item):        # Code Here
#     def size(self):        # Code Here
#     def pop(self, pos):        # Code HereL = LinkedList()inp = input('Enter Input : ').split(',')for i in inp:    if i[:2] == "AP":        L.append(i[3:])    elif i[:2] == "AH":        L.addHead(i[3:])    elif i[:2] == "SE":        print(f"{L.search(i[3:])} {i[3:]} in {L}")    elif i[:2] == "SI":        print(f"Linked List size = {L.size()} : {L}")    elif i[:2] == "ID":        print(f"Index ({i[3:]}) = {L.index(i[3:])} : {L}")    elif i[:2] == "PO":        before = f"{L}"        k = L.pop(int(i[3:]))        if k == "Success":            print(f"{k} | {before}-> {L}")        else:            print(f"{k} | {L}")before = f"{L}"
# ================================================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, item):
        cur = self.head
        idx = 0
        while cur != None:
            if cur.value == item:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if pos < 0 or self.isEmpty():
            return "Out of Range"
        
        if pos == 0:
            self.head = self.head.next
            return "Success"
            
        cur = self.head
        idx = 0
        while cur.next != None and idx < pos - 1:
            cur = cur.next
            idx += 1
            
        if cur.next == None:
            return "Out of Range"
            
        cur.next = cur.next.next
        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print(f"{L.search(i[3:])} {i[3:]} in {L}")
    elif i[:2] == "SI":
        print(f"Linked List size = {L.size()} : {L}")
    elif i[:2] == "ID":
        print(f"Index ({i[3:]}) = {L.index(i[3:])} : {L}")
    elif i[:2] == "PO":
        before = f"{L}"
        k = L.pop(int(i[3:]))
        if k == "Success":
            print(f"{k} | {before}-> {L}")
        else:
            print(f"{k} | {L}")

print("Linked List :", L)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 5 Item 1 (Singly Linked List).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================