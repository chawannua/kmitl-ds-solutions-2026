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
# Step-by-step AVL insertion that reports every rebalance and redraws the tree.
#
# Core idea:
#   insert() is an ordinary recursive BST insert with two extra lines on the way
#   back out. Once the recursive call has returned, the current node refreshes
#   root.height = 1 + max(getHeight(root.left), getHeight(root.right)) and then
#   reads balance = getBalance(root). The order matters: the child on the
#   insertion path only gets its new height while the recursion unwinds, so a
#   parent that measured itself BEFORE recursing would use a stale height. Going
#   bottom-up means every node is repaired before its parent looks at it.
#
# Key Steps & Logic:
# 1. The driver splits the input on whitespace and feeds one value per round,
#    printing "insert : <e>", then the tree, then a separator, so each line of
#    output is a snapshot of the tree after exactly one insertion.
#
# 2. getHeight(None) returns 0 and TreeNode starts at height 1, so height counts
#    NODES on the longest downward path, not edges.
#
# 3. getBalance(node) = getHeight(node.left) - getHeight(node.right).
#    POSITIVE means LEFT-heavy, NEGATIVE means RIGHT-heavy.
#    -1, 0 and +1 are all acceptable: the AVL rule only requires the two sides to
#    differ by at most one level, and that slack is what keeps the height
#    O(log n) without rebuilding the tree. A repair fires only when
#    |balance| > 1, i.e. one side is two full levels taller.
#
# 4. The four cases, written exactly as in insert(). Each one prints
#    "Not Balance, Rebalance!" from the deepest node that broke the rule, which
#    is why the message appears before the redrawn tree.
#    * Case 1, balance > 1 and getBalance(root.left) >= 0   -> LL
#      The left child is itself left-heavy or level, so the deep path is a
#      straight left spine: one rotateRight(root) lifts it.
#    * Case 2, balance > 1 and getBalance(root.left)  < 0   -> LR
#      The extra depth hangs off the left child's RIGHT side, a zig-zag. A lone
#      rotateRight(root) would push that bulge over to the other side and leave
#      the node off by 2 again, so root.left = rotateLeft(root.left) first turns
#      the zig-zag into a straight left spine, then rotateRight(root) applies.
#    * Case 3, balance < -1 and getBalance(root.right) <= 0 -> RR
#      Mirror of Case 1: a single rotateLeft(root).
#    * Case 4, balance < -1 and getBalance(root.right)  > 0 -> RL
#      Mirror of Case 2: root.right = rotateRight(root.right), then
#      rotateLeft(root). One rotation alone cannot straighten a zig-zag.
#
# 5. rotateLeft/rotateRight each move three pointers (y, the orphan subtree T2 or
#    T3, and z) and then recompute z.height before y.height, because y's height
#    depends on the repaired z. That is O(1) work, and insertion triggers at most
#    one repair, so an insert costs O(log n) and the height stays O(log n).
#
# 6. printTree90 prints the tree rotated 90 degrees counter-clockwise: it recurses
#    right first, so the RIGHT child appears ABOVE its parent and the left child
#    below, with indentation of 5 spaces per level standing in for depth.
#
# Worked example -- Enter Input : 10 20 30 40 50 25
#
#   insert 30: getBalance(10) = 0 - 2 = -2 and getBalance(20) = 0 - 1 = -1 <= 0,
#   so Case 3 (RR) fires at the root.
#
#     before                                   after rotateLeft(10)
#       10                                            20
#         \                                          /  \
#          20                                      10    30
#            \
#             30
#
#   insert 50: same Case 3, this time at node 30, giving  20(10, 40(30, 50)).
#
#   insert 25: 25 lands under 30. getBalance(20) = 1 - 3 = -2 (right-heavy) and
#   getBalance(20.right = 40) = 2 - 1 = +1 > 0, so Case 4 (RL) fires. The bulge
#   sits on the LEFT of the right child, so a lone rotateLeft(20) would swing 40
#   up and drop 10 one level deeper, tilting the tree by 2 the other way.
#
#     before                  step 1: rotateRight(40)   step 2: rotateLeft(20)
#          20                      20                         30
#         /  \                    /  \                       /  \
#       10    40                10    30                   20    40
#            /  \                    /  \                 /  \     \
#          30    50                25    40             10    25    50
#         /                                \
#       25                                  50
#
#   Final drawing printed for that round (right child on top):
#            50
#       40
#  30
#            25
#       20
#            10
# ================================================================================
