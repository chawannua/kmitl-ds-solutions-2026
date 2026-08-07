# ðŸŽ“ KMITL Data Structures (01276122) - Chapters 3, 4 & 5 Exam Mastery Guide

> **Compiled by 3 Specialized Pro AI Agents (Stack Expert, Queue Expert, LinkedList Expert)**  
> **Course**: 01276122 Data Structures and Algorithms @ KMITL  
> **Target Exam**: Quiz #1 & Midterm Prep (Chapters 3: Stack, 4: Queue, 5: Linked List)

---

## ðŸ“Œ Table of Contents
1. [Chapter 3: Stack Mastery (LIFO, Parentheses, Infix/Postfix, Parking Lot)](#chapter-3-stack-mastery)
2. [Chapter 4: Queue Mastery (FIFO, Circular Queue, Cafe Simulation, BFS)](#chapter-4-queue-mastery)
3. [Chapter 5: Linked List Mastery (Singly/Doubly, Pointer Safety, Radix Sort, VIM Editor)](#chapter-5-linked-list-mastery)

---


# Chapter 3: Stack - Mastery Guide
**KMITL Data Structures (01276122)**

## 1. Core Principles

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added to the stack will be the first one to be removed. Think of it like a stack of plates in a cafeteria.

### Stack ADT Operations
*   `push(item)`: Adds an item to the top of the stack.
*   `pop()`: Removes and returns the top item from the stack.
*   `peek()` (or `top()`): Returns the top item without removing it.
*   `is_empty()`: Returns `True` if the stack is empty, `False` otherwise.
*   `size()`: Returns the number of items in the stack.

## 2. Algorithm Breakdown & Python Code Templates

### 2.1 Parentheses Matching
Used to check if an expression has balanced parentheses.

**Algorithm:**
1. Initialize an empty stack.
2. Iterate through each character in the expression.
3. If it's an opening bracket `(`, `[`, `{`, `push` it onto the stack.
4. If it's a closing bracket `)`, `]`, `}`, check if the stack is empty. If it is, return False (unbalanced).
5. `pop` from the stack and check if the popped bracket matches the closing bracket. If not, return False.
6. After iterating, if the stack is empty, return True (balanced), else False.

**Python Code Template (Full Matching):**
```python
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if not self.is_empty() else None
    def peek(self): return self.items[-1] if not self.is_empty() else None
    def is_empty(self): return len(self.items) == 0
    def size(self): return len(self.items)

def is_balanced(expression):
    s = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in "([{":
            s.push(char)
        elif char in ")]}":
            if s.is_empty() or s.pop() != pairs[char]:
                return False
    return s.is_empty()
```

### 2.2 Infix to Postfix Conversion
Converts standard mathematical expressions (infix) to postfix notation.

**Precedence Rules:**
*   `^` (Highest)
*   `*`, `/` (Medium)
*   `+`, `-` (Lowest)
*   `(` has lowest precedence when on the stack, but highest when incoming.

**Algorithm:**
1. Initialize a stack for operators and an empty list/string for output.
2. Scan the infix expression from left to right.
3. If operand (A, B, 1, 2), append to output.
4. If `(`, push to stack.
5. If `)`, pop from stack and append to output until `(` is encountered. Discard `(`.
6. If operator (`+`, `-`, `*`, `/`, `^`):
    *   While stack is not empty and precedence of top operator >= precedence of incoming operator (Note: `^` is usually right-associative, so for `^`, pop if top > incoming).
    *   Pop and append to output.
    *   Push incoming operator.
7. After scanning, pop remaining operators from stack to output.

### 2.3 Postfix Evaluation Algorithm
Evaluates a postfix expression.

**Algorithm:**
1. Initialize an empty stack.
2. Scan the postfix expression from left to right.
3. If operand, push onto stack.
4. If operator:
    *   Pop two operands (val2 = pop(), val1 = pop()). **Order matters!**
    *   Evaluate `val1 operator val2`.
    *   Push result back onto stack.
5. Final result is the only item left in the stack.

### 2.4 Parking Lot Simulation Pattern
Often models a narrow alley where cars enter and must back out.
*   Requires an **auxiliary stack** (like a temporary street) to hold cars blocking the target car.

**Algorithm for removing a specific car:**
1. While top of main stack is not target car: pop from main, push to auxiliary stack.
2. Pop target car from main (remove it).
3. Pop all cars from auxiliary stack back to main stack.

## 3. Common Exam Traps & Edge Cases

*   **Popping Empty Stack:** Always check `is_empty()` before `pop()` or `peek()`. Exam code might crash if you try to `pop` an empty list.
*   **Order of Evaluation in Postfix:** When popping for an operator (e.g., `-`), remember the first popped is the *right* operand, and the second popped is the *left* operand. `a = pop(), b = pop() -> result = b - a`.
*   **Operator Precedence & Associativity:** Exponentiation `^` is usually right-associative. So `A^B^C` is `A^(B^C)`. When pushing `^` and top is `^`, do not pop. For left-associative (`+`, `-`, `*`, `/`), if top >= incoming, pop.
*   **Unmatched Parentheses at the End:** In parentheses matching, don't forget the final check `return s.is_empty()`. An expression like `((()` will finish scanning without errors, but the stack won't be empty.
*   **String Parsing Errors:** Infix to postfix might have multi-digit numbers. Usually, exam questions space-delimit them or keep them single-character. Be careful if they don't.

## 4. Exam Practice Problems

### Problem 1: Postfix Evaluation
**Question:** Evaluate the postfix expression `5 3 + 8 2 / * 4 -` using a stack. Show the stack state at each step.

**Solution:**
1. Read `5`: push `5` -> Stack: `[5]`
2. Read `3`: push `3` -> Stack: `[5, 3]`
3. Read `+`: pop `3`, pop `5`, calc `5 + 3 = 8`, push `8` -> Stack: `[8]`
4. Read `8`: push `8` -> Stack: `[8, 8]`
5. Read `2`: push `2` -> Stack: `[8, 8, 2]`
6. Read `/`: pop `2`, pop `8`, calc `8 / 2 = 4`, push `4` -> Stack: `[8, 4]`
7. Read `*`: pop `4`, pop `8`, calc `8 * 4 = 32`, push `32` -> Stack: `[32]`
8. Read `4`: push `4` -> Stack: `[32, 4]`
9. Read `-`: pop `4`, pop `32`, calc `32 - 4 = 28`, push `28` -> Stack: `[28]`
**Result:** 28

### Problem 2: Infix to Postfix
**Question:** Convert `A * ( B + C ) - D / E` to postfix. Show the stack and output at each step.

**Solution:**
1. `A` -> Out: `A`, Stack: `[]`
2. `*` -> Out: `A`, Stack: `[*]`
3. `(` -> Out: `A`, Stack: `[*, (]`
4. `B` -> Out: `A B`, Stack: `[*, (]`
5. `+` -> Out: `A B`, Stack: `[*, (, +]`
6. `C` -> Out: `A B C`, Stack: `[*, (, +]`
7. `)` -> pop `+` to out, pop `(` discard -> Out: `A B C +`, Stack: `[*]`
8. `-` -> pop `*` to out (since `*` >= `-`), push `-` -> Out: `A B C + *`, Stack: `[-]`
9. `D` -> Out: `A B C + * D`, Stack: `[-]`
10. `/` -> push `/` (since `/` > `-`) -> Out: `A B C + * D`, Stack: `[-, /]`
11. `E` -> Out: `A B C + * D E`, Stack: `[-, /]`
12. End -> pop all -> Out: `A B C + * D E / -`

### Problem 3: Parentheses Matching
**Question:** Trace the stack for `{[()()]}` and state if it is balanced.

**Solution:**
1. `{` -> push -> Stack: `[{]`
2. `[` -> push -> Stack: `[{, []`
3. `(` -> push -> Stack: `[{, [, (]`
4. `)` -> pop `(` matches -> Stack: `[{, []`
5. `(` -> push -> Stack: `[{, [, (]`
6. `)` -> pop `(` matches -> Stack: `[{, []`
7. `]` -> pop `[` matches -> Stack: `[{]`
8. `}` -> pop `{` matches -> Stack: `[]`
End of string, Stack is empty. **Result:** True (Balanced).

### Problem 4: The Broken Stack
**Question:** What is the output of the following sequence of stack operations?
`push(1)`, `push(2)`, `pop()`, `push(3)`, `push(4)`, `pop()`, `pop()`, `push(5)`, `pop()`

**Solution:**
- `push(1)` -> `[1]`
- `push(2)` -> `[1, 2]`
- `pop()` -> returns 2, stack `[1]`
- `push(3)` -> `[1, 3]`
- `push(4)` -> `[1, 3, 4]`
- `pop()` -> returns 4, stack `[1, 3]`
- `pop()` -> returns 3, stack `[1]`
- `push(5)` -> `[1, 5]`
- `pop()` -> returns 5, stack `[1]`
**Outputs:** 2, 4, 3, 5

### Problem 5: Parking Lot Simulator
**Question:** A dead-end street (Main Stack) contains cars parked in order: `A, B, C, D` (where D is top/closest to exit). Car `B` needs to leave. Trace the movements using an Auxiliary Stack.

**Solution:**
Initial Main: `[A, B, C, D]` (D on top) | Aux: `[]`
1. Pop D from Main, Push D to Aux -> Main: `[A, B, C]`, Aux: `[D]`
2. Pop C from Main, Push C to Aux -> Main: `[A, B]`, Aux: `[D, C]`
3. Pop B from Main (Target car leaves) -> Main: `[A]`, Aux: `[D, C]`
4. Pop C from Aux, Push to Main -> Main: `[A, C]`, Aux: `[D]`
5. Pop D from Aux, Push to Main -> Main: `[A, C, D]`, Aux: `[]`
**Final State:** Main: `[A, C, D]`, Aux: `[]`


# Chapter 4: Queue Mastery Guide
**Course:** KMITL Data Structures (01276122)

## 1. Core Principles
A **Queue** is a linear data structure that follows the **FIFO (First-In, First-Out)** principle. The first element added to the queue will be the first one to be removed. Think of it like a line of people waiting for a cashier.

### Queue ADT Operations
*   `enqueue(item)`: Adds an item to the **rear** (end) of the queue.
*   `dequeue()`: Removes and returns the item from the **front** of the queue.
*   `peek()` (or `front()`): Returns the item at the front without removing it.
*   `size()`: Returns the number of elements in the queue.
*   `is_empty()`: Returns True if the queue is empty, False otherwise.

---

## 2. Algorithm Breakdown & Python Code Templates

### A. Basic Queue: `collections.deque` vs List `pop(0)`
While you can implement a queue using a standard Python list, using `pop(0)` is inefficient.
*   **List `pop(0)`**: Takes **O(n)** time because all subsequent elements must shift left.
*   **`collections.deque`**: Takes **O(1)** time for appends and pops from both ends, making it the standard for queue implementations in Python.

**Basic Queue Implementation:**
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
```

### B. Circular Queue Implementation
A regular array-based queue suffers from wasted space as the front moves forward. A Circular Queue wraps around to the beginning using modulo arithmetic.

**Template:**
```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            return "Queue is Full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "Queue is Empty"
        item = self.queue[self.front]
        self.queue[self.front] = None # Optional: clear reference
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = -1
        return item
```

### C. Multi-Barista / Cafe Queue Simulation Pattern
A common exam application. You track customers arriving and being assigned to the barista with the shortest queue or nearest availability time.

**Pattern Setup:**
```python
class Barista:
    def __init__(self, id):
        self.id = id
        self.busy_until = 0

def cafe_simulation(customers, num_baristas):
    baristas = [Barista(i) for i in range(num_baristas)]
    queue = deque(customers) # [(arrival_time, prep_time), ...]
    current_time = 0
    
    while queue:
        # Find first available barista
        available_barista = min(baristas, key=lambda b: b.busy_until)
        
        # Advance time if all baristas are busy and next customer arrived
        arrival_time, prep_time = queue.popleft()
        if current_time < arrival_time:
            current_time = arrival_time
            
        if available_barista.busy_until > current_time:
            current_time = available_barista.busy_until
            
        # Assign customer to barista
        print(f"Customer served by Barista {available_barista.id} at time {current_time}")
        available_barista.busy_until = current_time + prep_time
```

### D. Search Portal Grid Traversal (Queue-based BFS)
Queues are the backbone of Breadth-First Search (BFS), used heavily for pathfinding in grids or finding the shortest path through portals.

**BFS Template:**
```python
def bfs_shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)]) # (r, c, steps)
    visited = set([start])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, steps = queue.popleft()
        
        if (r, c) == end:
            return steps
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
    return -1
