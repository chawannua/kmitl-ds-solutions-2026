# KMITL Data Structures & Algorithms (01276122)
# Ultimate Quiz 1 Preparation Guide - Chapters 1 to 4
# Target Date: Monday, August 2026
# Coverage: Chapter 1 (Python 1), Chapter 2 (Python 2), Chapter 3 (Stack), Chapter 4 (Queue)
# Encoding: UTF-8 plain ASCII - no emoji

---

## TABLE OF CONTENTS
1. Core Python Fundamentals (Ch 1 & 2)
2. Stack Data Structure (Ch 3)
3. Queue Data Structure (Ch 4)
4. Must-Know Exam Algorithms & Code Patterns
5. Top 5 Tricky Exam Pitfalls & Edge Cases

---

## 1. CORE PYTHON FUNDAMENTALS (Ch 1 & 2)

### Input Parsing & One-Liners
```python
# Single integer
n = int(input())

# Multiple integers on one line
a, b = map(int, input().split())

# Multiple floats
d, Vr, Vt, Vf = map(float, input().split())

# Array of integers
arr = list(map(int, input().split()))

# Split by comma
items = input().split(',')
```

### List Comprehensions
```python
# Filter odd numbers
odds = [x for x in numbers if x % 2 != 0]

# Convert strings to ints
arr = [int(x) for x in input().split()]

# Generate squares
squares = [x**2 for x in range(1, n+1)]
```

### String Slicing & Formatting
```python
s[::-1]        # Reverse string
s[1:]          # All chars except first
s[:-1]         # All chars except last
s[i:j]         # Substring from i to j-1

print(f"{ans:.2f}")    # 2 decimal places
print(f"{val:.4f}")    # 4 decimal places
print("{:>10}".format(s))   # Right-align width 10
```

### OOP - Class Blueprint
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} speaks"

    def __str__(self):
        return f"Animal: {self.name}"

a = Animal("Dog", "Mammal")
print(a.speak())
```

### Math Helpers
```python
import math

math.sqrt(x)        # square root
math.floor(x)       # round down
math.ceil(x)        # round up
math.gcd(a, b)      # greatest common divisor
math.pi             # 3.14159...
abs(x)              # absolute value
x ** 2              # power
x % 2 == 0          # even check
max(a, b)           # maximum
min(a, b)           # minimum
```

---

## 2. STACK DATA STRUCTURE - Ch 3 (LIFO)

### Stack: Key Facts
- LIFO = Last In First Out
- push = add to top
- pop = remove from top
- peek = look at top without removing
- All operations are O(1)

### Stack Implementation
```python
stack = []
stack.append(x)    # push - O(1)
stack.pop()        # pop - O(1)   ** check not empty first **
stack[-1]          # peek - O(1)
len(stack) == 0    # is_empty
not stack          # is_empty (Pythonic)
```

### Parentheses / Bracket Matching
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
Operator Precedence:
- ^ (power): 3  [RIGHT-associative - special!]
- * /: 2  [LEFT-associative]
- + -: 1  [LEFT-associative]
- (: 0

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
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   (precedence[stack[-1]] > precedence[token] or
                    (precedence[stack[-1]] == precedence[token]
                     and token not in right_assoc))):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)
```

### Postfix Evaluation
```python
def eval_postfix(expr):
    stack = []
    for token in expr.split():
        if token.lstrip('-').isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()   # pop b FIRST
            a = stack.pop()   # pop a SECOND
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
            elif token == '^': stack.append(a ** b)
    return stack[0]
```

### Stack - Top 3 Exam Traps
1. ^ is RIGHT-associative: a^b^c = a^(b^c), NOT (a^b)^c
2. Always check `if not stack` before `stack.pop()` to avoid IndexError
3. In postfix eval: pop b first, then a -> compute a op b

---

## 3. QUEUE DATA STRUCTURE - Ch 4 (FIFO)

### Queue: Key Facts
- FIFO = First In First Out
- enqueue = add to back
- dequeue = remove from front
- All operations must be O(1)

### Queue Implementation - USE deque (NOT list)
```python
from collections import deque

q = deque()
q.append(x)        # enqueue rear - O(1)
q.popleft()        # dequeue front - O(1)
q[0]               # peek front - O(1)
len(q) == 0        # is_empty
not q              # is_empty (Pythonic)
```

### CRITICAL WARNING - Avoid This Trap
```python
# WRONG - O(N) time - causes Time Limit Exceeded
lst = []
lst.pop(0)   # This shifts ALL elements - O(N)!

# CORRECT - O(1) time
from collections import deque
q = deque()
q.popleft()  # This is O(1)!
```

### Circular Queue
```python
class CircularQueue:
    def __init__(self, cap):
        self.cap = cap
        self.data = [None] * cap
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

Circular Queue Equations:
- Empty: size == 0
- Full: size == capacity
- Next index: (index + 1) % capacity

### BFS Template (Search Portal)
```python
from collections import deque

def bfs(grid, start, end):
    visited = set([start])
    q = deque([(start, 0)])
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        for neighbor in get_neighbors(pos):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))
    return -1
```

### Queue - Top 3 Exam Traps
1. list.pop(0) is O(N) - always use deque.popleft() for O(1)
2. Mark nodes VISITED before enqueuing, not after dequeuing
3. BFS uses Queue; DFS uses Stack - do not mix them up

---

## 4. MUST-KNOW EXAM ALGORITHMS

### Algorithm: Parking Lot (Stack simulation)
```python
def parking_lot(sequence):
    stack = []
    for action, car in sequence:
        if action == 'in':
            stack.append(car)
        elif action == 'out':
            temp = []
            while stack and stack[-1] != car:
                temp.append(stack.pop())
            if stack:
                stack.pop()  # remove target car
            stack.extend(reversed(temp))  # restore others
```

### Algorithm: Cafe Simulation (Event-Driven Queue)
```python
from collections import deque

def cafe_simulation(orders, baristas):
    q = deque(orders)
    times = [0] * baristas  # finish time per barista
    while q:
        order = q.popleft()
        earliest = min(times)
        idx = times.index(earliest)
        times[idx] = max(times[idx], order['arrive']) + order['duration']
    return max(times)
```

---

## 5. TOP 5 TRICKY EXAM PITFALLS

| # | Pitfall | Correct Approach |
|---|---------|-----------------|
| 1 | list.pop(0) is O(N) | Use deque.popleft() - O(1) |
| 2 | ^ is right-associative | a^b^c = a^(b^c) |
| 3 | stack.pop() on empty stack | Always check: if not stack |
| 4 | Circular queue uses modulo | (index + 1) % capacity |
| 5 | BFS marks visited BEFORE enqueue | Set visited.add() before q.append() |

---

## QUICK COMPLEXITY REFERENCE

| Operation | List | deque | Stack |
|-----------|------|-------|-------|
| Append end | O(1) | O(1) | O(1) push |
| Pop end | O(1) | O(1) | O(1) pop |
| Pop front | O(N) | O(1) | N/A |
| Peek | O(1) | O(1) | O(1) |

---
## NOTES FOR FUTURE UPDATES
- Add new algorithms under the relevant chapter section (## 2, ## 3, ## 4)
- Keep all text plain ASCII - no emoji characters
- Run the clean_ascii_safe.ps1 script after any edit to re-verify encoding
