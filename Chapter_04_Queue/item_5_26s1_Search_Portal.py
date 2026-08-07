# ================================================================================
# Chapter 4 - Item 5: 26s1 Search Portal
# --------------------------------------------------------------------------------
# Problem Statement:
# Sunfong received an assignment from the teacher to create a programming problem for the students. He went home to think about it and found himself in a dark room. He can see and walk to adjacent areas (in 4 directions: North, South, East, West). Sunfong must find the exit door from the dream to deliver the assignment to the teacher. He decided to use the Breadth First Search (BFS) method, starting from the initial point, checking and remembering the path in the order of North, East, South, and West. Then, he walks to the next cell and repeats the process.
# Sunfong needs a program to tell him if he can reach the exit or if he will be stuck in the dream forever. He is too lazy to write the code himself, so he wants the students to write it for him in a neat and concise manner.
# Program Details:Input:
# Receive the width, height, and the map. Each line of the map is separated by a comma.Example input: 3 3 F__,##_,O__This means the map is 3 wide and 3 high, and it looks like this
# F__##_O__
# ================================================================================

class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, value):
        self.items.append(value)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
        
    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    inp = input("Enter width, height, and room: ")
    parts = inp.split()
    
    if len(parts) < 3:
        print("Invalid map input.")
        exit(0)
        
    width = int(parts[0])
    height = int(parts[1])
    room = parts[2].split(',')
    
    # Validation
    valid = True
    if len(room) != height:
        valid = False
    else:
        for r in room:
            if len(r) != width:
                valid = False
                break
                
    if not valid:
        print("Invalid map input.")
        exit(0)
        
    start = None
    for y in range(height):
        for x in range(width):
            if room[y][x] == 'F':
                start = (x, y)
                break
        if start:
            break
            
    if start is None:
        print("Invalid map input.")
        exit(0)
        
    q = Queue()
    q.enqueue(start)
    visited = set()
    visited.add(start)
    
    found = False
    
    # Directions: North, East, South, West
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    while not q.is_empty():
        print(f"Queue: {q.items}")
        curr = q.dequeue()
        x, y = curr
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if room[ny][nx] == 'O':
                    found = True
                    break
                if room[ny][nx] == '_' and (nx, ny) not in visited:
                    q.enqueue((nx, ny))
                    visited.add((nx, ny))
                    
        if found:
            break
            
    if found:
        print("Found the exit portal.")
    else:
        print("Cannot reach the exit portal.")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# This Python script solves Chapter 4 Item 5 (26s1 Search Portal).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================