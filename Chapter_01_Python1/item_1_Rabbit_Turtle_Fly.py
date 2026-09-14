# ================================================================================
# Chapter 1 - Item 1: Rabbit & Turtle & Fly
# --------------------------------------------------------------------------------
# Problem Statement:
#     เริ่มต้นกระต่ายวิ่งอยู่หน้าเต่าเป็นระยะ d เมตร กระต่ายวิ่งด้วยความเร็วคงที่ Vr เมตรต่อวินาที และเต่าวิ่งด้วยความเร็วคงที่ Vt เมตรต่อวินาที ซึ่งนิทานเรื่องนี้เต่าจะวิ่งเร็วกว่ากระต่ายเสมอ แมลงวันตัวหนึ่งอยู่บนหัวเต่าบินด้วยควมเร็วคงที่ Vf เมตรต่อวินาที เมื่อแมลงวันบินไปจนถึงกระต่ายแล้วมันก็จะบินย้อนกลับไปหาเต่าด้วยความเร็วเท่าเดิม แมลงวันจะบินกลับไปกลับมาระหว่างกระต่ายและเต่าจนกว่าเต่าจะวิ่งมาทันกระต่ายพอดี (เต่าจะต้องวิ่งมาทันกระต่ายเพราะเต่าวิ่งด้วยความเร็วมากกว่ากระต่าย) 
#     จงเขียนโปรแกรมเพื่อหาว่าแมลงวันจะบินได้เป็นระยะทางทั้งสิ้นกี่เมตร เต่าจึงจะวิ่งทันกระต่ายพอดี ในข้อนี้ให้ถือว่าทั้งกระต่ายและเต่า และ แมลงวันเคลื่อนที่โดยไม่มีความเร่งเสมอ
# ข้อมูลนำเข้า
# บรรทัดเดียว จำนวนเต็มบวก d Vr Vt และ Vf ตามลำดับห่างกันด้วยเว้นวรรคหนึ่งช่อง โดยตัวเลขทุกตัวเลขทุกตัวจะไม่เกิน 5000 และ Vt > Vr และแมลงวันบินด้วยความเร็วสูงกว่าเต่าและกระต่ายเสมอ
# ข้อมูลส่งออก
# บรรทัดเดียว ระยะทางของแมลงวันที่บินได้ทั้งหมด โดยให้ตอบเป็นทศนิยม 2 ตำแหน่ง
# *** ห้ามใช้ For / While Loop ***
# Hint : S = VT
# ================================================================================

print("*** Rabbit & Turtle ***")


d, Vr, Vt, Vf = map(float, input("Enter Input : ").split())

time = d / (Vt - Vr)

total_distance = Vf * time

print(f"{total_distance:.2f}")

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# Closed-form relative-speed formula -- no loop needed because the fly's total
# path length only depends on how long the chase lasts, not on each leg.
#
# Core idea:
#   The fly bounces back and forth infinitely many times, but the SUM of an
#   infinite number of shrinking legs still just equals (fly speed) x (total
#   chase time), because the fly is airborne for the whole chase. So instead
#   of summing a geometric series of bounces, compute how long the turtle
#   takes to close the gap, then multiply by Vf directly (Hint: S = V*T).
#
# Key Steps & Logic:
# 1. d, Vr, Vt, Vf = map(float, ...) reads the 4 numbers on one line and
#    converts them to float, since the answer must be printed to 2 decimals.
# 2. time = d / (Vt - Vr) is the classic "closing speed" formula: the turtle
#    starts d meters behind and gains ground on the rabbit at (Vt - Vr) m/s,
#    so it needs d / (Vt - Vr) seconds to catch up. The problem guarantees
#    Vt > Vr, so this division never hits zero or goes negative.
# 3. total_distance = Vf * time converts that chase duration into the fly's
#    total flight distance -- the back-and-forth path is irrelevant, only
#    elapsed time times fly speed matters.
# 4. f"{total_distance:.2f}" formats the result to exactly 2 decimal places,
#    matching the "answer as a decimal with 2 digits" output requirement.
# 5. No for/while loop is used anywhere, satisfying the problem's constraint.
#
# Worked example -- Enter Input : 100 1 2 10  (d=100, Vr=1, Vt=2, Vf=10)
#   time            = 100 / (2 - 1) = 100.0 seconds
#   total_distance  = 10 * 100.0    = 1000.0 meters
#   Printed output  = "1000.00"
# ================================================================================