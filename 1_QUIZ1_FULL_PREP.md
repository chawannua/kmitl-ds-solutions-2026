# KMITL Data Structures & Algorithms (01276122)
# Ultimate Quiz 1 Preparation Guide - Chapters 1 to 5
# Format: UTF-8 Plain ASCII (No Emoji, Standard Quotes)
# Primary Focus: Chapters 3 (Stack), 4 (Queue), 5 (Linked List)
# Refresher: Chapters 1 (Python 1) & 2 (Python 2)

---

## TABLE OF CONTENTS
1. Foundational Refresher: Python 1 & 2 (Ch 1 & Ch 2)
2. Chapter 3: Stack Data Structure
3. Chapter 4: Queue Data Structure
4. Chapter 5: Linked List Data Structure
5. Master Big-O Complexity Comparison Table
6. Top Exam Pitfalls, Edge Cases & Debugging Checklist

---

## 1. FOUNDATIONAL REFRESHER: PYTHON 1 & 2 (Ch 1 & Ch 2)

### Chapter 1: Python 1 Essentials

#### 1. Input Parsing Patterns
```python
# Single integer / float
n = int(input())
f = float(input())

# Space-separated integers / floats
a, b, c = map(int, input().split())
d, Vr, Vt, Vf = map(float, input().split())

# Array of values
arr = list(map(int, input().split()))

# Comma-separated strings
items = [x.strip() for x in input().split(',')]
```

#### 2. Item 1: Rabbit, Turtle, Fly (Physics Formula)
Problem logic: Calculate the distance a fly travels back and forth between a rabbit and turtle moving towards each other.
Formula: 
- Total time before collision = d / (Vr + Vt)
- Fly distance = total_time * Vf = (d * Vf) / (Vr + Vt)
```python
d, Vr, Vt, Vf = map(float, input().split())
fly_distance = (d * Vf) / (Vr + Vt)
print(f"{fly_distance:.2f}")
```

#### 3. Item 2 & 3: Math operations, Digit Sums & Formatting
```python
# Multiplication or Sum: if product <= 1000 return product else return sum
def mult_or_sum(a, b):
    p = a * b
    return p if p <= 1000 else a + b

# Digit Sum of a number string
def digit_sum(n_str):
    return sum(int(ch) for ch in n_str if ch.isdigit())

# Output formatting: width alignment and precision
print(f"{val:.2f}")          # 2 decimal places
print(f"{val:05d}")          # Zero padded width 5
```

#### 4. Item 5: Vickrey Auction (Second-Price Sealed-Bid)
Rule: The highest bidder wins, but pays the second-highest bid price. If there is a tie for highest bid, or fewer than 2 bids, handle edge cases.
```python
def vickrey_auction(bids):
    if len(bids) < 2:
        return "not enough bidder"
    bids.sort(reverse=True)
    if bids[0] == bids[1]:
        return "error : have more than one max bid"
    return f"winner : {bids[0]} total price : {bids[1]}"
```

---

### Chapter 2: Python 2 Advanced Concepts & OOP

#### 1. Item 1: Roman Numeral Converter Class
```python
class Roman:
    def __init__(self):
        self.val_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        self.roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def int_to_roman(self, num):
        res = ""
        for val, symbol in self.val_map:
            while num >= val:
                res += symbol
                num -= val
        return res

    def roman_to_int(self, s):
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and self.roman_map[s[i]] < self.roman_map[s[i+1]]:
                res -= self.roman_map[s[i]]
            else:
                res += self.roman_map[s[i]]
        return res
```

#### 2. Item 2: Spherical Class (OOP)
```python
import math

class Spherical:
    def __init__(self, r):
        self.radius = r

    def changeR(self, Radius):
        self.radius = Radius

    def findVolume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    def findArea(self):
        return 4 * math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Is Sphere with radius {self.radius} Vol : {self.findVolume()} Area : {self.findArea()}"
```

