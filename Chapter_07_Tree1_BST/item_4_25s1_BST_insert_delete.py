# ================================================================================
# Chapter 7 - Item 4: 25s1 BST insert / delete
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Python program to accept a sequence of commands to construct and modify
# a Binary Search Tree (BST):
#   - i <int> : Insert data into BST
#   - d <int> : Delete data from BST
# If deleting a value that is not found in the BST, display "Error! Not Found DATA".
# After each operation, display the operation and print the BST sideways (90 degrees).
#
# Inputs:
#   - Comma-separated list of commands (e.g. "i 3,i 5,i 2,d 3")
# Outputs:
#   - Printed operation name and 90-degree sideways tree visualization after each step.
# ================================================================================

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 


class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            curr = self.root
            while True:
                if val < curr.data:
                    if curr.left is None:
                        curr.left = Node(val)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(val)
                        break
                    else:
                        curr = curr.right
        return self.root

    def _delete_node(self, r, data):
        """Helper to recursively delete a node without triggering 'Not Found' error."""
        if r is None:
            return None
        if data < r.data:
            r.left = self._delete_node(r.left, data)
        elif data > r.data:
            r.right = self._delete_node(r.right, data)
        else:
            if r.left is None:
                return r.right
            elif r.right is None:
                return r.left
            else:
                curr = r.right
                while curr.left is not None:
                    curr = curr.left
                r.data = curr.data
                r.right = self._delete_node(r.right, curr.data)
        return r

    def delete(self, r, data):
        """Delete a node with value `data` from subtree rooted at `r`."""
        if r is None:
            print("Error! Not Found DATA")
            return None
        
        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                return r.right
            elif r.right is None:
                return r.left
            else:
                # Node with two children: replace with in-order successor
                curr = r.right
                while curr.left is not None:
                    curr = curr.left
                r.data = curr.data
                r.right = self._delete_node(r.right, curr.data)
        return r

                
def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for cmd in data:
    parts = cmd.strip().split()
    op = parts[0]
    val = int(parts[1])
    if op == 'i':
        print(f"insert {val}")
        tree.insert(val)
        printTree90(tree.root)
    elif op == 'd':
        print(f"delete {val}")
        tree.root = tree.delete(tree.root, val)
        printTree90(tree.root)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 7 Item 4 (25s1 BST insert / delete).
#
# Key Steps & Logic:
# 1. Binary Search Tree (BST) Properties:
#    - For any node, all values in the left subtree are smaller than the node's value.
#    - All values in the right subtree are greater than or equal to the node's value.
# 2. Node Insertion:
#    - Starting at the root, compare the value to insert with current node data.
#    - Traverse left if smaller, right if greater/equal, until an empty branch is found.
#    - Create and link the new Node at that position.
# 3. Node Deletion:
#    - If target node is not found in the tree (reaching None), prints "Error! Not Found DATA".
#    - Case 1 (Leaf node / 0 children): Remove the node directly (return None).
#    - Case 2 (1 child): Bypass the node and return its non-empty child (left or right).
#    - Case 3 (2 children): Find the in-order successor (the smallest value in the right
#      subtree), replace the target node's data with successor's data, and remove the
#      successor node from the right subtree using `_delete_node`.
# 4. Tree Visualization:
#    - Recursively traverses right subtree first, prints current node with level indentation
#      (5 spaces per level), then traverses left subtree to display the BST rotated 90 degrees.
# ================================================================================
