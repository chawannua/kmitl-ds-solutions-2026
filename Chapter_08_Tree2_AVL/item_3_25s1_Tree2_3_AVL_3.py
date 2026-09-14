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
# Same AVL insertion as item 2, but every repair announces WHICH rotation it used.
#
# Core idea:
#   insert() is a recursive BST insert with a two-line epilogue that runs while
#   the recursion unwinds: refresh root.height from the children, then read
#   balance = getBalance(root). The height must be recomputed AFTER the recursive
#   call returns, because only then does the child on the insertion path carry
#   its new height; measuring before recursing would read a stale value. Unwinding
#   bottom-up also means the LOWEST node that breaks the rule is the one that gets
#   fixed, and fixing it usually restores the original subtree height so the
#   ancestors above need nothing.
#
# Key Steps & Logic:
# 1. The driver splits the input on whitespace, and for each value prints
#    "insert : <e>", the rotation name (only if one happened), the redrawn tree,
#    and a separator.
#
# 2. getHeight(None) returns 0 and a new TreeNode starts at height 1, so height
#    counts NODES on the longest downward path.
#
# 3. getBalance(node) = getHeight(node.left) - getHeight(node.right).
#    POSITIVE means LEFT-heavy, NEGATIVE means RIGHT-heavy.
#    -1, 0 and +1 are legal; the AVL invariant only forbids a two-level gap, and
#    tolerating one level is exactly what makes the height stay O(log n) while
#    keeping insertion cheap. A repair fires only when |balance| > 1.
#
# 4. The four cases as written, with the string this file prints for each:
#    * Case 1, balance > 1 and getBalance(root.left) >= 0
#      -> prints "Right Right Rotation", performs ONE rotateRight(root).
#         This is the classic Left-Left shape: the left child leans left (or is
#         level), so the deep part is a straight left spine.
#    * Case 2, balance > 1 and getBalance(root.left) < 0
#      -> prints "Left Right Rotation": root.left = rotateLeft(root.left), then
#         rotateRight(root). The extra depth hangs off the left child's RIGHT
#         side. A single rotateRight would merely carry that bulge to the other
#         side and leave the node off by 2 again, so the zig-zag has to be
#         straightened into a left spine first.
#    * Case 3, balance < -1 and getBalance(root.right) <= 0
#      -> prints "Left Left Rotation", performs ONE rotateLeft(root).
#         This is the classic Right-Right shape, the mirror of Case 1.
#    * Case 4, balance < -1 and getBalance(root.right) > 0
#      -> prints "Right Left Rotation": root.right = rotateRight(root.right),
#         then rotateLeft(root). Mirror of Case 2; one rotation cannot undo a
#         zig-zag.
#    Note the naming used by this exercise: the labels for the two SINGLE
#    rotations describe the direction the subtree is turned, not the insertion
#    pattern, so the Left-Left insertion prints "Right Right Rotation" and the
#    Right-Right insertion prints "Left Left Rotation". The in-code comments spell
#    both readings out.
#
# 5. rotateLeft/rotateRight each rewire three links (y, the orphan T2 or T3, and
#    z) and then set z.height before y.height, since y's height depends on the
#    repaired z. That is O(1) pointer work, and an insertion triggers at most one
#    repair, so an insert costs O(log n) and the height stays O(log n).
#
# 6. printTree90 recurses right-first, so the RIGHT child is drawn ABOVE its
#    parent and the left child below, 5 spaces of indent per level.
#
# Worked example -- Enter Input : 30 20 10 40 50 45
#
#   insert 10: getBalance(30) = 2 - 0 = +2 and getBalance(20) = 1 - 0 = +1 >= 0,
#   so Case 1 fires and the program prints "Right Right Rotation".
#
#     before                                   after rotateRight(30)
#          30                                          20
#         /                                           /  \
#       20                                          10    30
#       /
#     10
#
#   insert 50: the tree is 20(10, 30(-, 40)) and 50 lands under 40. The root is
#   fine (getBalance(20) = -1); it is node 30 that breaks:
#   getBalance(30) = 0 - 2 = -2 and getBalance(40) = 0 - 1 = -1 <= 0 -> Case 3,
#   printing "Left Left Rotation".
#
#     before                                   after rotateLeft(30)
#          20                                          20
#         /  \                                        /  \
#       10    30                                    10    40
#               \                                        /  \
#                40                                    30    50
#                  \
#                   50
#
#   The fix is applied at 30, the lowest ancestor that broke the rule; once that
#   subtree is back to its pre-insert height, 20 needs no work at all.
#
#   insert 45: Case 3 again, this time at the root, ending with
#   40(20(10, 30), 50(45, -)).
# ================================================================================
