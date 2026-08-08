# DATA STRUCTURES QUIZ 1 - 5-MINUTE CHEAT SHEET
# READ THIS RIGHT BEFORE ENTERING THE EXAM
# Encoding: Plain ASCII format

---

## CH 1 & 2: PYTHON ESSENTIALS & OOP (REFRESHER)

### 1. Fast Input Parsing
```python
# Single or multiple space-separated integers
a, b = map(int, input().split())
nums = list(map(int, input().split()))

# List comprehension parsing
arr = [int(x) for x in input().split()]
```

### 2. Slicing Syntax: list_or_str[start:end:step]
- `s[::-1]`    : Reverses string or list
- `s[1:4]`     : Substring/sublist from index 1 to 3 (end index 4 is EXCLUSIVE)
- `s[1:]`      : All elements except the first (index 0)
- `s[:-1]`     : All elements except the last

### 3. List Comprehensions
```python
evens = [x for x in range(10) if x % 2 == 0]      # [0, 2, 4, 6, 8]
pairs = [(x, y) for x in range(2) for y in range(2)]
```

### 4. OOP Class Template
```python
class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return str(self.val)
```

---

## CH 3: STACK (LIFO - LAST IN, FIRST OUT)

### 1. Parentheses Matching Algorithm
```python
def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0
```

### 2. Infix to Postfix Conversion & Precedence Table
| Operator | Precedence | Associativity | Pop Condition from Stack |
|----------|------------|---------------|--------------------------|
| ^        | 3          | RIGHT         | Pop while top prec > current prec |
| * /      | 2          | LEFT          | Pop while top prec >= current prec |
| + -      | 1          | LEFT          | Pop while top prec >= current prec |
| (        | 0          | N/A           | Stop popping |

- KEY RULE FOR `^` (RIGHT-ASSOCIATIVE):
  - `a^b^c` evaluates as `a^(b^c)`.
  - When scanner sees `^`, DO NOT pop existing `^` from stack because precedence is equal.
- Parentheses Rules:
  - `(` is pushed to stack immediately.
  - `)` pops all operators to output until `(` is popped.

### 3. Postfix Evaluation (3 Critical Steps)
```python
# When encountering an operator 'op':
b = stack.pop()       # Step 1: Pop second operand FIRST (b)
a = stack.pop()       # Step 2: Pop first operand SECOND (a)
res = eval_op(a, b)   # Step 3: Evaluate (a op b) -- Order matters for -, /, ^ !
stack.append(res)     # Push result back to stack
```

---

## CH 4: QUEUE (FIFO - FIRST IN, FIRST OUT)

### 1. Python implementation: deque vs list
- DO NOT use `list.pop(0)`: Takes O(N) time due to elements left-shifting!
- DO use `collections.deque`: Both `append()` and `popleft()` are O(1).
```python
from collections import deque
q = deque()
q.append(val)      # Enqueue: O(1)
val = q.popleft()  # Dequeue: O(1)
```

### 2. Circular Queue Equations
Given fixed capacity array/list `arr` of size `capacity`:
- Empty Condition: `size == 0`
- Full Condition : `size == capacity`
- Enqueue Pointer Update: `rear = (rear + 1) % capacity`
- Dequeue Pointer Update: `front = (front + 1) % capacity`
- Size calculation (without size variable): `(rear - front + capacity) % capacity`

### 3. BFS (Breadth-First Search) Template
```python
from collections import deque

def bfs(start, target, get_neighbors):
    q = deque([(start, 0)])      # (current_node, distance/step)
    visited = set([start])        # Mark visited AT ENQUEUE time!
    
    while q:
        curr, dist = q.popleft()
        if curr == target:
            return dist
            
        for nxt in get_neighbors(curr):
            if nxt not in visited:
                visited.add(nxt)  # MUST mark before appending!
                q.append((nxt, dist + 1))
    return -1
```

---

## CH 5: LINKED LIST

### 1. Singly vs Doubly Linked List Comparison
- Singly Linked List:
  - Node has `data` and `next`.
  - Memory overhead: 1 pointer per node.
  - Traversal: One-way forward (`head` to `tail`).
  - Search/Delete: O(N) to find `prev` node before deleting.
- Doubly Linked List:
  - Node has `data`, `prev`, and `next`.
  - Memory overhead: 2 pointers per node.
  - Traversal: Two-way forward and backward.
  - Deletion given node reference: O(1) without needing `prev` traversal.

### 2. Pointer Updates for Insertion and Deletion

#### Singly Linked List:
```python
# Insert new_node after prev_node:
new_node.next = prev_node.next
prev_node.next = new_node

# Delete target node after prev_node:
prev_node.next = target.next
```

#### Doubly Linked List:
```python
# Insert new_node between node_A and node_B:
new_node.prev = node_A
new_node.next = node_B
node_A.next = new_node
node_B.prev = new_node

# Delete node (with dummy head/tail or non-null prev/next):
node.prev.next = node.next
node.next.prev = node.prev
```

### 3. Merge Two Sorted Linked Lists (Dummy Head Trick)
```python
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        
    tail.next = l1 if l1 else l2
    return dummy.next
```

### 4. Radix Sort Using Buckets (LSD Radix Sort)
- Non-comparative sorting using 10 buckets (queues/lists indexed 0-9).
- Algorithm steps:
  1. Find maximum number to determine digit count.
  2. For `exp = 1, 10, 100, ...` (Least Significant Digit to Most Significant):
     a. Place each number into bucket corresponding to `(num // exp) % 10`.
     b. Flatten/collect all buckets back into list in FIFO order.
- Time Complexity: O(d * (N + k)) where d is max digits, k is radix (10).

---

## TOP 10 MUST-REMEMBER RULES FOR QUIZ 1

1. DEQUE OVER LIST: Never use list.pop(0) (O(N)); always use collections.deque.popleft() (O(1)).
2. EXPONENTIATION ASSOCIATIVITY: Operator ^ is right-associative (a^b^c = a^(b^c)). In infix-to-postfix, do NOT pop top ^ when scanning ^.
3. POSTFIX OPERAND ORDER: In postfix evaluation, pop b first, pop a second, then compute (a op b). Order is critical for subtraction and division.
4. STACK UNDERFLOW CHECK: Always check `if not stack` before reading stack[-1] or calling stack.pop() to prevent IndexError.
5. CIRCULAR QUEUE MODULO: Wrap head/tail pointers using `(ptr + 1) % capacity`.
6. BFS VISITED TIMING: Mark node in visited set BEFORE enqueuing, not when dequeuing, to prevent duplicate queue items.
7. SINGLY LIST DELETION PREV: To delete node in a singly linked list, you MUST maintain reference to prev node (`prev.next = curr.next`).
8. DOUBLY LIST POINTER ORDER: When inserting into doubly linked list, wire new node's prev and next links FIRST before updating adjacent pointers.
9. MERGE LIST DUMMY NODE: Use a dummy head node (`dummy = Node(0)`) to eliminate edge-case checks for head updates.
10. RADIX SORT STABILITY: Radix sort requires FIFO ordering within digit buckets to maintain stability across digit passes.
