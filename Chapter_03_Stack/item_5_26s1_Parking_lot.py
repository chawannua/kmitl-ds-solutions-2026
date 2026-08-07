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
# This Python script solves Chapter 3 Item 5 (26s1 Parking lot).
#
# Key Steps & Logic:
# 1. Inputs are parsed from user input and converted to appropriate data types.
# 2. The core data structure/algorithmic logic (e.g. math formula, stack operations, 
#    queue handling, linked list pointers, or recursive subproblems) is evaluated.
# 3. The final computed output is formatted and printed to match testcase specifications.
# ================================================================================