```

---

## 3. Common Exam Traps & Edge Cases
1.  **Modulo Arithmetic Errors**: When moving `front` or `rear` backwards (e.g., in Deque operations), students often write `(rear - 1) % capacity`. In Python, this works, but in C/Java it can yield a negative number. Better to use `(rear - 1 + capacity) % capacity`.
2.  **Off-by-One Capacity in Circular Queues**: In implementations that don't maintain a `size` counter, one array slot must be kept empty to differentiate between full (`(rear + 1) % cap == front`) and empty (`front == rear`). If the exam asks for a queue of size N using this method, the array must be size N + 1.
3.  **Multi-Queue State Sync**: In simulations, updating the global clock strictly by `+1` minute can lead to Time Limit Exceeded (TLE). Always fast-forward the global clock to the next relevant event (next customer arrival or next barista completion).
4.  **Forgetting to update `front` and `rear` to -1**: When a circular queue becomes empty after a dequeue, `front` and `rear` should be reset to `-1` (if that's the initialization logic), though relying on `size == 0` is safer.

---

## 4. Exam Practice Problems

### Problem 1: Circular Queue State Tracing
**Question:** A Circular Queue has a capacity of 5. Initialize it as empty. Perform the following:
`Enqueue(10), Enqueue(20), Enqueue(30), Dequeue(), Enqueue(40), Enqueue(50), Enqueue(60), Dequeue()`
What are the values of `front`, `rear`, and the current queue elements? (Assume 0-indexing, front and rear start at -1).

**Step-by-Step Solution:**
*   Start: `f=-1, r=-1, q=[None, None, None, None, None]`
*   Enq(10): `f=0, r=0, q=[10, _, _, _, _]`
*   Enq(20): `f=0, r=1, q=[10, 20, _, _, _]`
*   Enq(30): `f=0, r=2, q=[10, 20, 30, _, _]`
*   Deq(): removes 10. `f=1, r=2, q=[_, 20, 30, _, _]`
*   Enq(40): `f=1, r=3, q=[_, 20, 30, 40, _]`
*   Enq(50): `f=1, r=4, q=[_, 20, 30, 40, 50]`
*   Enq(60): Capacity is 5, size is 4. `r=(4+1)%5 = 0`. `f=1, r=0, q=[60, 20, 30, 40, 50]`
*   Deq(): removes 20 (at front `1`). `f=(1+1)%5 = 2`.
*   **Result:** `front=2`, `rear=0`, Elements in order: `30, 40, 50, 60`.

### Problem 2: Reverse a Queue using a Stack
**Question:** Write an algorithm to reverse the elements of a Queue using only a Stack and basic Queue ADT operations.

**Step-by-Step Solution:**
1.  Initialize an empty Stack.
2.  While the Queue is not empty, `dequeue()` an element and `push()` it onto the Stack.
3.  While the Stack is not empty, `pop()` an element from the Stack and `enqueue()` it back into the Queue.
*Since Stack is LIFO, the elements popped out will be in the reverse order of how they were dequeued.*

### Problem 3: Barista Wait Time
**Question:** 3 customers arrive at a cafe at times `[1, 2, 4]`. Their coffee prep times are `[3, 5, 2]`. There is 1 barista. Calculate the average waiting time for the customers (wait time = start_prep_time - arrival_time).

**Step-by-Step Solution:**
*   **C1:** arrives 1, barista free at 1. Wait = 1 - 1 = 0. Prep finishes at 1+3 = 4. Barista busy until 4.
*   **C2:** arrives 2, barista free at 4. Wait = 4 - 2 = 2. Prep finishes at 4+5 = 9. Barista busy until 9.
*   **C3:** arrives 4, barista free at 9. Wait = 9 - 4 = 5. Prep finishes at 9+2 = 11. Barista busy until 11.
*   **Average Wait:** (0 + 2 + 5) / 3 = 7 / 3 = 2.33.

### Problem 4: Implement Queue using Two Stacks
**Question:** Implement a Queue using two Stacks (`in_stack` and `out_stack`). Provide `enqueue` and `dequeue` logic.

**Step-by-Step Solution:**
*   **Enqueue(item):** Push the item onto `in_stack`. Time: O(1).
*   **Dequeue():**
    1. If both stacks are empty, raise Error.
    2. If `out_stack` is empty, pop all elements from `in_stack` and push them onto `out_stack`. (This reverses the order, bringing the oldest element to the top).
    3. Pop and return the top element from `out_stack`.
    *Amortized Time: O(1).*

### Problem 5: BFS Shortest Path
**Question:** You are at (0,0) in a 3x3 grid. Target is (2,2). `(1,0)` and `(1,1)` are walls. Show the queue state at each step of BFS to find the shortest path.
Grid:
```
S . .
W W .
. . E
```
**Step-by-Step Solution:**
*   Start: Q = `[(0,0)]`. Visited = `{(0,0)}`.
*   Step 1: Pop `(0,0)`. Neighbors: `(0,1)` (Right), Down is Wall.
    *   Q = `[(0,1)]`. Visited = `{(0,0), (0,1)}`.
*   Step 2: Pop `(0,1)`. Neighbors: `(0,2)` (Right), `(0,0)` (visited), Down is Wall.
    *   Q = `[(0,2)]`. Visited = `{(0,0), (0,1), (0,2)}`.
*   Step 3: Pop `(0,2)`. Neighbors: `(1,2)` (Down). Left is visited.
    *   Q = `[(1,2)]`. Visited = `{..., (1,2)}`.
*   Step 4: Pop `(1,2)`. Neighbors: `(2,2)` (Down) - Target reached! Path length = 4.


# Chapter 5: LinkedList - Mastery Guide (01276122)

## 1. Core Principles

### Nodes and Pointers
A **Linked List** is a linear data structure where elements are not stored in contiguous memory locations. Instead, elements are linked using pointers.
- **Node**: The fundamental unit of a linked list. It contains data and one or more pointers to other nodes.
- **Head**: A pointer to the first node in the list.
- **Tail**: A pointer to the last node in the list (optional but highly recommended for $O(1)$ appends).
- **Next**: A pointer in a node that references the next node in the sequence.
- **Prev**: A pointer in a node that references the previous node (used in Doubly Linked Lists).

### Singly vs Doubly Linked List
- **Singly Linked List**: Each node contains data and a `next` pointer. Traversal is strictly one-way (forward). Memory overhead is lower.
- **Doubly Linked List**: Each node contains data, a `next` pointer, and a `prev` pointer. Traversal can be forward or backward. Deletion and insertion before a given node are easier, but memory overhead is higher, and pointer updates are more complex.

---

## 2. Algorithm Breakdown & Python Code Templates

### 2.1 Singly Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def insert(self, index, data):
        if index <= 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            if not self.tail: self.tail = new_node
            return
        
        curr = self.head
        for _ in range(index - 1):
            if not curr: return # Out of bounds
            curr = curr.next
            
        if not curr: return # Out of bounds
        
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node
        if not new_node.next:
            self.tail = new_node

    def remove(self, data):
        curr = self.head
        prev = None
        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                    if not curr.next:
                        self.tail = prev
                else:
                    self.head = curr.next
                    if not self.head:
                        self.tail = None
                return True
            prev = curr
            curr = curr.next
        return False

    def reverse(self):
        prev = None
        curr = self.head
        self.tail = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
```

