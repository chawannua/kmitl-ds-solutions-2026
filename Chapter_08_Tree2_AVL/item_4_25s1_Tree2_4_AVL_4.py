# ================================================================================
# Chapter 8 - Item 4: 25s1 Tree2-4 AVL-4
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a program that builds an AVL tree by inserting integers in order. Print the AVL tree in a structured level-by-level format. Then continuously remove the root node and print the resulting tree until empty.
# ================================================================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)


class AVLTree:
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

    def insert(self, root, val):
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Left Left
        if balance > 1 and val < root.left.val:
            return self.rotateRight(root)

        # Right Right
        if balance < -1 and val > root.right.val:
            return self.rotateLeft(root)

        # Left Right
        if balance > 1 and val > root.left.val:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Right Left
        if balance < -1 and val < root.right.val:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def getMinValueNode(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def delete(self, root, val):
        if not root:
            return root

        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if not root:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)

        # Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)

        # Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def getLevels(self, root):
        if not root:
            return []
        levels = []
        q = [root]
        while q:
            levels.append([node.val for node in q])
            next_q = []
            for node in q:
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            q = next_q
        return levels

    def printTree(self, root):
        levels = self.getLevels(root)
        if not levels:
            return
        H = len(levels)
        for d, level in enumerate(levels):
            slot_width = 8 * (2 ** (H - 1 - d))
            print("".join(str(val).center(slot_width) for val in level))


def main():
    print(" *** AVL Tree ***")
    raw_input = input("Enter numbers to insert: ")
    if not raw_input.strip():
        print("===== End of program =====")
        return

    nums = [int(x) for x in raw_input.split()]
    tree = AVLTree()
    root = None
    for x in nums:
        root = tree.insert(root, x)

    while root:
        tree.printTree(root)
        print("------------------------------")
        root = tree.delete(root, root.val)

    print("===== End of program =====")


if __name__ == "__main__":
    main()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 8 Item 4 (25s1 Tree2-4 AVL-4).
#
# Key Steps & Logic:
# 1. Built an AVL tree with centered level-order formatting (dynamic slot width = 8 * 2^(height - 1 - level)).
# 2. Continuously popped the root node, replaced it with the in-order successor (minimum of right subtree), and performed AVL bottom-up rebalancing.
# 3. Printed level layout after each deletion until tree became empty.
# ================================================================================
