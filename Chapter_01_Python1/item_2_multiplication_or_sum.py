# ================================================================================
# Chapter 1 - Item 2: multiplication or sum
# --------------------------------------------------------------------------------
# Problem Statement:
# รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง
# ================================================================================

print("*** multiplication or sum ***")

num1, num2 = input("Enter num1 num2 : ").split()

num1 = int(num1)
num2 = int(num2)

if num1 * num2 <= 1000:
    print("The result is", num1 * num2)
else:
    print("The result is", num1 + num2)

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# A single threshold check on num1 * num2 decides which of two operations
# (product vs. sum) gets printed.
#
# Core idea:
#   The product is only ever computed once and reused as the branch
#   condition, so the "expensive" (larger) value never needs to be
#   recomputed twice; only the sum is calculated separately, and only in
#   the branch where it is actually needed.
#
# Key Steps & Logic:
# 1. input(...).split() splits "num1 num2" on whitespace into two strings,
#    which are then explicitly converted with int(...) since the problem
#    guarantees two integers.
# 2. if num1 * num2 <= 1000: uses "<=" (not "<") because the spec says
#    "less than or equal to 1,000" should print the product -- so the
#    boundary case product == 1000 must fall into the product branch.
# 3. When the product exceeds 1000, the else branch prints num1 + num2
#    instead, per the problem's "otherwise show the sum" rule.
# 4. Both branches share the same print("The result is", ...) prefix, so
#    only the trailing value differs between the two cases.
#
# Worked example A -- Enter num1 num2 : 10 20
#   product = 10 * 20 = 200 <= 1000  -> print "The result is 200"
# Worked example B -- Enter num1 num2 : 100 50
#   product = 100 * 50 = 5000 > 1000 -> print "The result is 150" (sum)
# ================================================================================