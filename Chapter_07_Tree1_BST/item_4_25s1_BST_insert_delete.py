# ================================================================================
# Chapter 7 - Item 4: 25s1 BST insert / delete
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Python program to accept a sequence of commands to construct and modify
# a Binary Search Tree (BST):
#   - i <int> : Insert data into BST
#   - d <int> : Delete data from BST
# If deleting a value that is not found in the BST, display "Error! Not Found DATA".
# After each operation, display the operation and print the BST sideways (90 degrees).
#
# Inputs:
#   - Comma-separated list of commands (e.g. "i 3,i 5,i 2,d 3")
# Outputs:
#   - Printed operation name and 90-degree sideways tree visualization after each step.
# ================================================================================

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 


class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            curr = self.root
            while True:
                if val < curr.data:
                    if curr.left is None:
                        curr.left = Node(val)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(val)
                        break
                    else:
                        curr = curr.right
        return self.root

    def _delete_node(self, r, data):
        """Helper to recursively delete a node without triggering 'Not Found' error."""
        if r is None:
            return None
        if data < r.data:
            r.left = self._delete_node(r.left, data)
        elif data > r.data:
            r.right = self._delete_node(r.right, data)
        else:
            if r.left is None:
                return r.right
            elif r.right is None:
                return r.left
            else:
                curr = r.right
                while curr.left is not None:
                    curr = curr.left
                r.data = curr.data
                r.right = self._delete_node(r.right, curr.data)
        return r

    def delete(self, r, data):
        """Delete a node with value `data` from subtree rooted at `r`."""
        if r is None:
            print("Error! Not Found DATA")
            return None
        
        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                return r.right
            elif r.right is None:
                return r.left
            else:
                # Node with two children: replace with in-order successor
                curr = r.right
                while curr.left is not None:
                    curr = curr.left
                r.data = curr.data
                r.right = self._delete_node(r.right, curr.data)
        return r

                
def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for cmd in data:
    parts = cmd.strip().split()
    op = parts[0]
    val = int(parts[1])
    if op == 'i':
        print(f"insert {val}")
        tree.insert(val)
        printTree90(tree.root)
    elif op == 'd':
        print(f"delete {val}")
        tree.root = tree.delete(tree.root, val)
        printTree90(tree.root)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Command-driven BST supporting insert (i) and all three classic BST
# deletion cases (d), reprinting the sideways tree after every command.
#
# BST invariant: enforced by "val < curr.data -> left, else -> right" in
# insert(), and mirrored by "data < r.data" / "data > r.data" in
# delete()/_delete_node().
#
# Key Steps & Logic:
# 1. Each comma-separated command ("i 3", "d 3", ...) is split into an
#    operation letter (op) and an integer value (val).
# 2. "i <val>" calls insert(val): walk down from the root comparing val to
#    curr.data until an empty child slot is found, then attach a new leaf.
# 3. "d <val>" calls delete(tree.root, val), which recurses down comparing
#    data to r.data. Falling off the tree (r is None) prints
#    "Error! Not Found DATA". Once the target node is found there are
#    three cases, all decided by the same if/elif/else block:
#      - Leaf / 0 children: r.left and r.right are both None, so
#        "if r.left is None: return r.right" returns None, unlinking it.
#      - 1 child: exactly one side is None, so "if r.left is None: return
#        r.right" (or the mirrored elif) splices that single child up in
#        place of the deleted node.
#      - 2 children: neither branch fires, so the else-block walks
#        curr = r.right, then curr = curr.left repeatedly until
#        curr.left is None. That curr is the INORDER SUCCESSOR (the
#        smallest value in the right subtree). Copying curr.data into
#        r.data keeps r's right subtree still >= r.data and r's left
#        subtree still < r.data, so the invariant survives. The now
#        duplicate successor leaf is then removed from the right subtree
#        via the helper _delete_node (same three cases, without the
#        "Error! Not Found DATA" message).
# 4. printTree90(tree.root) is called after every command to redraw the
#    sideways tree (right, node, left) so each step's effect is visible.
#
# Worked example -- Enter Input : i 3,i 5,i 2,d 3
#   insert 3 -> root:        3
#   insert 5 (>=3, right):   3
#                             \
#                              5
#   insert 2 (<3, left):     3
#                           /  \
#                          2    5
#   delete 3: node 3 has two children. curr starts at r.right (node 5);
#   curr.left is already None, so curr stops immediately at 5 -- the
#   inorder successor is 5 itself. r.data becomes 5, then _delete_node
#   removes the now-duplicate leaf 5 from the right subtree, leaving:
#         5
#        /
#       2
#   Program prints after "delete 3":
#        5
#   2
# ================================================================================
