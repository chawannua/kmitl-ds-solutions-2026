# ================================================================================
# Chapter 7 - Item 3: 25s1 BST search
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a python program to accept a sequence of integer and k.
# - create BST from a sequence
# - find out the number of nodes that less than or equal to k.
# ================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    else:
                        curr = curr.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def count_less_equal(self, node, k):
        if node is None:
            return 0
        count = 1 if node.data <= k else 0
        return count + self.count_less_equal(node.left, k) + self.count_less_equal(node.right, k)


T = BST()
inp, k = input('Enter Input : ').split('/')
k = int(k)
numbers = [int(i) for i in inp.split()]
for i in numbers:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(T.count_less_equal(root, k))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Builds a BST, then counts nodes <= k with an UNCONDITIONAL full traversal
# (despite the item's name, this is not a pruned/halving search).
#
# BST invariant: enforced only inside insert(), the same "data < curr.data
# -> left, else -> right" comparison as item_1/item_2. printTree() also
# reuses the right-node-left sideways layout from item_1.
#
# Key Steps & Logic:
# 1. The input line is split on '/' into the number sequence and the
#    threshold k (e.g. "8 3 10 1 6 14/6" -> numbers and k=6); the numbers
#    are inserted into the BST one by one via insert(), exactly like item_1.
# 2. count_less_equal(node, k) is NOT a binary search: it checks
#    "node.data <= k" for the current node, then unconditionally recurses
#    into BOTH node.left and node.right, summing all three counts. It never
#    uses the BST ordering to skip a branch, so it visits every node -- an
#    O(n) full-tree scan rather than an O(log n) bounded range lookup.
# 3. printTree(root) draws the sideways tree first, then a '----' divider
#    line is printed, then the final count from count_less_equal is printed.
#
# Worked example -- Enter Input : 8 3 10 1 6 14/6
#   Tree (same shape as item_1):
#
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#
#   count_less_equal visits all 6 nodes: 8<=6? no. 3<=6? yes. 10<=6? no.
#   1<=6? yes. 6<=6? yes. 14<=6? no. Total matches = 3.
#   Program prints the sideways tree, the '----' divider, then: 3
# ================================================================================
