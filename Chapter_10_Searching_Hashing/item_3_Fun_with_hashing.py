# ================================================================================
# Chapter 10 - Item 3: Fun with hashing
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Hashing program with the following operations:
# - Table index = (sum of ASCII values of the key) mod (table size).
# - On collision, shift the index using Quadratic Probing.
# - If collisions reach the MaxCollision limit, discard that Data immediately.
# - When the table is full, display "This table is full !!!!!!" (only once).
#
# Inputs:
# - "<table size> <MaxCollision>/<key value>,<key value>,..."
#   e.g. 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
# Outputs:
# - The table after every successful insert, "collision number N at IDX" for
#   each collision, "Max of collisionChain" when Data is discarded.
# ================================================================================

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, size, max_col):
        self.size = size
        self.max_col = max_col
        self.table = [None] * size
        self.count = 0

    def ascii_sum(self, key):
        return sum(ord(c) for c in key)

    def print_table(self):
        for i in range(self.size):
            print(f"#{i+1}\t{self.table[i]}")
        print("---------------------------")

    def insert(self, key, val):
        if self.count == self.size:
            return

        h = self.ascii_sum(key) % self.size
        col = 0
        while col < self.max_col:
            # Quadratic probing: h, h+1, h+4, h+9, ...
            idx = (h + col * col) % self.size
            if self.table[idx] is None:
                self.table[idx] = Data(key, val)
                self.count += 1
                self.print_table()
                if self.count == self.size:
                    print("This table is full !!!!!!")
                return
            else:
                col += 1
                print(f"collision number {col} at {idx}")

        # Too many collisions: discard this Data
        print("Max of collisionChain")
        self.print_table()

print(" ***** Fun with hashing *****")
inp = input('Enter Input : ').split('/')
table_size, max_collision = map(int, inp[0].split())
data_entries = inp[1].split(',')

h = hash(table_size, max_collision)
for item in data_entries:
    parts = item.split()
    if len(parts) >= 2:
        k, v = parts[0], parts[1]
        h.insert(k, v)
        # Stop once full so the "full" message appears only once
        if h.count == h.size:
            break

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# 1. Home index h = sum(ord(c) for c in key) % size.
# 2. Try h + 0^2, h + 1^2, h + 2^2, ... (mod size). Each occupied slot prints
#    "collision number <col> at <idx>".
# 3. First empty slot wins: store Data(key, value) and print the table.
# 4. If max_col collisions happen first, print "Max of collisionChain" and the
#    unchanged table (the Data is dropped).
# 5. After the table fills, print "This table is full !!!!!!" and stop reading
#    further input so the message is printed exactly once.
#
# Worked example -- Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,...
#   "1+1" -> slot 0.  "OnE" collides at 0, lands at 1.
#   "abcde" collides at 0 and 1 -> 2 collisions = max -> discarded.
#   "#$ew2" -> slot 2 -> table full -> message printed, input ends.
# ================================================================================
