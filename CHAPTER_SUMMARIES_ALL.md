# KMITL Data Structures & Algorithms - All Chapter Summaries
# Course: 01276122 | Student ID: 68011309
# Last Updated: 2026-08-08
# Format: Markdown (UTF-8, plain ASCII - safe for all terminals)

================================================================================
>>> QUIZ 1 FOCUS: CHAPTER 3 (STACK), CHAPTER 4 (QUEUE), CHAPTER 5 (LINKED LIST) <<<
================================================================================

---

## HOW TO UPDATE THIS FILE
- Each chapter has a clearly marked section header: `## CHAPTER X: <TITLE>`
- CHAPTERS 3, 4, AND 5 ARE THE PRIMARY FOCUS FOR QUIZ 1.
- CHAPTERS 1 AND 2 SERVE AS FOUNDATIONAL REFRESHER NOTES.
- Use plain ASCII characters only - NO emoji or non-ASCII symbols.

---

## CHAPTER 1: Python Basics (Python 1) [FOUNDATIONAL REFRESHER]

### Core Concepts
- Input parsing, type conversion, math operations, conditional logic
- Functions, return values, default arguments
- String operations, list comprehensions

### Key Patterns

**Fast Input Parsing**
```python
n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))
```

**Math Helpers**
```python
import math
math.sqrt(x)       # square root
math.floor(x)      # round down
math.ceil(x)       # round up
math.gcd(a, b)     # greatest common divisor
x ** 2             # power
x % 2 == 0         # even check
```

**String Operations**
```python
s = input().strip()
s.upper()          # uppercase
s.lower()          # lowercase
s[::-1]            # reverse string
s.split()          # split by whitespace
",".join(lst)      # join list to string
len(s)             # string length
```

**List Comprehension**
```python
squares = [x**2 for x in range(10)]
evens = [x for x in arr if x % 2 == 0]
```

### Chapter 1 Problems Summary
| Problem | Algorithm | Key Trick |
|---------|-----------|-----------|
| Rabbit Turtle Fly | Math formula | Distance/speed ratio |
| Multiplication or Sum | Conditional | Compare product vs sum |
| Digit Sum | Loop/Math | x % 10 gets last digit |
| Function | Function definition | Return value |
| Vickrey Auction | Sort + logic | Second highest price |

---

## CHAPTER 2: Object-Oriented Programming (Python 2) [FOUNDATIONAL REFRESHER]

### Core Concepts
- Classes, `__init__`, instance variables, methods
- Inheritance (basic structure)
- String formatting, format specifiers

### Key Patterns

**Class Template**
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None   # for linked list nodes

class Stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def is_empty(self):
        return len(self.data) == 0
```

**String Formatting**
```python
print(f"Value: {x:.2f}")   # 2 decimal places
print("{:>10}".format(s))  # right-align width 10
print("{:0>5}".format(n))  # zero-pad to width 5
```

### Chapter 2 Problems Summary
| Problem | Algorithm | Key Trick |
|---------|-----------|-----------|
| Roman Number | Dict lookup | Map int digits to Roman chars |
| Spherical | Math formula | 4/3 * pi * r^3 |
| New Range | List/loop | Filter within range |
| 3-SUM | Triple loop or sort | Find 3 numbers summing to 0 |
| Fun String | String manipulation | Process chars by position |

---

## CHAPTER 3: Stack (LIFO - Last In First Out) [*** QUIZ 1 FOCUS ***]

### Core Concepts
- LIFO structure: last element pushed is first popped
- Operations: push, pop, peek, is_empty
- Applications: bracket matching, expression conversion, undo systems

### Stack Implementation
```python
stack = []
stack.append(x)    # push - O(1)
stack.pop()        # pop - O(1)
stack[-1]          # peek - O(1)
len(stack) == 0    # is_empty
```

### Parentheses Matching - 4-Line Logic
```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
```

### Infix to Postfix Conversion
**Operator Precedence Table:**
| Operator | Precedence | Associativity |
|----------|-----------|---------------|
| ^ (power) | 3 | RIGHT (special!) |
| * / | 2 | LEFT |
| + - | 1 | LEFT |
| ( | 0 | - |

**Algorithm:**
1. If operand (number/letter) -> output directly
2. If `(` -> push to stack
3. If `)` -> pop until matching `(`
4. If operator -> pop while stack-top has HIGHER or EQUAL precedence (except `^` uses strictly higher)

```python
def infix_to_postfix(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_assoc = {'^'}
    output = []
    stack = []
    for token in expr.split():
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        else:
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   (precedence[stack[-1]] > precedence[token] or
                    (precedence[stack[-1]] == precedence[token] and token not in right_assoc))):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)
