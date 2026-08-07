# ðŸ“˜ KMITL Data Structures & Algorithms (01276122)
## ðŸš€ Ultimate Quiz #1 Preparation & Quick Study Guide (Chapters 1â€“4)
**Target Date**: Monday, August 10, 2026  
**Coverage**: Chapter 1 (Python 1), Chapter 2 (Python 2), Chapter 3 (Stack), Chapter 4 (Queue)  

---

# ðŸ“Œ Quick Cheat Sheet Table of Contents
1. [Core Python Fundamentals (Ch 1 & 2)](#1-core-python-fundamentals-ch-1--2)
2. [Stack Data Structure (Ch 3)](#2-stack-data-structure-ch-3)
3. [Queue Data Structure (Ch 4)](#3-queue-data-structure-ch-4)
4. [Must-Know Exam Algorithms & Code Patterns](#4-must-know-exam-algorithms--code-patterns)
5. [Top 5 Tricky Exam Pitfalls & Edge Cases](#5-top-5-tricky-exam-pitfalls--edge-cases)

---

# 1. Core Python Fundamentals (Ch 1 & 2)

### ðŸ”¹ Input Parsing & One-Liners
* **Parsing multiple inputs**:
  ```python
  # Split input by spaces and cast to int/float
  d, Vr, Vt, Vf = map(float, input("Enter Input : ").split())
  
  # Split by custom delimiter (e.g. comma)
  items = input("Enter Input : ").split(',')
  ```
* **List Comprehensions**:
  ```python
  # Filter odd numbers
  odds = [x for x in numbers if x % 2 != 0]
  
  # Convert array of strings to ints
  arr = [int(x) for x in input().split()]
  ```

### ðŸ”¹ String Slicing & Formatting
* **Formatting float outputs**:
  ```python
  print(f"{ans:.2f}")  # 2 decimal places (e.g. 3000.00)
  ```
* **String slicing tricks**:
  ```python
  s[::-1]        # Reverse string
  s[1:]          # All characters except first
  s[:-1]         # All characters except last
  ```

### ðŸ”¹ OOP (Classes & Methods)
* **Custom Class Blueprint**:
  ```python
  class Stack:
      def __init__(self, items=None):
          self.items = items if items is not None else []
          
      def push(self, item):
          self.items.append(item)
          
      def pop(self):
          if not self.is_empty():
              return self.items.pop()
          return None
          
      def is_empty(self):
          return len(self.items) == 0
          
      def size(self):
          return len(self.items)
          
      def peek(self):
          return self.items[-1] if not self.is_empty() else None
          
      def __str__(self):
          return " ".join(map(str, self.items))
  ```

---

# 2. Stack Data Structure (Ch 3)

### ðŸ”‘ Core Principle: **LIFO (Last-In, First-Out)**
The last element added (`push`) is the first element to be removed (`pop`).

| Operation | Description | Time Complexity | Python Equivalent |
| :--- | :--- | :---: | :--- |
| `push(item)` | Add item to top of stack | $O(1)$ | `list.append(item)` |
| `pop()` | Remove and return top item | $O(1)$ | `list.pop()` |
| `peek()` / `top()` | View top item without removing | $O(1)$ | `list[-1]` |
| `is_empty()` | Check if stack contains 0 items | $O(1)$ | `len(list) == 0` |
| `size()` | Count total items in stack | $O(1)$ | `len(list)` |

---

### ðŸ’¡ Stack Application 1: Parentheses Matching
Used to check if brackets `()`, `[]`, `{}` are balanced.

```python
def is_parentheses_matched(expression):
    stack = []
    open_brackets = "([{"
    close_brackets = ")]}"
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack or stack[-1] != mapping[char]:
                return False  # Unmatched or empty stack mismatch
            stack.pop()
            
    return len(stack) == 0  # True if no leftover opening brackets
```

---

### ðŸ’¡ Stack Application 2: Infix to Postfix Conversion
Convert human-readable math expressions (e.g. `A + B * C`) to Postfix (e.g. `A B C * +`).

#### **Operator Precedence Rules**:
1. `^` (Power) $\rightarrow$ Precedence **3** (Right-associative)
2. `*`, `/` $\rightarrow$ Precedence **2** (Left-associative)
3. `+`, `-` $\rightarrow$ Precedence **1** (Left-associative)

```python
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Pop '('
        else:  # Operator
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)
            
    while stack:
        output.append(stack.pop())
        
    return "".join(output)
```

---

### ðŸ’¡ Stack Application 3: Postfix Expression Evaluation
Evaluate math operations directly using a Stack.

```python
def evaluate_postfix(postfix_expr):
    stack = []
    
    for token in postfix_expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
            elif token == '^': stack.append(a ** b)
            
    return stack.pop()
```

---

# 3. Queue Data Structure (Ch 4)

### ðŸ”‘ Core Principle: **FIFO (First-In, First-Out)**
The first element added (`enqueue`) is the first element to be removed (`dequeue`).

| Operation | Description | Time Complexity | Python List Equivalent | Efficient `collections.deque` |
| :--- | :--- | :---: | :--- | :--- |
| `enqueue(item)` | Add item to rear of queue | $O(1)$ | `list.append(item)` | `deque.append(item)` |
| `dequeue()` | Remove and return front item | $O(1)^*$ | `list.pop(0)` *(O(N))* | `deque.popleft()` *(O(1))* |
| `front()` | View front item without removing | $O(1)$ | `list[0]` | `deque[0]` |
| `is_empty()` | Check if queue is empty | $O(1)$ | `len(list) == 0` | `len(deque) == 0` |

---

### ðŸ’¡ Circular Queue Implementation
Prevents memory waste by wrapping around indices using modulo `% capacity`.

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        
    def enqueue(self, item):
        if self.size == self.capacity:
            return "Queue Full!"
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        
    def dequeue(self):
        if self.size == 0:
            return "Queue Empty!"
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
```

---

# 4. Must-Know Exam Algorithms & Code Patterns

### ðŸ¢ 1. Parking Lot Simulation (Stack)
* **Rules**: Cars parked in a single-lane driveway (Stack). To remove car $X$, all cars parked after $X$ must be temporarily popped into an auxiliary stack, car $X$ leaves, and then temporary cars are pushed back.

```python
def park_lot_remove(car_stack, target_car):
    temp_stack = []
    found = False
    
    while car_stack:
        car = car_stack.pop()
        if car == target_car:
            found = True
            break
        temp_stack.append(car)
        
    # Restore cars back to original stack
    while temp_stack:
        car_stack.append(temp_stack.pop())
        
    return found
```

---

### â˜• 2. Multi-Barista / Multi-Cashier Queue Simulation
* **Rules**: Customers arrive in order. Route customer to whichever cashier becomes free first.

```python
def simulate_cafe(customers, baristas_count):
    # baristas stores remaining busy time for each barista
    baristas = [0] * baristas_count
    time = 0
    
    for order_time in customers:
        # Find first available barista (min busy time)
        min_idx = baristas.index(min(baristas))
        if baristas[min_idx] > 0:
            time += baristas[min_idx]
            # Reduce time for all
            baristas = [max(0, b - baristas[min_idx]) for b in baristas]
        baristas[min_idx] = order_time
```

---

# 5. Top 5 Tricky Exam Pitfalls & Edge Cases

1. **Popping from an Empty Stack/Queue**:
   - âš ï¸ *Mistake*: Calling `stack.pop()` when `len(stack) == 0` causes `IndexError: pop from empty list`.
   - âœ… *Fix*: Always check `if stack:` or `if not stack.is_empty():` before popping.

2. **Infix to Postfix Operator Precedence**:
   - âš ï¸ *Mistake*: Forgetting that `(` has precedence inside the stack until `)` is encountered.
   - âœ… *Fix*: When encountering `(`, push to stack. When encountering `)`, pop everything until `(` is popped.

3. **String Modulo & Floating Point Precision**:
   - âš ï¸ *Mistake*: Outputting `3000.0` instead of `3000.00`.
   - âœ… *Fix*: Use `f"{value:.2f}"`.

4. **Python `pop(0)` Efficiency**:
   - âš ï¸ *Mistake*: Using `list.pop(0)` in large loops can cause Time Limit Exceeded (TLE) because shifting items is $O(N)$.
   - âœ… *Fix*: Use `from collections import deque` and `deque.popleft()` for $O(1)$ queue operations.

5. **Modifying List While Iterating**:
   - âš ï¸ *Mistake*: `for item in queue: queue.remove(item)` skips elements!
   - âœ… *Fix*: Iterate over a copy (`for item in list(queue):`) or use `while queue:`.

---

## ðŸŽ¯ Quick Self-Test Practice Questions
Try answering these before Monday!

1. **Q1**: What is the output of Postfix expression `5 3 2 * + 4 -`?
   - *Answer*: `5 + (3 * 2) - 4` = `5 + 6 - 4` = **`7`**.
2. **Q2**: Which data structure is used by the browser Back/Forward button?
   - *Answer*: **Two Stacks** (Back stack and Forward stack).
3. **Q3**: In a Circular Queue of capacity 5 with `front = 4` and `size = 3`, what is `rear` index?
   - *Answer*: `(front + size) % capacity` = `(4 + 3) % 5` = **`2`**.

---
*Good luck on Monday's Quiz! You've got this! ðŸ’¯*


