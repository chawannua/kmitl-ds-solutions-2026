# ================================================================================
# Chapter 4 - Item 3: 26s1 Concept Queue
# --------------------------------------------------------------------------------
# Problem Statement:
# Accept a single line of input where each sequence is indicated by a letter followed by the number of times the action should be performed. 'E' indicates an enqueue operation, and 'D' indicates a dequeue operation. If the letter is something else, count it as an error input.
# You must report how many ineffective dequeues occur in sequence and show how the queue changes at each step.
# ================================================================================

class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, value):
        self.items.append(value)
        
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None
        
    def isEmpty(self):
        return len(self.items) == 0
        
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    inp_string = input("input : ")
    inp = inp_string.split(",")
    
    q = Queue()
    enq_counter = 0
    error_dequeue = 0
    error_input = 0
    
    for step in inp:
        step = step.strip()
        print(f"Step : {step}")
        if step.startswith('E') and step[1:].isdigit():
            count = int(step[1:])
            for _ in range(count):
                q.enqueue(f"*{enq_counter}")
                enq_counter += 1
            print(f"Enqueue : {q}")
        elif step.startswith('D') and step[1:].isdigit():
            count = int(step[1:])
            for _ in range(count):
                if q.isEmpty():
                    error_dequeue += 1
                else:
                    q.dequeue()
            print(f"Dequeue : {q}")
        else:
            error_input += 1
            print(q)
            
        print(f"Error Dequeue : {error_dequeue}")
        print(f"Error input : {error_input}")
        print("-" * 20)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Replays a comma-separated op log against a FIFO queue, counting failed ops.
#
# Core idea:
#   Every enqueued item is tagged "*<enq_counter>" with a counter that only ever
#   increases, so the queue's contents always reveal each item's original
#   insertion order even after many enqueue/dequeue rounds have mixed things up.
#
# Key Steps & Logic:
# 1. inp_string.split(",") turns "E3,D2,X,..." into steps; each is stripped of
#    whitespace before being classified.
# 2. "E<n>" (checked via step.startswith('E') and step[1:].isdigit()): loops n
#    times calling q.enqueue(f"*{enq_counter}") then enq_counter += 1, so each
#    push gets a fresh, unique label -- item identity, not just value, is kept.
# 3. "D<n>": loops n times, but checks q.isEmpty() BEFORE every single pop(0).
#    If empty it counts an "ineffective dequeue" (error_dequeue += 1) instead of
#    dequeuing; this lets a D-count larger than the queue's size correctly count
#    only the excess pops as errors instead of crashing or silently stopping.
# 4. Anything else (e.g. "X") is not E/D shaped, so it only bumps error_input
#    and the queue is printed unchanged -- no queue operation happens.
# 5. After every step the running error_dequeue/error_input totals and a
#    "-" * 20 divider are printed, giving a full step-by-step audit trail.
#
# Worked example -- "E3,D2,X,E1,D5"
#   step | queue after   | error_dequeue | error_input
#   -----+---------------+---------------+-------------
#   E3   | [*0,*1,*2]    | 0             | 0
#   D2   | [*2]          | 0             | 0
#   X    | [*2]          | 0             | 1   <- unrecognized op, queue untouched
#   E1   | [*2,*3]       | 0             | 1
#   D5   | []            | 3             | 1   <- 2 real pops + 3 ineffective ones
# ================================================================================