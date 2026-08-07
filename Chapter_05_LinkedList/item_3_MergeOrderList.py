# ================================================================================
# Chapter 5 - Item 3: MergeOrderList
# --------------------------------------------------------------------------------
# Problem Statement:
# Instructions for Merging Two Linked Lists Without Creating a LinkedList ClassNode Class:
# Ensure you have a Node class that contains a value and a reference to the next Node.Functions to Implement:
# createList(): Creates a LinkedList from a given list of values and returns the head of the LinkedList.printList(): Prints all the elements of a LinkedList starting from the given head.mergeOrderList(): Merges two LinkedLists into one in ascending order of their values and returns the head of the merged LinkedList.
# ****Using sort() is prohibited. If found, no points will be awarded.****
# ****Creating a LinkedList class is prohibited.****
# class node:    def __init__(self,data,next = None ):        ### Code Here ###
#     def __str__(self):        ### Code Here ###
# def createList(l=[]):    ### Code Here ###
# def printList(H):    ### Code Here ###
# def mergeOrderesList(p,q):    ### Code Here ###
# #################### FIX comand ####################   # input only a number save in L1,L2LL1 = createList(L1)LL2 = createList(L2)print('LL1 : ',end='')printList(LL1)print('LL2 : ',end='')printList(LL2)m = mergeOrderesList(LL1,LL2)print('Merge Result : ',end='')printList(m)
# ================================================================================

class node:
    def __init__(self, data, next=None):
        self.data = int(data)
        self.next = next
        
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if not l or l == ['']:
        return None
    head = node(l[0])
    cur = head
    for val in l[1:]:
        cur.next = node(val)
        cur = cur.next
    return head

def printList(H):
    cur = H
    while cur:
        print(cur.data, end=' ')
        cur = cur.next
    print()

def mergeOrderesList(p, q):
    dummy = node(0)
    cur = dummy
    while p and q:
        if p.data <= q.data:
            cur.next = p
            p = p.next
        else:
            cur.next = q
            q = q.next
        cur = cur.next
        
    if p:
        cur.next = p
    if q:
        cur.next = q
        
    return dummy.next

L1, L2 = [], []
inp = input('Enter 2 Lists : ').split(' ')
if len(inp) > 0 and inp[0]:
    L1 = inp[0].split(',')
if len(inp) > 1 and inp[1]:
    L2 = inp[1].split(',')

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(m)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 5 Item 3 (MergeOrderList).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================