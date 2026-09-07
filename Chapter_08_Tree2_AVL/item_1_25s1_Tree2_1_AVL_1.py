# ================================================================================
# Chapter 8 - Item 1: 25s1 Tree2-1 AVL-1
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program to receive input, create an AVL tree, and display the post-order traversal of the nodes.
# Modify the add method to add data to the AVL tree, and the postOrder method to traverse all nodes in post-order.
# ================================================================================

class AVLTree:

    class AVLNode:

        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()        

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a,b)
            return self.height            

        def getHeight(self, node):
            return -1 if node == None else node.height
          
        def balanceValue(self):    
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = AVLTree._add(self.root, int(data))

    def _add(root, data):
        if root is None:
            return AVLTree.AVLNode(data)

        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)

        root.setHeight()

        balance = root.balanceValue()

        # Left heavy
        if balance < -1:
            if root.left.balanceValue() <= 0:
                return AVLTree.rotateLeftChild(root)
            else:
                root.left = AVLTree.rotateRightChild(root.left)
                return AVLTree.rotateLeftChild(root)

        # Right heavy
        if balance > 1:
            if root.right.balanceValue() >= 0:
                return AVLTree.rotateRightChild(root)
            else:
                root.right = AVLTree.rotateLeftChild(root.right)
                return AVLTree.rotateRightChild(root)

        return root

    def rotateLeftChild(root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.setHeight()
        new_root.setHeight()
        return new_root

    def rotateRightChild(root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.setHeight()
        new_root.setHeight()
        return new_root

    def postOrder(self):
        print('AVLTree post-order :', end=' ')
        AVLTree._postOrder(self.root)
        print()

    def _postOrder(root):
        if root is not None:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data, end=' ')

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)


avl1 = AVLTree()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])

    elif i[:2] == "PR":
        avl1.printTree()

    elif i[:2] == "PO":

        avl1.postOrder()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 8 Item 1 (25s1 Tree2-1 AVL-1).
#
# Key Steps & Logic:
# 1. Parsed comma-separated operations ('AD <val>', 'PR', 'PO').
# 2. Built an AVL tree with self-balancing rotations (Left-Left, Left-Right, Right-Right, Right-Left).
# 3. Implemented post-order depth-first traversal and 2D formatted tree visualization.
# ================================================================================