#### 3. Item 3: Custom Range Generator Function
```python
def my_range(*args):
    if len(args) == 1:
        start, stop, step = 0.0, float(args[0]), 1.0
    elif len(args) == 2:
        start, stop, step = float(args[0]), float(args[1]), 1.0
    elif len(args) == 3:
        start, stop, step = float(args[0]), float(args[1]), float(args[2])
    else:
        raise TypeError("my_range expects 1 to 3 arguments")

    res = []
    curr = start
    if step > 0:
        while curr < stop - 1e-9:
            res.append(round(curr, 3))
            curr += step
    elif step < 0:
        while curr > stop + 1e-9:
            res.append(round(curr, 3))
            curr += step
    return tuple(res)
```

#### 4. Item 4: 3-Sum Algorithm (O(N^2) Two-Pointer Technique)
Goal: Find all unique triplets `[arr[i], arr[j], arr[k]]` such that `arr[i] + arr[j] + arr[k] == 0`.
```python
def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplet = [nums[i], nums[left], nums[right]]
                if triplet not in res:
                    res.append(triplet)
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res
```

#### 5. Item 5: funString Class (String Operations)
```python
class funString:
    def __init__(self, string=""):
        self.string = string

    def size(self):
        return len(self.string)

    def change_case(self):
        return self.string.swapcase()

    def reverse(self):
        return self.string[::-1]

    def delete_duplicate(self):
        seen = set()
        res = []
        for ch in self.string:
            if ch not in seen:
                seen.add(ch)
                res.append(ch)
        return "".join(res)
```

---

## 2. CHAPTER 3: STACK DATA STRUCTURE (LIFO)

### Core Stack Principles
- Operations: `push` (add to top), `pop` (remove from top), `peek` (view top), `is_empty`
- Time Complexity: O(1) for push, pop, peek when implemented with Python list or custom Stack class.
- Space Complexity: O(N) where N is number of elements stored.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

---

### Key Stack Algorithms & Problem Implementations

#### 1. Parentheses Matching Ver 1 (Counting Unmatched Brackets)
Goal: Count total unmatched opening and closing brackets (`(`, `)`, `[`, `]`). Output `"Perfect ! ! !"` if balance == 0.
```python
def count_unmatched_parentheses(s):
    matching = {')': '(', ']': '['}
    stack = Stack()
    unmatched_closers = 0

    for ch in s:
        if ch in '([':
            stack.push(ch)
        elif ch in ')]':
            if not stack.is_empty() and stack.peek() == matching[ch]:
                stack.pop()
            else:
                unmatched_closers += 1

    unmatched_openers = stack.size()
    total_unmatched = unmatched_closers + unmatched_openers
    return total_unmatched
```

#### 2. Parentheses Matching Ver 2 (Error Classification)
Goal: Identify exact error type: `"MATCH"`, `"close paren excess"`, `"open paren excess"`, or `"Unmatch open-close"`.
```python
def check_parentheses_detailed(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = Stack()

    for ch in s:
        if ch in '([{':
            stack.push(ch)
        elif ch in ')]}':
            if stack.is_empty():
                return "close paren excess", None, None
            top = stack.pop()
            if top != pairs[ch]:
                return "Unmatch open-close", None, None

    if not stack.is_empty():
        return "open paren excess", stack.size(), "".join(stack.items)

    return "MATCH", None, None
```

#### 3. Infix to Postfix Conversion (Handling ^ Right-Associativity)
Precedence Rules:
- `^` (exponentiation): precedence 3, RIGHT-associative
- `*`, `/`: precedence 2, LEFT-associative
- `+`, `-`: precedence 1, LEFT-associative
- `(`: precedence 0

Right-Associativity Rule:
- When incoming operator has EQUAL precedence to stack top:
  - If LEFT-associative: Pop stack top to output (while loop condition >=).
  - If RIGHT-associative (`^`): Keep stack top! (while loop condition >).

```python
def infix_to_postfix(expr):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_assoc = {'^'}
    output = []
    stack = Stack()

    for token in expr.split():
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        else:  # Operator
            while not stack.is_empty() and stack.peek() != '(':
                top_prec = prec.get(stack.peek(), 0)
                curr_prec = prec.get(token, 0)
                if top_prec > curr_prec or (top_prec == curr_prec and token not in right_assoc):
                    output.append(stack.pop())
                else:
                    break
            stack.push(token)

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)
```

