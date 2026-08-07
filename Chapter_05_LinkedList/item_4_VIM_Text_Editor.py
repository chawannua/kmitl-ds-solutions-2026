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
# This Python script solves Chapter 5 Item 4 (VIM Text Editor).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================