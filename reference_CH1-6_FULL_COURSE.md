# ðŸ“– KMITL Data Structures (01276122) - FULL COURSE SUMMARY (CHAPTERS 1 TO 6)

> **Complete Course Reference & Exam Guide**  
> **Coverage**: Chapters 1â€“6 (Python 1, Python 2, Stack, Queue, Linked List, Recursion)

---

## ðŸ“Œ Course Chapters Roadmap
* ðŸŸ¢ **Chapter 1: Python 1** (Input parsing, List comprehensions, Math formulas, Functions)
* ðŸŸ¢ **Chapter 2: Python 2** (Classes & OOP, Roman Numerals, Spherical Math, 3-SUM)
* ðŸŸ¢ **Chapter 3: Stack** (LIFO, Parentheses Matching, Infix to Postfix, Postfix Evaluation, Parking Lot)
* ðŸŸ¢ **Chapter 4: Queue** (FIFO, Circular Queue, Multi-Barista Cafe Simulation, BFS Search Portal)
* ðŸŸ¢ **Chapter 5: Linked List** (Singly & Doubly Linked List, Pointer Reassignment, Merge List, VIM Editor, Radix Sort)
* ðŸŸ¢ **Chapter 6: Recursion** (Fibonacci, String Length, GCD, Tower of Hanoi, Draw Stairs)

---


# Masterclass Quiz #1 Preparation Guide (KMITL Data Structure and Algorithms)
## Chapters 1 to 4: Python 1, Python 2, Stack, Queue

Welcome to the ultimate preparation guide for your first Data Structure and Algorithms quiz! This guide breaks down every core concept, algorithm, and simulation pattern you need to ace Chapters 1-4.

---

## 1. Complete Breakdown of Chapter 1 & 2 (Python 1 & 2)

### Input Parsing
In Python, reading standard input efficiently is key for programming questions.
- **Fast I/O:** `import sys; sys.stdin.read().split()` is highly recommended for reading all inputs quickly.
- `input().split()`: Reads a line, strips trailing/leading whitespaces, and splits by spaces into a list of strings.
- `list(map(int, input().split()))`: Automatically converts the split strings into integers.

### String Slicing
Python strings (and lists) support slicing: `sequence[start:stop:step]`
- `s[::-1]`: Reverses the string.
- `s[1:5]`: Slices from index 1 up to (but not including) index 5.

### List Comprehensions
A concise way to create lists.
- Syntax: `[expression for item in iterable if condition]`
- Example: `[x*2 for x in range(10) if x % 2 == 0]` -> `[0, 4, 8, 12, 16]`

### Math Formulas & Built-ins
- Division: `/` (float division), `//` (integer/floor division), `%` (modulo/remainder).
- Exponentiation: `**` (e.g., `2**3` is 8).

### OOP Class Structure
Classes encapsulate data (attributes) and behavior (methods).
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)
```

### Custom Exceptions
You can define your own error types to make debugging easier.
```python
class StackUnderflowError(Exception):
    pass

if stack.is_empty():
    raise StackUnderflowError("Cannot pop from an empty stack")
