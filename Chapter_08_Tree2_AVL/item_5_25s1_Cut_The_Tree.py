# ================================================================================
# Chapter 8 - Item 5: 25s1 Cut The Tree
# --------------------------------------------------------------------------------
# Problem Statement:
# Cut a Binary Search Tree (BST) into two subtrees: the extracted subtree pruned from a target node, and the remaining left tree. Then convert both subtrees into balanced AVL Trees.
# ================================================================================

class BST:
    class BSTNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, root=None) -> None:
        self.root = root

    def get_successor(self, curr):
        node = curr.right
        while node and node.left:
            node = node.left
        return node

    def search_subtree(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search_subtree(root.left, key)
        return self.search_subtree(root.right, key)

    def insert(self, root, key):
        if root is None:
            return self.BSTNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def delete_subtree(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return None
        if key < root.val:
            root.left = self.delete_subtree(root.left, key)
        else:
            root.right = self.delete_subtree(root.right, key)
        return root

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent, root.val)
            self.printTree90(root.left, indent + 1)


class AVLTree:
    class AVLNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
            self.height = 1  # Height of the node

    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, root, key):
        if not root:
            return self.AVLNode(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def bst_to_avl(self, bst_root):
        # Convert BST to sorted list via in-order traversal
        sorted_values = self.inorder_traversal(bst_root)

        # Insert elements into the AVL tree
        for val in sorted_values:
            self.root = self.insert(self.root, val)

    def inorder_traversal(self, root):
        # Helper function to perform in-order traversal and return a sorted list
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.val]
            + self.inorder_traversal(root.right)
        )

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)


inp1, inp2 = input(
    "Enter the val of tree and node to cut: "
).split("/")
bst = BST()
for i in inp1.split():
    bst.root = bst.insert(bst.root, int(i))
print("Before cut:")
bst.printTree90(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

# Convert the found subtree into an AVL tree
print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
avl1.bst_to_avl(subtree_root)
avl1.printTree90(avl1.root)

# Convert the remaining BST (after deletion) into an AVL tree
print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
avl2.bst_to_avl(bst.root)
avl2.printTree90(avl2.root)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 8 Item 5 (25s1 Cut The Tree).
#
# Key Steps & Logic:
# 1. Built the initial Binary Search Tree (BST) from space-separated integers.
# 2. Searched for the target node subtree and pruned it from the main BST (delete_subtree).
# 3. Converted both subtrees into AVL Trees via in-order traversal and sequential AVL insertions, then printed the resulting structures.
# ================================================================================