```

### Postfix Evaluation - 3-Step Logic
```python
def eval_postfix(expr):
    stack = []
    for token in expr.split():
        if token.lstrip('-').isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()   # IMPORTANT: b is popped FIRST
            a = stack.pop()   # a is popped SECOND
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
            elif token == '^': stack.append(a ** b)
    return stack[0]
```

### EXAM TRAPS - Chapter 3
1. **`^` is RIGHT-associative**: `a ^ b ^ c` = `a ^ (b ^ c)`, NOT `(a ^ b) ^ c`
2. **Empty stack check before pop**: Always check `if not stack` before `stack.pop()` to avoid IndexError
3. **Order of operands in postfix eval**: pop `b` first, then pop `a`; do `a op b`
4. **Stack Calculator operand order**: The actual code pops `x` (top) then `y` (second) and does `x - y` for subtraction. Verify this matches testcase specs.

### Chapter 3 Problems Summary
| Problem | Algorithm | Key Data Structure |
|---------|-----------|-------------------|
| Parentheses v1 | Bracket matching | Stack + dict |
| Parenthesis Matching | Balanced brackets | Stack |
| Infix to Postfix | Shunting-yard | Stack |
| Stack Calculator | Postfix eval | Stack |
| Parking Lot | Enter/exit simulation | Stack |

---

## CHAPTER 4: Queue (FIFO - First In First Out) [*** QUIZ 1 FOCUS ***]

### Core Concepts
- FIFO structure: first element enqueued is first dequeued
- Operations: enqueue, dequeue, peek, is_empty
- Applications: BFS, simulations, scheduling

### Queue Implementation - USE deque (O(1))
```python
from collections import deque

q = deque()
q.append(x)        # enqueue - O(1)
q.popleft()        # dequeue - O(1) *** USE THIS, NOT list.pop(0) ***
q[0]               # peek front - O(1)
len(q) == 0        # is_empty
```

### WARNING - O(N) Trap
```python
# WRONG - O(N) time - causes TLE on large inputs
lst = []
lst.append(x)
lst.pop(0)     # This is O(N)!

