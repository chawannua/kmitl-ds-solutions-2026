# ================================================================================
# Chapter 5 - Item 4: VIM Text Editor
# --------------------------------------------------------------------------------
# Problem Statement:
# Kritsada had a brilliant idea to create his own Text Editor similar to VIM, which operates in a single mode called Command Mode (our input). The program includes 5 commands: Insert (I), Left (L), Right (R), Backspace (B), and Delete (D). (The functionality of each command is explained below.) However, Kritsada lacks programming skills, so he requested help from computer engineering students to develop the Text Editor he envisioned. The output should display the remaining word after executing the commands and the position of the cursor.
# Explanation of the 5 Input Commands:I <word>: Inserts the word at the current cursor position. After inserting the word, the cursor moves to the end of the inserted word.
# L: Moves the cursor one position to the left. If the cursor is already at the leftmost position, nothing happens.
# R: Moves the cursor one position to the right. If the cursor is already at the rightmost position, nothing happens.
# B: Deletes the character to the left of the cursor. If the cursor is already at the leftmost position, nothing happens.
# D: Deletes the character to the right of the cursor. If the cursor is already at the rightmost position, nothing happens.
# ================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class TextEditor:
    def __init__(self):
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.cursor = self.dummy_head

    def insert(self, word):
        new_node = Node(word)
        new_node.next = self.cursor.next
        new_node.prev = self.cursor
        self.cursor.next.prev = new_node
        self.cursor.next = new_node
        self.cursor = new_node

    def left(self):
        if self.cursor != self.dummy_head:
            self.cursor = self.cursor.prev

    def right(self):
        if self.cursor.next != self.dummy_tail:
            self.cursor = self.cursor.next

    def backspace(self):
        if self.cursor != self.dummy_head:
            to_delete = self.cursor
            self.cursor = self.cursor.prev
            self.cursor.next = to_delete.next
            to_delete.next.prev = self.cursor

    def delete(self):
        if self.cursor.next != self.dummy_tail:
            to_delete = self.cursor.next
            self.cursor.next = to_delete.next
            to_delete.next.prev = self.cursor

    def __str__(self):
        s = ""
        cur = self.dummy_head
        while cur:
            if cur != self.dummy_head and cur != self.dummy_tail:
                s += str(cur.data) + " "
            if cur == self.cursor:
                s += "| "
            cur = cur.next
        return s

if __name__ == "__main__":
    inp = input("Enter Input : ").split(',')
    editor = TextEditor()
    
    for cmd in inp:
        cmd = cmd.strip()
        if cmd.startswith('I'):
            parts = cmd.split(' ', 1)
            if len(parts) > 1:
                editor.insert(parts[1])
        elif cmd == 'L':
            editor.left()
        elif cmd == 'R':
            editor.right()
        elif cmd == 'B':
            editor.backspace()
        elif cmd == 'D':
            editor.delete()
            
    print(editor)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Doubly linked list with two SENTINEL nodes (dummy_head, dummy_tail) that are
# never removed; the cursor is just a Node reference sitting "on" the
# character it is positioned after.
#
# Core idea:
#   self.cursor always points at the node the caret sits immediately AFTER
#   (dummy_head means "before the first real character"). Every command is
#   just a pointer move (L/R) or a small 4-link splice (I/B/D) relative to
#   self.cursor -- there is no index math and no shifting of a Python list.
#
# Key Steps & Logic:
# 1. insert(word): splice a new node right after self.cursor, THEN move the
#    cursor onto it (so typing continues after the inserted text):
#      new_node.next = self.cursor.next
#      new_node.prev = self.cursor
#      self.cursor.next.prev = new_node   (fix the node ahead first...)
#      self.cursor.next = new_node        (...before cursor.next is overwritten)
#      self.cursor = new_node
#    Reading self.cursor.next.prev before overwriting self.cursor.next
#    matters: swap those two lines and the "node ahead" link would be lost.
#
# 2. left()/right(): pure pointer walks (cursor = cursor.prev / cursor.next)
#    guarded by comparing against the sentinels, so the cursor can never step
#    onto or past dummy_head/dummy_tail -- that's what "nothing happens at
#    the edge" means, with no extra empty-list special case needed.
#
# 3. backspace() removes the node the cursor is ON (deletes to the left of
#    where typing continues) and MUST move the cursor first:
#      to_delete = self.cursor; self.cursor = self.cursor.prev
#      self.cursor.next = to_delete.next
#      to_delete.next.prev = self.cursor
#    Moving the cursor before rewriting links is required -- otherwise
#    self.cursor.next would rewrite to_delete's own link instead of the
#    node before it, corrupting the chain.
#
# 4. delete() removes cursor.next (to the right) WITHOUT moving the cursor,
#    since deleting ahead doesn't change what the caret sits after; it only
#    rewires the two links around the removed node.
#
# 5. __str__ walks from dummy_head, printing each real node's data, and
#    prints "| " right after whichever node equals self.cursor -- so the "|"
#    in the output IS the cursor position, not decoration.
#
# Worked example -- Enter Input : I ab,I cd,L,B,D
#   I ab -> insert after dummy_head, cursor -> ab
#           dummy_head -> [ab] -> dummy_tail
#   I cd -> insert after ab, cursor -> cd
#           dummy_head -> [ab] -> [cd] -> dummy_tail
#   L    -> cursor = cursor.prev -> back to [ab]
#   B    -> backspace deletes the node cursor sits on ([ab]):
#           cursor moves to dummy_head first, then dummy_head.next = cd
#           dummy_head -> [cd] -> dummy_tail        (ab removed)
#   D    -> delete removes cursor.next ([cd]):
#           dummy_head -> dummy_tail                (cd removed, list empty)
#   Output: "|"   (cursor sits at dummy_head, no characters remain)
# ================================================================================