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
# Builds an expression tree from a POSTFIX string using a node stack, then
# prints it sideways and derives infix/prefix by choosing traversal order.
#
# Key Steps & Logic:
# 1. The input string is scanned one character at a time (no tokenizing or
#    spaces needed, since every operand here is a single character).
#    Operands (any char not in "+-*/") are pushed as leaf Nodes:
#    "stack.append(Node(ch))".
# 2. Each operator character pops the two most recently pushed items as its
#    operands: r = stack.pop() (the right operand) then l = stack.pop()
#    (the left operand) -- this is exactly postfix evaluation order, so
#    operators always become INTERNAL nodes and operands always end up as
#    LEAVES. The popped l/r become n.left/n.right and the new subtree is
#    pushed back for a later operator to consume.
# 3. After the scan, exactly one item remains on the stack: the root of
#    the full expression tree.
# 4. printTree(node, level) reuses the right-node-left sideways layout from
#    Chapter 7 Item 1 (5-space indent per depth level).
# 5. to_infix(node) is an inorder walk (left, node, right) that wraps every
#    internal node's result in parentheses: "({left}{val}{right})" -- the
#    parentheses are what recover the original operator grouping.
# 6. to_prefix(node) is a preorder walk (node, left, right) with no
#    parentheses, since prefix notation does not need them to stay
#    unambiguous.
#
# Worked example -- Enter Postfix : AB+C*
#   Scan: 'A' -> push leaf A.  'B' -> push leaf B.
#   '+'  -> pop B (r), pop A (l) -> node "+" (left=A, right=B); push it.
#   'C'  -> push leaf C.
#   '*'  -> pop C (r), pop the "+" node (l) -> node "*" (left=+, right=C);
#   push it. Only the root remains on the stack.
#
#           *
#          / \
#         +   C
#        / \
#       A   B
#
#   printTree (right-node-left) produces this actual console output:
#         C
#    *
#              B
#         +
#              A
#   to_infix(root)  -> Infix : ((A+B)*C)
#   to_prefix(root) -> Prefix : *+ABC
# ================================================================================
