# ================================================================================
# Chapter 8 - Item 2: 25s1 Tree2-2 AVL-2
# --------------------------------------------------------------------------------
# Problem Statement:
# Create an AVL Tree using a class. After each round of insertion, display the tree and check whether it is balanced. If not, adjust the balance and display the result accordingly.
# ================================================================================

class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rotateRight(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, root, data):
        val = int(data)
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            print("Not Balance, Rebalance!")
            return self.rotateRight(root)

        # Case 2 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            print("Not Balance, Rebalance!")
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Case 3 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            print("Not Balance, Rebalance!")
            return self.rotateLeft(root)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            print("Not Balance, Rebalance!")
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 8 Item 2 (25s1 Tree2-2 AVL-2).
#
# Key Steps & Logic:
# 1. Implemented step-by-step AVL insertion with recursive height updates.
# 2. Detected subtree balance factor violations (|balance| > 1) and output 'Not Balance, Rebalance!'.
# 3. Performed LL, LR, RR, or RL rotations to restore balance and printed the tree structure.
# ================================================================================