### 2.2 Doubly Linked List
```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_at_index(self, index, data):
        if index <= 0:
            new_node = DNode(data)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail: self.tail = new_node
            return
            
        curr = self.head
        for _ in range(index - 1):
            if not curr: return
            curr = curr.next
            
        if not curr: return
        
        new_node = DNode(data)
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        else:
            self.tail = new_node
        curr.next = new_node

    def remove_value(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                    
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return True
            curr = curr.next
        return False
```

### 2.3 Merge Two Sorted Linked Lists
```python
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    curr = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        
    curr.next = l1 if l1 else l2
    return dummy.next
```

### 2.4 VIM Text Editor Simulation
Using a Doubly Linked List with a cursor pointer.
```python
class VimEditor:
    def __init__(self):
        self.head = DNode('|') # Cursor representation
        self.tail = self.head
        self.cursor = self.head

    def insert(self, char):
        new_node = DNode(char)
        new_node.prev = self.cursor.prev
        new_node.next = self.cursor
        
        if self.cursor.prev:
            self.cursor.prev.next = new_node
        else:
            self.head = new_node
            
        self.cursor.prev = new_node

    def move_left(self):
        if self.cursor.prev:
            # Swap cursor data with prev data visually, or move pointer
            pass # Implementation depends on specific requirements

    def move_right(self):
        if self.cursor.next:
            pass
            
    def delete(self):
        # Backspace behavior (delete char before cursor)
        if self.cursor.prev:
            to_delete = self.cursor.prev
            if to_delete.prev:
                to_delete.prev.next = self.cursor
            else:
                self.head = self.cursor
            self.cursor.prev = to_delete.prev
```

