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
# Breadth-First Search over a grid maze, using the FIFO Queue as the BFS frontier.
#
# Core idea:
#   A FIFO queue makes BFS explore the maze in "rings" of increasing distance
#   from the start: everything enqueued at the current distance is dequeued and
#   expanded before anything at the next distance is even looked at, since new
#   cells always join the REAR while dequeue() always takes the FRONT.
#
# Key Steps & Logic:
# 1. The map string ("F__,##_,O__") is split on ',' into rows; room[y][x] indexes
#    row y, column x. 'F' marks the start, scanned row-major and stored as (x, y).
# 2. q.enqueue(start) seeds the frontier; the visited set is populated as soon as
#    a cell is enqueued (not when it's dequeued) so the same cell can never be
#    queued twice, which would otherwise loop forever between open cells.
# 3. print(f"Queue: {q.items}") runs BEFORE q.dequeue(), so each printed line is
#    a snapshot of the frontier the instant curr is about to be pulled from it.
# 4. directions = [N, E, S, W] fixes the exact order neighbors are tried, per the
#    problem statement -- it changes the trace but not whether 'O' is reachable.
# 5. For each neighbor: an 'O' cell sets found = True and breaks immediately
#    (the exit itself is never enqueued, since the search can stop there); a
#    '_' cell not yet in visited is enqueued and marked visited in the same step
#    to close the race between two directions reaching it at once.
# 6. The `if found: break` after the neighbor loop exits the outer while too, so
#    BFS stops the moment the exit is discovered rather than draining the queue.
#
# Worked example -- "3 3 F__,##_,O__" (grid: row0 "F__", row1 "##_", row2 "O__")
#   op            | queue printed  | why
#   --------------+----------------+---------------------------------------
#   start=(0,0)   | [(0,0)]        | 'F' found at row 0, col 0
#   dequeue (0,0) | [(1,0)]        | E=(1,0) '_' enqueued; S=(0,1) '#' blocked
#   dequeue (1,0) | [(2,0)]        | E=(2,0) '_' enqueued; W=(0,0) visited
#   dequeue (2,0) | [(2,1)]        | S=(2,1) '_' enqueued
#   dequeue (2,1) | [(2,2)]        | S=(2,2) '_' enqueued; W=(1,1) '#' blocked
#   dequeue (2,2) | [(1,2)]        | W=(1,2) '_' enqueued
#   dequeue (1,2) | (none printed) | W=(0,2) is 'O' -> found = True, break
#   -> "Found the exit portal."
# ================================================================================