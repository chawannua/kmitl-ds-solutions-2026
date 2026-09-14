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
# Classic "merge two sorted linked lists" via a dummy head and two cursors --
# no new nodes are created for the merge, only existing nodes are re-linked.
#
# Core idea:
#   mergeOrderesList assumes p and q are each ALREADY sorted ascending. A
#   dummy sentinel node (`dummy = node(0)`) removes the need for an "is this
#   the first node?" special case: `cur` always has something to attach to,
#   even before any real node has been picked.
#
# Key Steps & Logic:
# 1. `p` and `q` are cursors into list 1 and list 2. While BOTH still have
#    nodes left, compare p.data <= q.data (the "<=" makes the merge stable --
#    ties keep list 1's node first) and re-link the smaller node's node
#    object onto cur.next, then advance that cursor (p = p.next or
#    q = q.next) and advance cur to the node just attached.
#
# 2. Only ONE of p/q can run out first. Whichever list still has nodes left
#    (`if p: cur.next = p` / `if q: cur.next = q`) is spliced onto the tail
#    of the merged list IN ONE STEP -- its remaining nodes are already sorted
#    relative to each other, so there is no need to walk them one at a time.
#
# 3. dummy.next (not dummy itself) is returned, since dummy was only a
#    throwaway anchor to hang the first real node from cur.next.
#
# Worked example -- Enter 2 Lists : 1,3,5 2,4,6
#   LL1: [1] -> [3] -> [5] -> None
#   LL2: [2] -> [4] -> [6] -> None
#   dummy -> ?                         cur = dummy
#   1<=2 -> take 1   dummy -> [1]                        p advances to 3
#   3> 2  -> take 2   dummy -> [1] -> [2]                q advances to 4
#   3<=4 -> take 3   dummy -> [1] -> [2] -> [3]          p advances to 5
#   5> 4  -> take 4   dummy -> [1] -> [2] -> [3] -> [4]  q advances to 6
#   5<=6 -> take 5   ... -> [5]                          p becomes None
#   q still holds [6] -> spliced whole: cur.next = q
#   Merge Result : 1 2 3 4 5 6
# ================================================================================