#### 4. Stack Calculator (Instruction Execution)
Supported Commands:
- `+`, `-`, `*`, `/`: Pop top two items, perform binary operation, push result. Note subtraction is `sec - top`, division is `sec / top`.
- `DUP`: Duplicate the top element.
- `POP`: Pop and discard the top element.
- `PSH <val>` / numeric tokens: Push value onto stack.
- Invalid tokens: Return `"Invalid instruction: <token>"`.

```python
class StackCalculator:
    def run(self, instructions):
        stack = Stack()
        tokens = instructions.split()
        i = 0
        while i < len(tokens):
            t = tokens[i]
            if t in ('+', '-', '*', '/'):
                if stack.size() < 2:
                    return "Invalid instruction"
                b = stack.pop()  # top
                a = stack.pop()  # second
                if t == '+': stack.push(a + b)
                elif t == '-': stack.push(a - b)
                elif t == '*': stack.push(a * b)
                elif t == '/': stack.push(a / b)
            elif t == 'DUP':
                if stack.is_empty(): return "Invalid instruction"
                stack.push(stack.peek())
            elif t == 'POP':
                if stack.is_empty(): return "Invalid instruction"
                stack.pop()
            elif t == 'PSH':
                i += 1
                stack.push(float(tokens[i]))
            else:
                try:
                    stack.push(float(t))
                except ValueError:
                    return f"Invalid instruction: {t}"
            i += 1

        if stack.is_empty():
            return 0
        res = stack.peek()
        if isinstance(res, float) and res.is_integer():
            return int(res)
        return res
```

#### 5. Parking Lot Simulation (Stack with Restoring Operation)
Scenario:
- Narrow single-lane parking lane represented as Stack.
- `arrive`: Check if car already present or lot is full (max_cars). Otherwise push.
- `depart`: Pop cars into a temporary stack until target car is removed, then restore temporary stack back into main stack.

```python
class ParkingLot:
    def __init__(self, max_cars, cars):
        self.max_cars = max_cars
        self.stack = Stack()
        for c in cars:
            if c != 0:
                self.stack.push(c)

    def arrive(self, car_num):
        if car_num in self.stack.items:
            return f"car {car_num} already in soi"
        if self.stack.size() >= self.max_cars:
            return f"car {car_num} cannot arrive : Soi Full"
        self.stack.push(car_num)
        return f"car {car_num} arrive! : Add Car {car_num}"

    def depart(self, car_num):
        if car_num not in self.stack.items:
            return f"car {car_num} cannot depart : Dont Have Car {car_num}"

        temp = Stack()
        while self.stack.peek() != car_num:
            temp.push(self.stack.pop())
        self.stack.pop()  # remove target car
        while not temp.is_empty():
            self.stack.push(temp.pop())  # restore cars

        return f"car {car_num} depart ! : Car {car_num} was remove"
```

---

## 3. CHAPTER 4: QUEUE DATA STRUCTURE (FIFO)

### Core Queue Principles
- Operations: `enqueue` (add to rear), `dequeue` (remove from front), `peek` (view front), `is_empty`
- Time Complexity Warning:
  - Python `list.pop(0)` is O(N) because all remaining N-1 elements shift left!
  - `collections.deque.popleft()` is O(1) time complexity.
  - Circular Queue array implementation is O(1) time complexity.

---

### Key Queue Algorithms & Problem Implementations

#### 1. Basic Queue & Queue using `collections.deque`
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)    # O(1)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()  # O(1)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

#### 2. Circular Queue Implementation
Concept: Array of fixed capacity `N` with `front`, `rear`, and `size` variables. Index wrapping uses modulo arithmetic `% N`.
```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            return False
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.data[self.front]
```