### 2.5 Radix Sort (Descending Order using Linked Lists)
```python
def radix_sort_descending(head):
    if not head: return None
    
    # Find max to know number of digits
    curr = head
    max_val = curr.data
    while curr:
        if curr.data > max_val: max_val = curr.data
        curr = curr.next
        
    exp = 1
    while max_val // exp > 0:
        buckets = [SinglyLinkedList() for _ in range(10)]
        
        curr = head
        while curr:
            digit = (curr.data // exp) % 10
            buckets[digit].append(curr.data)
            curr = curr.next
            
        # Reconstruct in descending order (bucket 9 to 0)
        head = None
        tail = None
        for i in range(9, -1, -1):
            if buckets[i].head:
                if not head:
                    head = buckets[i].head
                    tail = buckets[i].tail
                else:
                    tail.next = buckets[i].head
                    tail = buckets[i].tail
        exp *= 10
        
    return head
```

---

## 3. Common Exam Traps & Edge Cases

1. **`AttributeError: 'NoneType' has no attribute 'next'`**:
   - Always check if `curr` or `curr.next` is `None` before accessing attributes.
   - Common in while loops: `while curr.next:` will fail if `curr` is `None`. Use `while curr and curr.next:`.

2. **Head/Tail Boundary Updates**:
   - If you delete the *only* node in a list, both `head` and `tail` must be set to `None`.
   - If you append to an empty list, both `head` and `tail` point to the new node.
   - If you insert at the end or delete the last node, `tail` must be updated!

