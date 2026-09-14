# ================================================================================
# Chapter 7 - Item 2: 25s1 BST height
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Python program to accept a sequence of integer for Binary Search Tree, 
# the first input is the root. Then find out the height of the tree.
#
# Inputs:
# - A sequence of space-separated integers representing nodes to insert into the BST.
# Outputs:
# - The height of the constructed Binary Search Tree (where a single root node has height 0).
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

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is :", T.height(root))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Recursive tree height measured in EDGES, not nodes, via post-order recursion.
#
# BST invariant: reused unchanged from insert() -- values less than curr.data
# go left, values greater-or-equal go right (same code as item_1). height()
# does not depend on the invariant at all; it only needs the left/right
# pointers that insert() already built.
#
# Key Steps & Logic:
# 1. height(node) has the base case "if node is None: return -1" for an
#    empty subtree. That -1 is the trick that makes a single leaf come out
#    as height 0: 1 + max(height(None), height(None)) = 1 + max(-1,-1) = 0,
#    matching the header's rule "a single root node has height 0".
# 2. For any other node, height(node) = 1 + max(height(node.left),
#    height(node.right)) -- the 1 accounts for the edge down to whichever
#    child subtree is taller, so the result is the count of EDGES on the
#    longest root-to-leaf path (not the count of nodes on that path).
# 3. main flow inserts every input value in order, then calls height(root)
#    exactly once on the fully built tree and prints the result.
#
# Worked example -- Enter Input : 8 3 10 1 6 14
#   Same insert order as item_1, producing:
#
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#
#   height(1) = height(6) = height(14) = 0 (each is a leaf).
#   height(3)  = 1 + max(height(1), height(6))    = 1 + max(0, 0)  = 1.
#   height(10) = 1 + max(height(None), height(14)) = 1 + max(-1, 0) = 1.
#   height(8)  = 1 + max(height(3), height(10))    = 1 + max(1, 1)  = 2.
#   Program prints: Height of this tree is : 2
# ================================================================================
