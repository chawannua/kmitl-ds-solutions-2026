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
# Doubly linked list with head AND tail pointers, so every insert/remove must
# fix FOUR links (both directions on both neighbours), not just two.
#
# Core idea:
#   Because each Node has .next and .previous, whenever a node is spliced in
#   or out, its neighbour on each side must have that same relationship
#   updated in BOTH directions -- fixing only .next (like a singly linked
#   list) would leave str_reverse() walking a broken/partial chain.
#
# Key Steps & Logic:
# 1. append(data): if empty, new_node becomes both head and tail. Otherwise
#    link forward (tail.next = new_node) THEN backward
#    (new_node.previous = tail) THEN move the tail pointer. The forward link
#    must be set before tail is reassigned, or the old tail is lost.
#
# 2. insert(index, data) -- 3 cases, each reassigns pointers in a safe order:
#    a. index == 0: new_node.next = self.head (attach forward first, so the
#       old head is not lost), then self.head.previous = new_node, then
#       self.head = new_node.
#    b. index >= size: delegates to append() (inserting past the end == append).
#    c. middle: walk `cur` to the target index, then splice new_node BEFORE
#       cur: new_node.next = cur; new_node.previous = cur.previous;
#       cur.previous.next = new_node; cur.previous = new_node.
#       All 4 links are written -- 2 on new_node, 2 on its neighbours -- and
#       new_node.previous is read (cur.previous) before it gets overwritten
#       by the next line, so the order here also matters.
#
# 3. remove(data): walk `cur` until cur.data == data, then unlink it from
#    BOTH sides:
#    - if cur.previous exists, bridge it to cur.next; else cur WAS head, so
#      self.head must move to cur.next (special case: removing the head).
#    - if cur.next exists, bridge it back to cur.previous; else cur WAS tail,
#      so self.tail must move to cur.previous (special case: removing the
#      tail). A single-element list hits BOTH special cases at once, leaving
#      head = tail = None.
#
# 4. str_reverse() walks from self.tail via .previous -- this only produces
#    correct output because every insert/remove above kept .previous in sync
#    with .next; it is the direct proof that both directions were maintained.
#
# Worked example -- Enter Input : A a, A b, A c, Ab z, I 1:x, R b
#   A a   -> append: head=tail=[a]
#   A b   -> append: [a]<->[b]                 (tail becomes b)
#   A c   -> append: [a]<->[b]<->[c]           (tail becomes c)
#   Ab z  -> insert(0,z): head.previous=z, z.next=old head
#            before: head -> [a] <-> [b] <-> [c] <- tail
#            after:  head -> [z] <-> [a] <-> [b] <-> [c] <- tail
#   I 1:x -> insert(1,x): cur=[a] (index 1), splice x before it
#            before: [z] <-> [a] <-> [b] <-> [c]
#            after:  [z] <-> [x] <-> [a] <-> [b] <-> [c]
#   R b   -> remove('b'): cur=[b] has both neighbours (a, c)
#            before: [z] <-> [x] <-> [a] <-> [b] <-> [c]
#            after:  [z] <-> [x] <-> [a] <-> [c]     (b's slot bridged)
#   Final: linked list : z->x->a->c   reverse : c->a->x->z
# ================================================================================