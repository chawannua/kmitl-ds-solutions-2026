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
# This Python script solves Chapter 7 Item 2 (25s1 BST height).
#
# Key Steps & Logic:
# 1. Node & BST Representation:
#    - Node stores integer data and left/right child pointers.
#    - BST contains methods to iteratively insert elements based on standard BST properties
#      (smaller values go to the left subtree, greater/equal values go to the right subtree).
# 2. Height Calculation:
#    - The height of a tree/node is defined recursively:
#      - An empty subtree (None) has height -1.
#      - A single root node with no children has height 1 + max(-1, -1) = 0.
#      - Any other node has height 1 + max(height(left), height(right)).
# 3. Input & Execution:
#    - Reads space-separated integers from user input.
#    - Inserts each value into the BST in the given sequence.
#    - Calculates and prints the total height of the tree rooted at root.
# ================================================================================
