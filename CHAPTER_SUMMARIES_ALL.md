# KMITL Data Structures & Algorithms - All Chapter Summaries
# Course: 01276122 | Student ID: 68011309
# Last Updated: 2026-08-08
# Format: Markdown (UTF-8, no emoji - safe for all terminals)

---

## HOW TO UPDATE THIS FILE
- Each chapter has a clearly marked section header: `## CHAPTER X: <TITLE>`
- To add new topics, append under the correct chapter section
- To add new chapters (e.g., Chapter 7+), copy the chapter template at the bottom
- Keep code blocks inside triple backticks with language tag: ```python
- Use plain ASCII characters only - NO emoji to avoid encoding issues

---

## CHAPTER 1: Python Basics (Python 1)

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

## CHAPTER 2: Object-Oriented Programming (Python 2)

### Core Concepts
- Classes, `__init__`, instance variables, methods
- Inheritance (not heavily tested)
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

## CHAPTER 3: Stack (LIFO - Last In First Out)

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
4. **Stack Calculator (item_4) operand order**: The actual code pops `x` (top) then `y` (second) and does `x - y` for subtraction. Verify this matches KMITL judge expected output before exam.

### Chapter 3 Problems Summary
| Problem | Algorithm | Key Data Structure |
|---------|-----------|-------------------|
| Parentheses v1 | Bracket matching | Stack + dict |
| Parenthesis Matching | Balanced brackets | Stack |
| Infix to Postfix | Shunting-yard | Stack |
| Stack Calculator | Postfix eval | Stack |
| Parking Lot | Enter/exit simulation | Stack |

---

## CHAPTER 4: Queue (FIFO - First In First Out)

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

## CHAPTER 5: Linked List

### Core Concepts
- Dynamic data structure with nodes connected by pointers
- Singly Linked List: each node has `next` pointer
- Doubly Linked List: each node has `next` AND `prev` pointer
- No random access (no indexing like arrays)

### Node Classes
```python
class SinglyNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
```

### Singly Linked List - Core Operations
```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):          # Add to end - O(N)
        new = SinglyNode(val)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def prepend(self, val):         # Add to front - O(1)
        new = SinglyNode(val)
        new.next = self.head
        self.head = new

    def delete(self, val):          # Delete node - O(N)
        if not self.head: return
        if self.head.val == val:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.val != val:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
```

### CRITICAL: Pointer Reassignment Safety
```python
# WRONG - NoneType AttributeError
curr = self.head
curr = curr.next.next   # CRASH if curr.next is None

# CORRECT - Always check before accessing
if curr and curr.next:
    curr = curr.next.next
```

### Doubly Linked List - Insert After Node
```python
def insert_after(self, target_node, val):
    new = DoublyNode(val)
    new.next = target_node.next
    new.prev = target_node
    if target_node.next:
        target_node.next.prev = new
    target_node.next = new
    if new.next is None:
        self.tail = new
```

### Merge Two Sorted Linked Lists
```python
def merge_sorted(l1, l2):
    dummy = SinglyNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next
```

### Radix Sort (Descending) - Bucket Distribution
```python
def radix_sort_desc(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        # Gather in REVERSE order for descending
        arr = []
        for i in range(9, -1, -1):   # 9 down to 0
            arr.extend(buckets[i])
        exp *= 10
    return arr
```

### EXAM TRAPS - Chapter 5
1. **Check `curr` and `curr.next` before traversal** - prevent NoneType crash
2. **Update BOTH `next` AND `prev` pointers** in doubly linked list
3. **Radix Sort descending** - gather buckets from index 9 down to 0
4. **Tail pointer** - update when inserting at end or deleting tail node
5. **DLL delete** - also update predecessor's `next` and successor's `prev`

### Chapter 5 Problems Summary
| Problem | Algorithm | Key Challenge |
|---------|-----------|--------------|
| Singly Linked List | Linked list ops | Pointer management |
| Doubly Linked List | DLL insert/delete | Both prev and next |
| Merge Order List | Merge sort merge | Two-pointer technique |
| VIM Text Editor | DLL cursor sim | Insert/delete at cursor |
| Radix Sort Desc | Counting/bucket sort | Reverse bucket gather |

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

| Chapter | Topic | Must-Know Pattern |
|---------|-------|-------------------|
| 1 | Python Basics | map(int, input().split()) |
| 2 | OOP | class Node: __init__ |
| 3 | Stack (LIFO) | stack.append / stack.pop |
| 4 | Queue (FIFO) | deque + popleft() |
| 5 | Linked List | Pointer safety check |
| 6 | Recursion | Base case first |

## COMPLEXITY CHEAT SHEET

| Operation | List | deque | Linked List |
|-----------|------|-------|-------------|
| Append (end) | O(1) | O(1) | O(N)* |
| Pop (end) | O(1) | O(1) | O(N)* |
| Pop (front) | O(N) | O(1) | O(1) |
| Access by index | O(1) | O(N) | O(N) |
| Insert middle | O(N) | O(N) | O(1)** |

*O(1) with tail pointer  **O(1) with reference to node
