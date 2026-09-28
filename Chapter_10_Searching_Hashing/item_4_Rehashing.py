# ================================================================================
# Chapter 10 - Item 4: Rehashing
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Hashing program for integers with Quadratic Probing that rehashes:
# - Table index = value mod (table size).
# - On collision, shift the index using Quadratic Probing.
# - Rehash when inserting would push the load above the threshold (%), or when
#   collisions reach the MaxCollision limit.
# - New table size = the first prime number greater than 2 * old size.
# (The portal's statement text is copied from item 3; the rules above are
#  taken from the portal's test cases.)
#
# Inputs:
# - "<table size> <MaxCollision> <threshold %>/<values separated by spaces>"
#   e.g. 5 1 67/1 6
# Outputs:
# - The initial table, then for every value: "Add : v", any collision lines,
#   any rehash message, and the resulting table.
# ================================================================================

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    p = n + 1
    while not is_prime(p):
        p += 1
    return p

class Rehashing:
    def __init__(self, size, max_col, threshold):
        self.size = size
        self.max_col = max_col
        self.threshold = threshold
        self.table = [None] * size
        self.data_list = []

    def print_table(self):
        for i in range(self.size):
            print(f"#{i+1}\t{self.table[i]}")
        print("----------------------------------------")

    def is_over_threshold(self, count):
        return (count / self.size * 100) > self.threshold

    def insert_into_table(self, table, size, val, max_col):
        h = val % size
        col = 0
        while col < max_col:
            # Quadratic probing: h, h+1, h+4, h+9, ...
            idx = (h + col * col) % size
            if table[idx] is None:
                table[idx] = val
                return True
            else:
                col += 1
                print(f"collision number {col} at {idx}")
        return False

    def rehash(self, new_val, reason):
        if reason == "threshold":
            print("****** Data over threshold - Rehash !!! ******")
        elif reason == "max_col":
            print("****** Max collision - Rehash !!! ******")

        # Re-insert every stored value (in original order) plus the new one
        all_vals = self.data_list + [new_val]

        while True:
            new_size = next_prime(self.size * 2)
            self.size = new_size
            new_table = [None] * new_size

            rehash_failed = False
            for v in all_vals:
                success = self.insert_into_table(new_table, self.size, v, self.max_col)
                if not success:
                    # Still too many collisions -> grow again
                    rehash_failed = True
                    print("****** Max collision - Rehash !!! ******")
                    break
            if not rehash_failed:
                self.table = new_table
                self.data_list = all_vals
                break

        self.print_table()

    def add(self, val):
        print(f"Add : {val}")

        # 1. Check threshold
        if self.is_over_threshold(len(self.data_list) + 1):
            self.rehash(val, "threshold")
            return

        # 2. Try inserting
        success = self.insert_into_table(self.table, self.size, val, self.max_col)
        if not success:
            self.rehash(val, "max_col")
        else:
            self.data_list.append(val)
            self.print_table()

print(" ***** Rehashing *****")
inp = input('Enter Input : ').split('/')
size, max_col, threshold = map(int, inp[0].split())
values = list(map(int, inp[1].split()))

r = Rehashing(size, max_col, threshold)
print("Initial Table :")
r.print_table()

for v in values:
    r.add(v)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# 1. Before inserting, check the load: (stored + 1) / size * 100 > threshold
#    -> rehash with the new value included.
# 2. Otherwise probe val % size with quadratic steps. If max_col collisions
#    happen -> rehash with the new value included.
# 3. Rehash: size = next prime > 2 * size, then re-insert all stored values in
#    their original insertion order, then the new value. If that itself hits
#    max collisions, grow again and retry.
# 4. Print the table after every Add.
#
# Worked example -- Enter Input : 5 1 67/1 6
#   Add 1 -> 1 % 5 = 1 -> slot #2.
#   Add 6 -> 6 % 5 = 1 is taken -> collision 1 = max -> rehash.
#   New size = next prime > 10 = 11. 1 -> slot #2, 6 -> slot #7.
# ================================================================================