# CORRECT - O(1) time
from collections import deque
q = deque()
q.append(x)
q.popleft()    # This is O(1)
```

### Circular Queue
```python
class CircularQueue:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self): return self.size == 0
    def is_full(self):  return self.size == self.cap

    def enqueue(self, x):
        if self.is_full(): return False
        self.data[self.rear] = x
        self.rear = (self.rear + 1) % self.cap
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty(): return None
        val = self.data[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return val
```

**Circular Queue Key Equations:**
- Empty condition: `size == 0`
- Full condition: `size == capacity`
- Next index: `(index + 1) % capacity`

### BFS Template (Search Portal problem)
```python
from collections import deque

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    q = deque([(start, 0)])   # (position, distance)
    visited.add(start)
    while q:
        pos, dist = q.popleft()
        if pos == end: return dist
        for neighbor in get_neighbors(pos, rows, cols):
            if neighbor not in visited and grid[neighbor] != 'wall':
                visited.add(neighbor)
                q.append((neighbor, dist + 1))
    return -1
```

### EXAM TRAPS - Chapter 4
1. **list.pop(0) is O(N)** - always use `deque.popleft()` for O(1)
2. **Circular Queue uses modulo** - `(index + 1) % capacity`
3. **BFS uses Queue, DFS uses Stack** - don't mix them up
4. **Mark visited BEFORE enqueuing** - not after dequeuing, to avoid duplicates

### Chapter 4 Problems Summary
| Problem | Algorithm | Key Trick |
|---------|-----------|-----------|
| Basic Queue | FIFO operations | deque |
| Queue 2 | Queue with priority | deque + sort |
| Concept Queue | Circular queue | Modulo arithmetic |
| Cafe | Event simulation | Time-jumping |
| Search Portal | BFS grid | deque + visited set |

---

## CHAPTER 5: Linked List [*** QUIZ 1 FOCUS ***]

### Core Concepts
- Dynamic data structure with nodes connected by pointers
- Singly Linked List (SLL): each node has `next` pointer
- Doubly Linked List (DLL): each node has `next` AND `prev` (`previous`) pointer
- No random access (no indexing like arrays, linear O(N) traversal required)

---

### FULL IMPLEMENTATIONS FOR CHAPTER 5

#### 1. Singly Linked List (SLL)
Full implementation supporting `append`, `addHead`, `search`, `index`, `size`, and `pop(pos)`.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next is not None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, item):
        cur = self.head
        idx = 0
        while cur is not None:
            if cur.value == item:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if pos < 0 or self.isEmpty():
            return "Out of Range"
        if pos == 0:
            self.head = self.head.next
            return "Success"
        cur = self.head
        idx = 0
        while cur.next is not None and idx < pos - 1:
            cur = cur.next
            idx += 1
        if cur.next is None:
            return "Out of Range"
        cur.next = cur.next.next
        return "Success"
```

---

#### 2. Doubly Linked List (DLL)
Full implementation supporting `append`, `insert`, `remove`, and `str_reverse`.

```python
class Node:
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
        s = str(cur.data)
        while cur.next:
            cur = cur.next
            s += "->" + str(cur.data)
        return s

    def str_reverse(self):
        if self.isEmpty():
            return ""
        cur = self.tail
        s = str(cur.data)
        while cur.previous:
            cur = cur.previous
            s += "->" + str(cur.data)
        return s

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def insert(self, index, data):
        new_node = Node(data)
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

#### 3. Merge Two Sorted Linked Lists
Merging two ordered linked lists in ascending order without creating a wrapper LinkedList class or using built-in sort.

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

#### 4. VIM Text Editor Simulation
Doubly linked list with dummy head and dummy tail for cursor movements and character insertions/deletions.

```python
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
```

---

#### 5. Radix Sort in Descending Order using Linked List
Multi-digit Radix Sort using Linked List buckets (0-9). Positives are gathered from bucket 9 down to 0, while negatives are gathered from 0 up to 9.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def is_empty(self):
        return self.head is None

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
    if not arr:
        return
    before_list = LinkedList()
    for num in arr:
        before_list.append(num)

    max_abs_val = max(abs(x) for x in arr)
    max_digits = 0 if max_abs_val == 0 else len(str(max_abs_val))

    main_list = LinkedList()
    for num in arr:
        if num >= 0:
            main_list.append(num)
    for num in arr:
        if num < 0:
            main_list.append(num)

    for rnd in range(1, max_digits + 1):
        bins = [LinkedList() for _ in range(10)]
        cur = main_list.head
        while cur:
            val = cur.data
            digit = (abs(val) // (10 ** (rnd - 1))) % 10
            bins[digit].append(val)
            cur = cur.next

        main_list.clear()
        # Collect Positives (9 down to 0 for descending order)
        for i in range(9, -1, -1):
            cur = bins[i].head
            while cur:
                if cur.data >= 0:
                    main_list.append(cur.data)
                cur = cur.next

        # Collect Negatives (0 up to 9 for descending order)
        for i in range(10):
            cur = bins[i].head
            while cur:
                if cur.data < 0:
                    main_list.append(cur.data)
                cur = cur.next

    return before_list, main_list, max_digits
```

---

### CRITICAL: Pointer Reassignment Safety
```python
# WRONG - NoneType AttributeError
curr = self.head
curr = curr.next.next   # CRASH if curr.next is None

# CORRECT - Always check before accessing
if curr and curr.next:
    curr = curr.next.next
```

### EXAM TRAPS - Chapter 5
1. **Check `curr` and `curr.next` before traversal** - prevent NoneType crash
2. **Update BOTH `next` AND `prev` pointers** in doubly linked list operations
3. **Radix Sort descending** - gather positive buckets from index 9 down to 0, negative from 0 up to 9
4. **Tail pointer** - update when inserting at end or deleting tail node
5. **DLL delete** - also update predecessor's `next` and successor's `prev`

### Chapter 5 Problems Summary
| Problem | Algorithm | Key Challenge |
|---------|-----------|--------------|
| Singly Linked List | Linked list ops | Pointer management & indexing |
| Doubly Linked List | DLL insert/delete | Both prev and next pointers |
| Merge Order List | Merge sort merge | Two-pointer technique with dummy head |
| VIM Text Editor | DLL cursor sim | Insert/delete relative to cursor |
| Radix Sort Desc | Counting/bucket sort | Reverse bucket gather for descending |

---

## CHAPTER 6: Recursion

### Core Concepts
- Function calling itself with a smaller subproblem
- Must have: Base Case (stop condition) + Recursive Case
- Call stack grows with each recursive call

### Recursion Template
```python
def recursive_func(n):
    # Base case - ALWAYS define first
    if n <= 0:
        return 0
    # Recursive case
    return n + recursive_func(n - 1)
```

### Fibonacci
```python
# Naive - O(2^N) slow
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Memoized - O(N) fast
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1: return n
    return fib_memo(n-1) + fib_memo(n-2)
```

### GCD (Euclidean Algorithm)
```python
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

# Python built-in
import math
math.gcd(a, b)
```

### String Length (Recursive)
```python
def str_len(s):
    if s == '': return 0
    return 1 + str_len(s[1:])
```

### Tower of Hanoi
```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)
# Total moves = 2^n - 1
```

### Draw Stairs
```python
def draw_stairs(n, current=1):
    if current > n: return
    print('#' * current)
    draw_stairs(n, current + 1)
```

### EXAM TRAPS - Chapter 6
1. **Always define base case FIRST** - infinite recursion = RecursionError
2. **Fibonacci without memoization is O(2^N)** - very slow for large N
3. **Tower of Hanoi**: minimum moves = `2^n - 1`
4. **Recursion depth limit**: Python default is 1000; use `sys.setrecursionlimit(N)` if needed
5. **Stack overflow** from deep recursion - prefer iterative for N > 500

### Chapter 6 Problems Summary
| Problem | Algorithm | Key Formula |
|---------|-----------|-------------|
| Fibonacci Recursion | Divide & conquer | fib(n-1) + fib(n-2) |
| String Length | Linear recursion | 1 + len(s[1:]) |
| GCD | Euclidean algorithm | gcd(b, a%b) |
| Tower of Hanoi | Divide & conquer | 2^n - 1 total moves |
| Draw Stair | Linear recursion | Print then recurse |

---

## CHAPTER TEMPLATE (Copy for Future Chapters)

## CHAPTER X: <TITLE>

### Core Concepts
- Concept 1
- Concept 2

### Key Patterns

```python
# Code example here
```

### EXAM TRAPS - Chapter X
1. Trap 1
2. Trap 2

### Chapter X Problems Summary
| Problem | Algorithm | Key Trick |
|---------|-----------|-----------|
| Problem 1 | Algorithm | Trick |

---

## QUICK REFERENCE TABLE

| Chapter | Topic | Must-Know Pattern | Quiz 1 Status |
|---------|-------|-------------------|---------------|
| 1 | Python Basics | map(int, input().split()) | Refresher |
| 2 | OOP | class Node: __init__ | Refresher |
| 3 | Stack (LIFO) | stack.append / stack.pop | QUIZ 1 FOCUS |
| 4 | Queue (FIFO) | deque + popleft() | QUIZ 1 FOCUS |
| 5 | Linked List | SLL, DLL, Merge, VIM, Radix | QUIZ 1 FOCUS |
| 6 | Recursion | Base case first | Post-Quiz 1 |

---

## COMPLEXITY CHEAT SHEET

| Operation | List | deque | Linked List |
|-----------|------|-------|-------------|
| Append (end) | O(1) | O(1) | O(N)* |
| Pop (end) | O(1) | O(1) | O(N)* |
| Pop (front) | O(N) | O(1) | O(1) |
| Access by index | O(1) | O(N) | O(N) |
| Insert middle | O(N) | O(N) | O(1)** |

*O(1) with tail pointer  **O(1) with reference to node
