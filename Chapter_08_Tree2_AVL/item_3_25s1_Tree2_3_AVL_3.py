# ================================================================================
# Chapter 8 - Item 3: 25s1 Tree2-3 AVL-3
# --------------------------------------------------------------------------------
# Problem Statement:
# Show the rotation during inserting node in AVLTree. Displays the tree structure after each insertion and prints the name of the rotation performed.
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

        # Case 1 - Right Right Rotation (Left-heavy, Left-Left insertion)
        if balance > 1 and self.getBalance(root.left) >= 0:
            print("Right Right Rotation")
            return self.rotateRight(root)

        # Case 2 - Left Right Rotation (Left-heavy, Left-Right insertion)
        if balance > 1 and self.getBalance(root.left) < 0:
            print("Left Right Rotation")
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Case 3 - Left Left Rotation (Right-heavy, Right-Right insertion)
        if balance < -1 and self.getBalance(root.right) <= 0:
            print("Left Left Rotation")
            return self.rotateLeft(root)

        # Case 4 - Right Left Rotation (Right-heavy, Right-Left insertion)
        if balance < -1 and self.getBalance(root.right) > 0:
            print("Right Left Rotation")
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

print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("====================")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 8 Item 3 (25s1 Tree2-3 AVL-3).
#
# Key Steps & Logic:
# 1. Maintained AVL balance through node insertions.
# 2. When unbalance is detected, identified the specific rotation type: 'Left Left Rotation', 'Right Right Rotation', 'Left Right Rotation', or 'Right Left Rotation'.
# 3. Rebalanced tree pointers, updated node heights, and displayed tree hierarchy.
# ================================================================================
