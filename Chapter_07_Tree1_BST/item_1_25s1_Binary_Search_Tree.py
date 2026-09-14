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
# Iterative BST insertion plus a reversed-inorder (right, node, left) printout.
#
# BST invariant: every node's left subtree holds smaller values and its right
# subtree holds greater-or-equal values. insert() enforces this with one
# comparison at each step of the descent: "if data < curr.data" moves left,
# the "else" branch moves right (inside the "while True" loop).
#
# Key Steps & Logic:
# 1. insert() starts at self.root and walks down: at each curr it compares
#    the new value to curr.data and moves to curr.left or curr.right, until
#    it finds an empty (None) child slot -- then it attaches a new Node
#    there. Every inserted value becomes a LEAF at the moment it is placed.
# 2. printTree(node, level) runs once on the finished root. It recurses into
#    node.right, prints the current node, then recurses into node.left --
#    the reverse of a normal left-node-right inorder walk. Because right
#    children print before their parent and left children print after,
#    rotating the console output 90 degrees clockwise turns it into a
#    normal top-down tree, with right branches above the root line and
#    left branches below it.
# 3. Indentation is '     ' * level (5 spaces per depth), so each recursive
#    level is pushed one column further right -- this is what makes the
#    sideways layout readable as a tree shape.
#
# Worked example -- Enter Input : 8 3 10 1 6 14
#   Insertions in order: 8 becomes root; 3 < 8 goes left of 8; 10 >= 8 goes
#   right of 8; 1 < 8 and < 3 goes left of 3; 6 < 8 but >= 3 goes right of
#   3; 14 >= 8 and >= 10 goes right of 10.
#
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#
#   printTree walks right-node-left at every level, so the actual console
#   output (5 spaces of indent per depth level) is:
#              14
#         10
#    8
#              6
#         3
#              1
# ================================================================================