```

### Output Formatting
Format floating-point numbers to specific decimal places using f-strings.
- `print(f"{value:.2f}")`: Prints `value` rounded to 2 decimal places.

---

## 2. Complete Breakdown of Chapter 3 (Stack)

### LIFO Principles
Stack follows **Last In, First Out (LIFO)**. The last element added is the first one removed.
Operations: `push` (add), `pop` (remove), `peek` / `top` (view top element), `is_empty`, `size`.

### Parentheses Matching Algorithm
Use a stack to check if brackets `()`, `{}`, `[]` are balanced.
1. Iterate through the string.
2. If opening bracket, `push` to stack.
3. If closing bracket, check if stack is empty (Invalid) or if `pop()` matches the closing bracket type.
4. At the end, stack must be empty for it to be valid.

### Infix to Postfix Conversion
Rules for precedence: `^` (highest), `* /` (medium), `+ -` (lowest).
Associativity: Left-to-Right for all except `^` (Right-to-Left).
Algorithm:
1. Operand: Output directly.
2. `(` : Push to stack.
3. `)` : Pop to output until `(` is encountered.
4. Operator: Pop to output all operators with **greater or equal** precedence (if left-associative). For right-associative operators like `^`, pop operators with strictly **greater** precedence. Then push the new operator.

### Postfix Evaluation Algorithm
1. Read from left to right.
2. Operand: Push to stack.
3. Operator: Pop two operands (let's say `A` then `B`, so `B op A`), compute the result, and push it back.
4. Final result is the only item left in the stack.

### Parking Lot Simulation Pattern
Often involves two stacks (or a stack and a temporary queue) to move cars out of the way for a specific car to exit, and then return them in the same order.

---

## 3. Complete Breakdown of Chapter 4 (Queue)

### FIFO Principles
Queue follows **First In, First Out (FIFO)**. Elements are added at the rear and removed from the front.
Operations: `enqueue` (add), `dequeue` (remove), `front`, `is_empty`, `size`.

### Linear vs Circular Queue Implementation
- **Linear Queue**: Using a list where `enqueue` is `append()` and `dequeue` is `pop(0)`. (Inefficient for large queues). **Explicit Requirement:** Use `collections.deque.popleft()` for O(1) performance instead of O(N) `list.pop(0)`.
- **Circular Queue**: Uses a fixed-size array and modulo wrapping to reuse spaces.
  - `rear = (rear + 1) % capacity`
  - `front = (front + 1) % capacity`
  - **State equations:** Empty when `size == 0` vs Full when `(rear + 1) % capacity == front`.

### Multi-Barista / Cafe Queue Simulation Pattern
Simulates multiple servers (baristas) processing a queue of customers.
- Keep track of each server's busy time.
- When a server is free, assign the next customer from the queue.
- **Event-driven time-jumping:** Advance time to the next available server's finishing time instead of step-by-step to optimize.

### Search Portal / BFS Pattern
Queues are the core data structure for **Breadth-First Search (BFS)**.
- Start at node, enqueue it.
- While queue not empty, dequeue node, check condition, enqueue all unvisited neighbors.

---

## 4. Comprehensive Code Cheat Sheets

### Stack Implementation
```python
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
```

### Queue Implementation
```python
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
```

### Parentheses Matching
```python
def is_balanced(expr):
    s = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in '({[':
            s.push(char)
        elif char in ')}]':
            if s.is_empty() or s.pop() != pairs[char]:
                return False
    return s.is_empty()
```

---

## 5. Common Exam Pitfalls & Edge Cases

1. **Popping from empty structures:** Always check `is_empty()` before `pop()` or `dequeue()`. Otherwise, you'll encounter `IndexError`.
2. **Operator Precedence in Postfix:** Remember that `*` and `/` have the same precedence. `+` and `-` have the same precedence. Pop from stack if top element precedence `>=` current operator precedence.
3. **String Formatting:** Remember `.2f` rounds, but some questions might ask for truncation instead of rounding. Read instructions carefully!
4. **List Modification During Iteration:** Avoid `for item in my_list: my_list.remove(item)`. Iterate over a copy (`my_list[:]`) or use list comprehensions instead.
5. **Division in Evaluation:** In postfix evaluation, if you pop `A` then `B`, the operation is `B / A`, not `A / B`. Order matters for `-` and `/`.
6. **Linked List Operations:** Ensure pointer reassignment safety. Always check head/tail single-node boundary handling.

---

## 6. 10 Practice Exam Questions with Step-by-Step Solutions

**Q1: Write a list comprehension to get all numbers from 1 to 50 that are divisible by 3 but not by 5.**
*Solution:*
```python
ans = [x for x in range(1, 51) if x % 3 == 0 and x % 5 != 0]
```

**Q2: Given an input string "10 20 30", parse it into a list of integers and print the sum.**
*Solution:*
```python
nums = list(map(int, "10 20 30".split()))
print(sum(nums)) # Output: 60
```

**Q3: Check if the string `"(([]))"` is balanced.**
*Solution:* 
Iterate left to right. Push `(`, `(`, `[`. Read `]`, pop `[` (match). Read `)`, pop `(` (match). Read `)`, pop `(` (match). Stack empty. Valid.

**Q4: Convert `A + B * C` to postfix.**
*Solution:*
- Read `A`: Output `A`.
- Read `+`: Push `+`.
- Read `B`: Output `AB`.
- Read `*`: `*` > `+`, Push `*`. Stack: `+ *`.
- Read `C`: Output `ABC`.
- End: Pop all. Output: `ABC*+`.

**Q5: Evaluate postfix `5 3 + 8 2 / *`.**
*Solution:*
- Push 5, Push 3.
- `+`: Pop 3, Pop 5. `5+3=8`. Push 8.
- Push 8, Push 2.
- `/`: Pop 2, Pop 8. `8/2=4`. Push 4.
- `*`: Pop 4, Pop 8. `8*4=32`. Push 32.
- Result: 32.

**Q6: What is the issue with implementing a Queue using a standard Python list's `pop(0)`?**
*Solution:* `pop(0)` takes O(n) time because all subsequent elements must be shifted left by one index. A circular queue or `collections.deque` solves this by providing O(1) operations.

**Q7: Print the number 3.14159 to two decimal places.**
*Solution:*
```python
pi = 3.14159
print(f"{pi:.2f}") # Output: 3.14
```

**Q8: Implement a Queue using two Stacks.**
*Solution:*
```python
class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
        
    def enqueue(self, item):
        self.in_stack.push(item)
        
    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
```

**Q9: Explain Circular Queue modulo arithmetic for `enqueue`.**
*Solution:* `self.rear = (self.rear + 1) % self.max_size`. This ensures that when `rear` reaches the end of the list array, it wraps back around to index 0, reusing empty spaces created by `dequeue`.

**Q10: In a Cafe Queue Simulation, if Barista 1 finishes at time=5 and Barista 2 finishes at time=7, and a new customer arrives at time=3, when will the customer be served and by whom?**
*Solution:* The customer arrives at 3 but both baristas are busy. The customer waits until time=5 when Barista 1 becomes available. Wait time = 5 - 3 = 2. Served by Barista 1.

---
*Good luck with your Masterclass Quiz #1! Keep calm and trust your data structures!*



