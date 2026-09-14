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
# A command-driven AVL tree whose node objects cache and refresh their own height.
#
# Core idea:
#   Every AVLNode stores self.height. When a recursive _add() call returns, the
#   node that is unwinding calls setHeight() to recompute
#   1 + max(getHeight(left), getHeight(right)) from its now-updated children, and
#   only then asks balanceValue() whether it may keep its shape. The refresh has
#   to happen AFTER the recursive call: before it, the child on the insertion
#   path still carries its old height, so the parent would compute a stale value.
#   Unwinding bottom-up guarantees each child is already correct.
#
# Key Steps & Logic:
# 1. Input is one comma-separated command list. i[:2] is the opcode and i[3:] the
#    payload, so "AD 30" adds 30, "PR" draws the tree sideways via printTree, and
#    "PO" prints the post-order walk via postOrder.
#
# 2. getHeight(node) returns -1 for None, so a leaf has height 0. Both rotation
#    helpers finish by calling setHeight() on the demoted node FIRST and on the
#    promoted node second, because the new subtree root's height is computed from
#    the old root's freshly repaired height.
#
# 3. balanceValue() = getHeight(self.right) - getHeight(self.left).
#    NEGATIVE means LEFT-heavy, POSITIVE means RIGHT-heavy. This is the reverse
#    of the convention used by items 2-5 in this chapter, so check the sign
#    before reusing the code. Values of -1, 0 and +1 are all accepted: an AVL
#    tree only promises the two sides differ by at most one level, and that
#    single level of slack is already enough to bound the height at O(log n).
#    Only |balance| > 1 forces a repair.
#
# 4. The rotation helpers are named after the child they promote, not after the
#    direction of travel:
#      rotateLeftChild(root)  -> root.left  becomes the new root (a right rotation)
#      rotateRightChild(root) -> root.right becomes the new root (a left rotation)
#    Each rewires exactly three links and returns the new subtree root, which the
#    caller assigns back into root.left / root.right / self.root.
#
# 5. The four repair cases, exactly as _add() tests them:
#    * balance < -1 and root.left.balanceValue() <= 0    -> LL
#      The left child leans left (or is level), so the deep part is a straight
#      left spine: one rotateLeftChild(root) lifts it by a level.
#    * balance < -1 and root.left.balanceValue()  > 0    -> LR
#      The extra depth hangs off the left child's RIGHT side. A lone
#      rotateLeftChild would just carry that bulge across to the other side and
#      leave the node tilted by 2 again, so the code first straightens the
#      zig-zag with root.left = rotateRightChild(root.left), then applies
#      rotateLeftChild(root).
#    * balance > 1 and root.right.balanceValue() >= 0    -> RR
#      Mirror of LL: a single rotateRightChild(root).
#    * balance > 1 and root.right.balanceValue()  < 0    -> RL
#      Mirror of LR: root.right = rotateLeftChild(root.right) turns the zig-zag
#      into a straight right spine, then rotateRightChild(root) finishes it.
#      One rotation cannot fix a zig-zag, for the same reason as LR.
#    A rotation is a fixed number of pointer writes plus two setHeight() calls,
#    i.e. O(1), and an insert triggers at most one of them, so add() is O(log n)
#    and the tree height stays O(log n).
#
# Worked example -- Enter Input : AD 30,AD 20,AD 10,AD 25,AD 40,AD 35,PO
#
#   After "AD 10": balanceValue(30) = -1 - 1 = -2 (left-heavy) and
#   balanceValue(20) = -1 - 0 = -1 <= 0, so this is LL.
#
#     before                                   after rotateLeftChild(30)
#          30                                          20
#         /                                           /  \
#       20                                          10    30
#       /
#     10
#
#   After "AD 35": 35 lands under 40. balanceValue(20) = 2 - 0 = +2 (right-heavy)
#   and balanceValue(30) = 1 - 0 = +1 >= 0, so this is RR.
#
#     before                                   after rotateRightChild(20)
#          20                                          30
#         /  \                                        /  \
#       10    30                                    20    40
#            /  \                                  /  \   /
#          25    40                              10    25 35
#               /
#             35
#
#   "PO" then prints:  AVLTree post-order : 10 25 20 35 40 30
# ================================================================================
