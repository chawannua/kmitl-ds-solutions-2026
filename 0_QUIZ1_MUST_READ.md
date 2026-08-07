# DATA STRUCTURES QUIZ 1 - 5-MINUTE CHEAT SHEET
# READ THIS RIGHT BEFORE ENTERING THE EXAM
# Encoding: plain ASCII - no emoji

---

## CH 1 & 2: PYTHON ESSENTIALS & OOP

Fast Input Parsing:
```python
a, b = map(int, input().split())
nums = list(map(int, input().split()))
arr = [int(x) for x in input().split()]
```

String & List Slicing [start:end:step]:
- s[::-1]  ->  Reverses the string or list
- s[1:4]   ->  Gets indices 1, 2, 3 (end is EXCLUSIVE)
- s[1:]    ->  All characters except first

OOP Node Template:
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

---

## CH 3: STACK (LIFO - Last In, First Out)

1. Parentheses Matching (4-Line Logic):
```python
for char in s:
    if char in "({[":
        stack.append(char)
    elif not stack or not matches(stack[-1], char):
        return False
    else:
        stack.pop()
return len(stack) == 0
```

2. Infix to Postfix - Precedence Table:
| Operator | Precedence | Associativity |
|----------|-----------|---------------|
| ^        | 3         | RIGHT         |
| * /      | 2         | LEFT          |
| + -      | 1         | LEFT          |

KEY RULE: ^ is RIGHT-associative
- a^b^c = a^(b^c)  [NOT (a^b)^c]

3. Postfix Evaluation - 3 Steps:
```python
b = stack.pop()   # Step 1: pop b FIRST
a = stack.pop()   # Step 2: pop a SECOND
stack.append(a op b)  # Step 3: push result
```

---

## CH 4: QUEUE (FIFO - First In, First Out)

USE deque - NOT list:
```python
from collections import deque
q = deque()
q.append(x)    # enqueue - O(1)
q.popleft()    # dequeue - O(1)  <-- NOT list.pop(0) which is O(N)!
```

Circular Queue Key Equations:
- Empty:     size == 0
- Full:      size == capacity
- Next slot: (index + 1) % capacity

BFS Template:
```python
from collections import deque
visited = set([start])
q = deque([(start, 0)])
while q:
    pos, dist = q.popleft()
    if pos == end: return dist
    for nb in neighbors(pos):
        if nb not in visited:
            visited.add(nb)  # mark BEFORE enqueue
            q.append((nb, dist+1))
```

---

## TOP 5 MUST-REMEMBER RULES

1. list.pop(0) is O(N) -- use deque.popleft() which is O(1)
2. ^ is RIGHT-associative -- a^b^c = a^(b^c)
3. Always check `if not stack` before stack.pop()
4. Circular queue uses modulo: (index + 1) % capacity
5. BFS: mark visited BEFORE enqueuing (not after dequeuing)
