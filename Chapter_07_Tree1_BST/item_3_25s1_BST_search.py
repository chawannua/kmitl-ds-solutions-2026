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
# This Python script solves Chapter 7 Item 3 (25s1 BST search).
#
# Key Steps & Logic:
# 1. Parsed the input sequence of integers and threshold integer k separated by '/'.
# 2. Inserted each integer sequentially into a Binary Search Tree (BST).
# 3. Visualized the constructed BST using 2D tree formatting (right-root-left traversal).
# 4. Recursively traversed the tree to count all nodes whose value is less than or equal to k.
# ================================================================================