#### 3. Cafe Simulation (Multi-Barista Queue)
Scenario: Customers arrive at time `arr` with preparation time `prep`. 2 baristas process orders.
Assignment rule: Assign to whichever barista becomes free earliest (`b1_free` vs `b2_free`).
```python
class Customer:
    def __init__(self, cid, arr, prep):
        self.cid = cid
        self.arr = arr
        self.prep = prep
        self.finish = 0
        self.wait = 0

def cafe_simulation(log_str):
    raw_orders = log_str.split('/')
    q = deque()
    for i, s in enumerate(raw_orders):
        arr, prep = map(int, s.split(','))
        q.append(Customer(i + 1, arr, prep))

    b1_free, b2_free = 0, 0
    processed = []

    while q:
        c = q.popleft()
        if b1_free <= b2_free:
            start = max(c.arr, b1_free)
            c.wait = start - c.arr
            c.finish = start + c.prep
            b1_free = c.finish
        else:
            start = max(c.arr, b2_free)
            c.wait = start - c.arr
            c.finish = start + c.prep
            b2_free = c.finish
        processed.append(c)

    processed.sort(key=lambda x: (x.finish, x.cid))
    return processed
```

#### 4. Search Portal (2D Grid BFS Algorithm)
Rule: Search directions order: North `(0, -1)`, East `(1, 0)`, South `(0, 1)`, West `(-1, 0)`.
CRITICAL: Mark visited immediately upon ENQUEUING to avoid processing duplicate grid nodes!
```python
def search_portal_bfs(width, height, room_grid):
    start = None
    for y in range(height):
        for x in range(width):
            if room_grid[y][x] == 'F':
                start = (x, y)
                break
        if start: break

    if not start:
        return "Invalid map input."

    q = deque([start])
    visited = {start}
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # North, East, South, West

    found = False
    while q:
        curr = q.popleft()
        x, y = curr

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if room_grid[ny][nx] == 'O':
                    found = True
                    break
                if room_grid[ny][nx] == '_' and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
        if found:
            break

    return "Found the exit portal." if found else "Cannot reach the exit portal."
```

---

## 4. CHAPTER 5: LINKED LIST DATA STRUCTURE (PRIMARY FOCUS)

### Linked List Principles vs Dynamic Arrays
- Array: Contiguous memory, O(1) index access, O(N) insert/delete at head/middle.
- Linked List: Non-contiguous nodes with pointers, O(N) index access, O(1) insert/delete at head or adjacent to known node pointers.

---

### 1. Singly Linked List (SLL)

#### Node Structure & Class Definition
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur = self.head
        res = []
        while cur:
            res.append(str(cur.value))
            cur = cur.next
        return " ".join(res) + " "

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
```

#### Core SLL Methods Implementations
```python
    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def search(self, item):
        cur = self.head
        while cur:
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, item):
        cur = self.head
        idx = 0
        while cur:
            if cur.value == item:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def pop(self, pos):
        if pos < 0 or self.isEmpty():
            return "Out of Range"
        if pos == 0:
            self.head = self.head.next
            return "Success"
        cur = self.head
        idx = 0
        while cur.next and idx < pos - 1:
            cur = cur.next
            idx += 1
        if cur.next is None:
            return "Out of Range"
        cur.next = cur.next.next
        return "Success"

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
```

---

### 2. Doubly Linked List (DLL)

#### Node Structure & Class Definition
```python
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def __str__(self):
        if self.isEmpty():
            return ""
        cur = self.head
        elements = []
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        return "->".join(elements)

    def str_reverse(self):
        if self.isEmpty():
            return ""
        cur = self.tail
        elements = []
        while cur:
            elements.append(str(cur.data))
            cur = cur.previous
        return "->".join(elements)
```

#### Core DLL Methods Implementations
```python
    def append(self, data):
        new_node = DLLNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def insert(self, index, data):
        new_node = DLLNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
            return

        sz = self.size()
        if index == 0:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        elif index >= sz:
            self.append(data)
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            new_node.next = cur
            new_node.previous = cur.previous
            cur.previous.next = new_node
            cur.previous = new_node

    def remove(self, data):
        cur = self.head
        idx = 0
        while cur:
            if cur.data == data:
                if cur.previous:
                    cur.previous.next = cur.next
                else:
                    self.head = cur.next

                if cur.next:
                    cur.next.previous = cur.previous
                else:
                    self.tail = cur.previous
                return cur, idx
            cur = cur.next
            idx += 1
        return None, -1
