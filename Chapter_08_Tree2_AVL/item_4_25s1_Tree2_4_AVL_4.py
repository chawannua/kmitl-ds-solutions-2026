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
# Build an AVL tree, draw it level by level, then repeatedly delete its own root.
#
# Core idea:
#   Both insert() and delete() are ordinary recursive BST operations with the
#   same three-line epilogue: refresh root.height from the children, read
#   balance = getBalance(root), and rotate if the gap is too wide. The epilogue
#   must run AFTER the recursive call returns, because only the unwind carries
#   each child's new height back up; a node that measured itself on the way down
#   would read a stale height. Since the recursion unwinds from the changed leaf
#   to the root, every node on the path is re-checked, lowest first.
#
# Key Steps & Logic:
# 1. main() reads one line of space-separated integers, inserts them in order,
#    and then loops "print the tree, delete root.val" until root becomes None.
#    Because the loop always passes root.val, it drains the tree from the top.
#
# 2. getHeight(None) returns 0 and a new TreeNode starts at height 1, so height
#    counts NODES on the longest downward path.
#
# 3. getBalance(node) = getHeight(node.left) - getHeight(node.right).
#    POSITIVE means LEFT-heavy, NEGATIVE means RIGHT-heavy.
#    -1, 0 and +1 are all fine: the AVL rule only bans a two-level gap between
#    the two sides, and allowing one level of slack is precisely what keeps the
#    height O(log n) while leaving most updates rotation-free. A repair fires
#    only when |balance| > 1.
#
# 4. The four cases in insert() are detected from the KEY, not from the child's
#    balance, because during an insertion the new value itself tells you which
#    grandchild subtree grew:
#    * balance > 1  and val < root.left.val   -> LL: one rotateRight(root).
#    * balance < -1 and val > root.right.val  -> RR: one rotateLeft(root).
#    * balance > 1  and val > root.left.val   -> LR: the new node hangs off the
#      left child's RIGHT side, so a lone rotateRight would just move the bulge
#      across and leave the node off by 2 again. root.left = rotateLeft(root.left)
#      straightens the zig-zag into a left spine first, then rotateRight(root).
#    * balance < -1 and val < root.right.val  -> RL: mirror image;
#      root.right = rotateRight(root.right), then rotateLeft(root). One rotation
#      cannot undo a zig-zag.
#
# 5. delete() repeats the same four cases but CANNOT use the key trick: the value
#    being removed is gone by the time the unwind reaches an ancestor, and a
#    deletion makes a node unbalanced by SHRINKING the side that changed, so the
#    taller side is the one that did not change. It therefore asks the child
#    directly -- getBalance(root.left) >= 0 for LL, < 0 for LR,
#    getBalance(root.right) <= 0 for RR, > 0 for RL. Note the >= / <= : a
#    perfectly balanced child (0) is routed to the single-rotation branch,
#    which is the case that only deletion can produce.
#
# 6. delete() itself: a node with at most one child is replaced by that child
#    (return root.right / root.left). A node with two children copies the value
#    of its in-order successor -- getMinValueNode(root.right), the leftmost node
#    of the right subtree -- into itself and then deletes that successor from the
#    right subtree, which is always the easy 0-or-1-child case.
#
# 7. printTree uses getLevels (a BFS that collects only the nodes that exist) and
#    prints level d with slot_width = 8 * 2 ** (H - 1 - d), so the top level owns
#    the widest slot and each level down halves it. Missing children are skipped
#    rather than padded, so the centring is exact on a full level and the values
#    shift left on a ragged one.
#
# 8. Every rotation is a fixed number of pointer writes plus two height updates,
#    i.e. O(1). Insertion triggers at most one; deletion may trigger one per level
#    on the way up, so both operations stay O(log n).
#
# Worked example -- Enter numbers to insert: 10 20 30 40 50 25
#
#   The ascending run 10,20,30 fires RR at 10; inserting 50 fires RR at node 30;
#   inserting 25 fires RL at the root (balance = -2 and 25 < root.right.val = 40).
#   The first drawing is therefore, with slot widths 32 / 16 / 8:
#
#                30
#        20              40
#    10      25      50
#
#   The loop then deletes 30 (successor 40 takes its place) and next deletes 40.
#   Deleting 40 promotes its successor 50 and unlinks the old 50 node, which
#   leaves the right side one level short:
#
#     before rebalance                         after rotateRight(50)
#            50                                        20
#           /                                         /  \
#         20                                        10    50
#        /  \                                            /
#      10    25                                        25
#
#   getBalance(50) = 2 - 0 = +2 and getBalance(50.left = 20) = 1 - 1 = 0 >= 0, so
#   the LL branch is taken and one rotateRight is enough. The printed levels are
#   "20" / "10  50" / "25", and the loop continues until "===== End of program ====="
# ================================================================================
