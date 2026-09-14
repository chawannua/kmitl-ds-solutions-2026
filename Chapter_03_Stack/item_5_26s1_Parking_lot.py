# ================================================================================
# Chapter 3 - Item 5: 26s1 Parking lot
# --------------------------------------------------------------------------------
# Problem Statement:
#         Mr. A's parking area is shaded in blue, while the red area belongs to Mr. B, who is a relative. Both Mr. A's and Mr. B's parking areas are very narrow and can only accommodate cars in a single line. Mr. B does not use his parking space but allows Mr. A to use it without parking his car there permanently. Due to the narrow alley, parking (arrive) and retrieving cars (depart) will operate as a stack. The condition is that when retrieving any car x, the order of the cars should remain the same, as shown in the diagram simulating the parking of cars in Mr. A's parking space using stack operations. Below is an example output.
# Input: Receive 4 values in one line separated by a space (" "). The first position is the maximum number of cars that can park in Mr. A's alley, the second position is the car currently parked in Mr. A's alley, the third position is the action (e.g., if it is "arrive", it will add a car to the alley, and if it is "depart", it will remove a car from the alley), and the fourth position is the number of the car to be added or removed.
# Note: If there are no cars in the alley, set the input to 0 in the second position.
# ================================================================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def contains(self, item):
        return item in self.items

    def to_list(self):
        return list(self.items)


class ParkingLot:
    def __init__(self, max_cars, cars):
        self.max_cars = max_cars
        self.stack = Stack()
        for c in cars:
            self.stack.push(c)

    def arrive(self, num):
        if self.stack.contains(num):
            return f"car {num} already in soi"
        elif len(self.stack.to_list()) >= self.max_cars:
            return f"car {num} cannot arrive : Soi Full"
        else:
            self.stack.push(num)
            return f"car {num} arrive! : Add Car {num}"

    def depart(self, num):
        if not self.stack.contains(num):
            return f"car {num} cannot depart : Dont Have Car {num}"

        temp = Stack()
        while self.stack.peek() != num:
            temp.push(self.stack.pop())
        self.stack.pop()
        while not temp.is_empty():
            self.stack.push(temp.pop())

        return f"car {num} depart ! : Car {num} was remove"

    def cars(self):
        return self.stack.to_list()


def main():
    print("******** Parking Lot ********")
    line = input("Enter max of car / car in soi / operation : ")

    max_str, cars_str, op_str = [part.strip() for part in line.split('/')]
    max_cars = int(max_str)

    cars_str = cars_str.strip()
    cars = [int(x) for x in cars_str.split(',')]

    lot = ParkingLot(max_cars, cars)

    op_parts = op_str.split()
    action = op_parts[0]
    num = int(op_parts[1])

    if action == 'arrive':
        print(lot.arrive(num))
    elif action == 'depart':
        print(lot.depart(num))

    print(lot.cars())


if __name__ == "__main__":
    main()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Models the single-lane alley as a Stack: the car parked last is always the
# one nearest the street exit, so it is the only one that can move freely.
#
# Core idea:
#   To depart a car buried under others, every car parked after it must
#   first be pulled out into the street (a temporary stack `temp`), the
#   target removed, and everyone else parked back in the same relative
#   order. Popping into `temp` reverses the displaced cars once; pushing
#   them back out of `temp` reverses them a second time, so the two
#   reversals cancel out and the original order is restored.
#
# Key Steps & Logic:
# 1. ParkingLot.__init__ pushes the initial `cars` list in order, so the
#    LAST element given is the one nearest the exit (top of stack).
# 2. arrive(num) refuses a duplicate (contains(num)) or a full alley
#    (len(to_list()) >= max_cars); otherwise it pushes the new car on top,
#    since a new arrival always waits at the street end.
# 3. depart(num) first checks contains(num); if the car isn't there at all
#    it fails immediately without touching the stack.
# 4. Otherwise it pops cars into `temp` while stack.peek() != num -- every
#    car parked after the target is temporarily moved out of the alley.
# 5. Once stack.peek() == num, that single pop() removes the target car.
# 6. "while not temp.is_empty(): stack.push(temp.pop())" then drives every
#    displaced car back into the alley in its original relative order, with
#    only the target car now missing.
#
# Worked example -- Enter max of car / car in soi / operation :
#                    3 / 1,2,3 / depart 1
#   Initial stack (bottom -> top): [1, 2, 3]
#   step        | action                | stack   | temp
#   ------------+-----------------------+---------+--------
#   peek=3 != 1 | pop 3 -> temp         | [1, 2]  | [3]
#   peek=2 != 1 | pop 2 -> temp         | [1]     | [3, 2]
#   peek=1 == 1 | stop, pop() removes 1 | []      | [3, 2]
#   restore     | push temp.pop()=2     | [2]     | [3]
#   restore     | push temp.pop()=3     | [2, 3]  | []
#   Printed: car 1 depart ! : Car 1 was remove
#            [2, 3]
# ================================================================================