# ================================================================================
# Chapter 7 - Item 5: 25s1 Expression Tree
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Python program to accept a postfix mathematical expression and construct the corresponding expression tree using +, -, *, /, displaying the tree and prefix/infix expressions.
# ================================================================================

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print('     ' * level, node.val)
        printTree(node.left, level + 1)


def to_infix(node):
    if node is None:
        return ""
    if node.left is None and node.right is None:
        return node.val
    return f"({to_infix(node.left)}{node.val}{to_infix(node.right)})"


def to_prefix(node):
    if node is None:
        return ""
    return f"{node.val}{to_prefix(node.left)}{to_prefix(node.right)}"


postfix = input("Enter Postfix : ")
stack = []
for ch in postfix:
    if ch in "+-*/":
        r = stack.pop()
        l = stack.pop()
        n = Node(ch)
        n.left = l
        n.right = r
        stack.append(n)
    else:
        stack.append(Node(ch))

root = stack.pop()
print("Tree :")
printTree(root)
print("--------------------------------------------------")
print("Infix :", to_infix(root))
print("Prefix :", to_prefix(root))

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 7 Item 5 (25s1 Expression Tree).
#
# Key Steps & Logic:
# 1. Scanned postfix expression token by token using an expression tree node stack.
# 2. For operators (+, -, *, /), popped two operands to form subtrees and pushed back the operator node.
# 3. Printed the expression tree in 2D representation along with infix/prefix traversals.
# ================================================================================
