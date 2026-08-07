# ðŸš€ DATA STRUCTURES QUIZ 1 - 5-MIN CHEAT SHEET

## ðŸ“ CH 1 & 2: PYTHON ESSENTIALS & OOP
**Fast Input Parsing:**
```python
# Multiple ints on one line
a, b = map(int, input().split())
# List of ints
nums = list(map(int, input().split()))
```
**String & List Slicing `[start:end:step]`:**
- `s[::-1]` âž¡ï¸ **Reverses** the string or list!
- `s[1:4]` âž¡ï¸ Gets indices 1, 2, 3 (end is EXCLUSIVE).

**Quick OOP Node Template:**
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

---

## ðŸ¥ž CH 3: STACK (LIFO - Last In, First Out)
**1. Parentheses Matching (4-Line Logic):**
```python
for char in s:
    if char in "({[": stack.append(char)
    elif not stack or match(stack.pop(), char) == False: return False
return len(stack) == 0
```

**2. Infix to Postfix Precedence:**
| Operator | Precedence | Associativity |
| :--- | :--- | :--- |
| `^` | 3 | **Right-to-Left** (Push to stack if same/higher) |
| `*`, `/` | 2 | Left-to-Right |
| `+`, `-` | 1 | Left-to-Right |
| `(` | 0 (in stack) | N/A |
**RULE:** Pop from stack to output while `precedence(stack_top) >= precedence(current)`. 
*Exception: `^` is Right-Associative, only pop if `precedence(stack_top) > precedence(current)`.*

**3. Postfix Evaluation (3-Step Logic):**
1. Read left to right.
2. If operand (number) âž¡ï¸ **Push** to stack.
3. If operator âž¡ï¸ **Pop two**, calculate `(2nd_popped op 1st_popped)`, **Push** result.

---

## ðŸš¶ CH 4: QUEUE (FIFO - First In, First Out)
**1. The O(1) Queue (DON'T use `list.pop(0)`!):**
```python
from collections import deque
q = deque()
q.append(1)      # Enqueue O(1)
x = q.popleft()  # Dequeue O(1)
```

**2. Circular Queue Modulo Equations:**
- **Empty:** `size == 0` (or `front == rear` depending on implementation)
- **Full:** `(rear + 1) % capacity == front`
- **Next Pos:** `(pos + 1) % capacity`

---

## âš ï¸ TOP 5 INSTANT EXAM PITFALLS âš ï¸
1. **Wrong Pop Order in Postfix Eval:** It is ALWAYS `val2 (op) val1` where `val1 = pop()` and `val2 = pop()`. Subtraction/Division order matters!
2. **Right-Associativity of `^`:** `A^B^C` is evaluated as `A^(B^C)`. Do NOT pop `^` from the stack when pushing another `^`.
3. **Queue `pop(0)` Time Complexity:** Using `list.pop(0)` is **O(N)**. Always use `collections.deque.popleft()` for **O(1)**.
4. **Parentheses Remaining:** Forgetting to check if the stack is EMPTY at the end of parentheses matching. (`return len(stack) == 0`)
5. **String Immutability:** You cannot do `s[0] = 'a'`. You must slice and reassign or convert to a list first.


