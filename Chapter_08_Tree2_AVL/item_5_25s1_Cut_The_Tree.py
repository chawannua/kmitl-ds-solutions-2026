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
# Prune a whole subtree out of a plain BST, then rebuild BOTH halves as AVL trees.
#
# Core idea:
#   This is not an AVL insert/delete problem. The BST is built unbalanced, one
#   node is chosen as the cut point, and the two resulting pieces are each
#   flattened to a sorted list by an in-order walk and re-inserted into a fresh
#   AVLTree. Balancing happens only in that rebuild step -- the original BST is
#   never rotated.
#
# Key Steps & Logic:
# 1. The input line is split on "/": inp1 is the space-separated list of values
#    for the BST, inp2 is the single key to cut at. BST.insert is a plain
#    recursive BST insert (ties go right), so the shape depends entirely on the
#    order the values arrive in.
#
# 2. search_subtree(root, key) walks down comparing against root.val and returns
#    the NODE that holds the key. Returning the node hands back the entire
#    subtree hanging under it, which is exactly "the cut piece". A key that is
#    not in the tree returns None.
#
# 3. avl1.bst_to_avl(subtree_root) does the rebuild in two moves:
#    a. inorder_traversal returns left + [val] + right, and because the source is
#       a BST that list comes out SORTED.
#    b. Each value is then pushed through AVLTree.insert one at a time.
#    Feeding a sorted list to an ordinary BST would build a straight line, so
#    this is the worst possible input -- and that is the point: every ascending
#    run trips the Right-Right case and gets rotated flat again, so the finished
#    tree is O(log n) tall instead of O(n).
#
# 4. Inside AVLTree.insert, after the recursive call returns, the node refreshes
#    root.height = 1 + max(get_height(left), get_height(right)) and then reads
#    get_balance(root). The refresh has to come AFTER the recursion, because only
#    the unwind carries the child's new height back up; a node measured on the
#    way down would use a stale value. get_height(None) is 0 and a new AVLNode
#    starts at height 1, so height counts nodes on the longest downward path.
#
# 5. get_balance(root) = get_height(root.left) - get_height(root.right).
#    POSITIVE means LEFT-heavy, NEGATIVE means RIGHT-heavy. -1, 0 and +1 are all
#    acceptable: the AVL rule only forbids a two-level gap, and that one level of
#    slack is what keeps the height O(log n) without constant reshaping. A repair
#    fires only when |balance| > 1, and the case is picked from the key just
#    inserted, because that key is what tells you which grandchild subtree grew:
#    * balance > 1  and key < root.left.val   -> LL: one right_rotate(root).
#    * balance < -1 and key > root.right.val  -> RR: one left_rotate(root).
#    * balance > 1  and key > root.left.val   -> LR: the new node hangs off the
#      left child's RIGHT side. A lone right_rotate would just carry that bulge
#      to the other side and leave the node off by 2 again, so
#      root.left = left_rotate(root.left) straightens the zig-zag into a left
#      spine first, then right_rotate(root) lifts it.
#    * balance < -1 and key < root.right.val  -> RL: mirror image;
#      root.right = right_rotate(root.right), then left_rotate(root). One
#      rotation cannot undo a zig-zag.
#    left_rotate/right_rotate each rewire three links and recompute z.height
#    before y.height (y's height depends on the repaired z). That is O(1) work.
#
# 6. delete_subtree(root, key) is a PRUNE, not a BST delete: as soon as
#    root.val == key it returns None, so the parent's link is set to None and the
#    whole subtree disappears together with its children. A normal delete would
#    re-attach those children. This is safe here because it runs only AFTER avl1
#    has already copied the cut values out with its in-order walk.
#
# 7. avl2.bst_to_avl(bst.root) rebuilds whatever is left the same way. Edge cases
#    fall out naturally: a key that is not in the tree gives subtree_root = None,
#    so inorder_traversal returns [] and "Cutted Tree:" prints nothing; cutting
#    at the BST root leaves "Left Tree:" empty.
#
# 8. printTree90 draws a tree rotated 90 degrees counter-clockwise by recursing
#    right-first, so the RIGHT child sits ABOVE its parent and the left child
#    below, 4 spaces of indent per level.
#
# Worked example -- Enter the val of tree and node to cut:
#                   50 30 70 20 40 60 80 35 45/30
#
#   The BST built from those values ("Before cut:"):
#
#              50
#            /    \
#         30        70
#        /  \      /  \
#      20    40  60    80
#           /  \
#         35    45
#
#   Cut at 30 -> in-order of that subtree = [20, 30, 35, 40, 45]. Re-inserting
#   that ascending list fires RR twice (left_rotate at 20 when 35 arrives, and
#   left_rotate at 35 when 45 arrives), giving "Cutted Tree:"
#
#         30
#        /  \
#      20    40
#           /  \
#         35    45
#
#   delete_subtree then sets 50.left = None, so what remains is 50(-, 70(60, 80)).
#   Its in-order is [50, 60, 70, 80]; re-inserting fires one left_rotate at 50
#   when 70 arrives, giving "Left Tree:"
#
#         60
#        /  \
#      50    70
#              \
#               80
# ================================================================================