```

---

### 3. Merge Ordered Lists (Item 3)
Problem Rule: Merge two sorted singly linked lists `p` and `q` into one ascending order linked list. No `sort()` call allowed. No LinkedList class wrapper allowed (functions only).

```python
class node:
    def __init__(self, data, next=None):
        self.data = int(data)
        self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if not l or l == ['']:
        return None
    head = node(l[0])
    cur = head
    for val in l[1:]:
        cur.next = node(val)
        cur = cur.next
    return head

def printList(H):
    cur = H
    while cur:
        print(cur.data, end=' ')
        cur = cur.next
    print()

def mergeOrderesList(p, q):
    dummy = node(0)
    cur = dummy
    while p and q:
        if p.data <= q.data:
            cur.next = p
            p = p.next
        else:
            cur.next = q
            q = q.next
        cur = cur.next

    if p:
        cur.next = p
    if q:
        cur.next = q

    return dummy.next
```

---

### 4. VIM Text Editor Simulation (Item 4)
Problem Architecture: Doubly Linked List with `dummy_head` and `dummy_tail`.
Cursor variable points to the node BEFORE the cursor bar `|`.

Supported Commands:
- `I <word>`: Insert word immediately after `self.cursor`, update cursor to `new_node`.
- `L`: Move cursor left (`cursor = cursor.prev`) if not at `dummy_head`.
- `R`: Move cursor right (`cursor = cursor.next`) if `cursor.next` is not `dummy_tail`.
- `B`: Backspace char to left of cursor (remove node at `cursor`, move cursor to `cursor.prev`).
- `D`: Delete char to right of cursor (remove node at `cursor.next`).

```python
class VIMNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class TextEditor:
    def __init__(self):
        self.dummy_head = VIMNode(None)
        self.dummy_tail = VIMNode(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.cursor = self.dummy_head

    def insert(self, word):
        new_node = VIMNode(word)
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
```

---

### 5. Radix Sort Descending Order using Linked List Buckets (Item 5)
Algorithm Requirements:
1. Determine max number of rounds from maximum digit count: `max_digits = len(str(max_abs_val))`.
2. Create 10 LinkedList buckets (`bins[0]` through `bins[9]`).
3. Bucket digit extraction formula: `digit = (abs(val) // (10 ** (rnd - 1))) % 10`.
4. Descending Harvesting Order:
   - Positives (`>= 0`): Harvest from bin 9 down to bin 0.
   - Negatives (`< 0`): Harvest from bin 0 up to bin 9.

```python
class RadixNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class RadixLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = RadixNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def clear(self):
        self.head = self.tail = None

    def print_elements(self):
        cur = self.head
        elements = []
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        return " ".join(elements) + " " if elements else ""

    def to_arrow_string(self):
        cur = self.head
        elements = []
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        return " -> ".join(elements)

def radix_sort_descending(arr):
    if not arr: return

    before_list = RadixLinkedList()
    for num in arr:
        before_list.append(num)

    max_abs_val = max(abs(x) for x in arr)
    max_digits = 0 if max_abs_val == 0 else len(str(max_abs_val))

    main_list = RadixLinkedList()
    for num in arr:
        if num >= 0: main_list.append(num)
    for num in arr:
        if num < 0: main_list.append(num)

    for rnd in range(1, max_digits + 1):
        print("-" * 60)
        print(f"Round : {rnd}")
        bins = [RadixLinkedList() for _ in range(10)]

        cur = main_list.head
        while cur:
            val = cur.data
            digit = (abs(val) // (10 ** (rnd - 1))) % 10
            bins[digit].append(val)
            cur = cur.next

        for i in range(10):
            print(f"{i} : {bins[i].print_elements()}")

        main_list.clear()
        # Collect Positives (9 down to 0)
        for i in range(9, -1, -1):
            cur = bins[i].head
            while cur:
                if cur.data >= 0:
                    main_list.append(cur.data)
                cur = cur.next

        # Collect Negatives (0 up to 9)
        for i in range(10):
            cur = bins[i].head
            while cur:
                if cur.data < 0:
                    main_list.append(cur.data)
                cur = cur.next

    print("-" * 60)
    print(f"{max_digits} Time(s)")
    print(f"Before Radix Sort : {before_list.to_arrow_string()}")
    print(f"After  Radix Sort : {main_list.to_arrow_string()}")
```

---

## 5. MASTER BIG-O COMPLEXITY COMPARISON TABLE

| Data Structure / Operation | Access by Index | Search by Value | Insert at Head | Insert at Tail | Insert at Middle | Delete at Head | Delete at Tail | Delete at Middle |
|----------------------------|-----------------|-----------------|----------------|----------------|------------------|----------------|----------------|------------------|
| Python List (`list`)       | O(1)            | O(N)            | O(N)           | O(1) amortized | O(N)             | O(N)           | O(1)           | O(N)             |
| `collections.deque`        | O(N)            | O(N)            | O(1)           | O(1)           | O(N)             | O(1)           | O(1)           | O(N)             |
| Stack (List / Custom)      | N/A (Top O(1))  | O(N)            | O(1) (Push)    | N/A            | N/A              | O(1) (Pop)     | N/A            | N/A              |
| Queue (Deque / Circular)   | N/A (Front O(1))| O(N)            | N/A            | O(1) (Enqueue) | N/A              | O(1) (Dequeue) | N/A            | N/A              |
| Singly Linked List (SLL)   | O(N)            | O(N)            | O(1)           | O(N) / O(1)*   | O(N)             | O(1)           | O(N)           | O(N)             |
| Doubly Linked List (DLL)   | O(N)            | O(N)            | O(1)           | O(1)*          | O(N)             | O(1)           | O(1)*          | O(N)             |

*Note: SLL with tail pointer supports O(1) tail append. DLL with head & tail pointers supports O(1) append and O(1) tail deletion.

---

## 6. TOP EXAM PITFALLS, EDGE CASES & DEBUGGING CHECKLIST

| # | Pitfall / Error | Problem Area | Correct Fix / Rule |
|---|-----------------|--------------|--------------------|
| 1 | Using `list.pop(0)` for Queue | Queue (Ch 4) | Causes TLE (Time Limit Exceeded - O(N)). Use `deque.popleft()` or Circular Queue for O(1). |
| 2 | Exponentiation `^` associativity | Stack (Ch 3) | `^` is RIGHT-associative. Do NOT pop equal-precedence `^` off the stack when parsing infix! |
| 3 | Popping operands in wrong order | Stack (Ch 3) | `b = stack.pop()` is top operand, `a = stack.pop()` is second. Division is `a / b`, sub is `a - b`. |
| 4 | Circular Queue array indexing | Queue (Ch 4) | Always use modulo arithmetic: `(index + 1) % capacity`. |
| 5 | BFS visited set timing | Queue (Ch 4) | Add to `visited` BEFORE / AT ENQUEUE, not after dequeue, to prevent exponential duplicate nodes! |
| 6 | Forgotten `prev` pointers in DLL | Linked List (Ch 5) | Updating `node.next` without updating `node.next.previous` causes broken reverse traversal! |
| 7 | Pop on Empty List / Out of Range | Linked List (Ch 5) | Check `if pos < 0 or pos >= size()` or `self.isEmpty()` before dereferencing `cur.next`. |
| 8 | Loose head / tail updating | Linked List (Ch 5) | When inserting/removing index 0, update `self.head`. When operating at size-1, update `self.tail`. |
| 9 | Radix Sort harvesting direction | Linked List (Ch 5) | Descending radix: Positives from bin 9 down to 0, Negatives from bin 0 up to 9! |
| 10| Input splitting format | Ch 1 - Ch 5 | Pay close attention to input delimiters: `,`, `/`, or space ` `. Strip whitespace carefully! |

---