3. **Dummy Head Nodes**:
   - Extremely useful for algorithms that might modify the head of the list (e.g., merging sorted lists, removing specific elements).
   - `dummy = Node(0)`, `dummy.next = head`. Return `dummy.next` at the end. It eliminates the need for edge-case checks for the head node.

4. **Circular References in Reversing**:
   - When reversing a list, make sure the original head's `next` pointer is set to `None`, or you'll create a cycle.

5. **Garbage Collection**:
   - Python handles memory automatically, but in exams, ensuring all pointers (`prev` and `next`) of removed nodes are disconnected is good practice.

---

## 4. Exam Practice Problems

### Problem 1: Detect a Cycle
**Task**: Given the head of a linked list, determine if it has a cycle.
**Solution**: Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Problem 2: Find the Middle Node
**Task**: Return the middle node of a linked list. If there are two middle nodes, return the second one.
**Solution**: Slow/Fast pointers.
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### Problem 3: Remove Nth Node From End
**Task**: Remove the nth node from the end of the list and return its head.
**Solution**: Two pointers with a gap of N.
```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = second = dummy
    
    for _ in range(n + 1):
        first = first.next
        
    while first:
        first = first.next
        second = second.next
        
    second.next = second.next.next
    return dummy.next
```

### Problem 4: Palindrome Linked List
**Task**: Check if a singly linked list is a palindrome.
**Solution**: Find middle, reverse second half, compare.
```python
def is_palindrome(head):
    if not head or not head.next: return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # Reverse second half
    prev = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
        
    # Compare halves
    left, right = head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    return True
```

### Problem 5: Swap Nodes in Pairs
**Task**: Swap every two adjacent nodes and return its head. (e.g., 1->2->3->4 becomes 2->1->4->3).
**Solution**: Use a dummy node and iterative swapping.
```python
def swap_pairs(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # Swap
        first.next = second.next
        second.next = first
        prev.next = second
        
        # Move forward
        prev = first
        
    return dummy.next
```
