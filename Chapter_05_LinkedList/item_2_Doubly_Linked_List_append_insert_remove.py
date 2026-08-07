# ================================================================================
# Chapter 5 - Item 2: Doubly Linked List(append,insert,remove)
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a class for a Doubly Linked List which includes the following methods:
# def __init__(self): Initializes the linked list.
# def __str__(self): Returns a string representing the values in the linked list.
# def str_reverse(self): Returns a string representing the values in the linked list from back to front.
# def isEmpty(self): Returns whether the list is empty.
# def append(self, data): Adds a node with the given data to the end of the linked list.
# def insert(self, index, data): Inserts data at the specified index.
# def remove(self, data): Removes and returns the node with the given data.
# When inserting, the new data replaces the position of the old data, and the old data is moved to follow the new data.Input format is as follows:
# append -> Aadd_before -> Abinsert -> Iremove -> R******* Use the Node class to implement the Linked List. Do not use Python's built-in list.*********
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.previous = None
# ================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return ""
        cur = self.head
        s = str(cur.data)
        while cur.next:
            cur = cur.next
            s += "->" + str(cur.data)
        return s

    def str_reverse(self):
        if self.isEmpty():
            return ""
        cur = self.tail
        s = str(cur.data)
        while cur.previous:
            cur = cur.previous
            s += "->" + str(cur.data)
        return s

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def insert(self, index, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
            return
            
        sz = self.size()
        if index == 0:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        elif index >= sz:
            self.append(data)
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            new_node.next = cur
            new_node.previous = cur.previous
            cur.previous.next = new_node
            cur.previous = new_node

    def remove(self, data):
        cur = self.head
        idx = 0
        while cur:
            if cur.data == data:
                if cur.previous:
                    cur.previous.next = cur.next
                else:
                    self.head = cur.next
                    
                if cur.next:
                    cur.next.previous = cur.previous
                else:
                    self.tail = cur.previous
                return cur, idx
            cur = cur.next
            idx += 1
        return None, -1

if __name__ == "__main__":
    inp = input('Enter Input : ').split(',')
    L = DoublyLinkedList()
    
    for item in inp:
        item = item.strip()
        parts = item.split(' ')
        cmd = parts[0]
        
        if cmd == 'A':
            L.append(parts[1])
        elif cmd == 'Ab':
            L.insert(0, parts[1])
        elif cmd == 'I':
            idx, data = parts[1].split(':')
            idx = int(idx)
            if idx < 0 or idx > L.size():
                print("Data cannot be added")
            else:
                print(f"index = {idx} and data = {data}")
                L.insert(idx, data)
        elif cmd == 'R':
            removed, idx = L.remove(parts[1])
            if removed is None:
                print("Not Found!")
            else:
                print(f"removed : {parts[1]} from index : {idx}")
                
        print("linked list :", L)
        print("reverse :", L.str_reverse())

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 5 Item 2 (Doubly Linked List(append,insert,remove)).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================