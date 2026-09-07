# ================================================================================
# Chapter 7 - Item 1: 25s1 Binary Search Tree
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Python program to accept a sequence of integer for Binary Search Tree,
# the first input is the root. Build the BST and display it in 2D format.
#
# Inputs:
# - A sequence of space-separated integers representing nodes to insert into the BST.
# Outputs:
# - 2D tree representation printed sideways (root on the left, right child on top, left child on bottom).
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
    
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 7 Item 1 (25s1 Binary Search Tree).
#
# Key Steps & Logic:
# 1. Node & BST Representation:
#    - Node stores integer data and left/right child pointers.
#    - BST contains methods to iteratively insert elements based on standard BST properties:
#      values strictly less than the current node value go left, while greater or equal values go right.
# 2. Insertion:
#    - For each value in the input list, traverse from the root until finding an empty spot (None)
#      on the appropriate side (left or right) and attach a new Node.
# 3. 2D Tree Visualization (printTree):
#    - Uses reverse in-order traversal: right subtree first, then current node, then left subtree.
#    - Each depth level adds 5 indentation spaces, presenting the tree horizontally where the root
#      appears on the far left, right branches above, and left branches below.
# ================================================================================
