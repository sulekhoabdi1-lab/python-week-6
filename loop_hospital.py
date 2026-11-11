
@@ -0,0 +1,21 @@
# Patient 1 — should print 1 to 10, but stops early:
# FIXED: Changed range stop bound from 10 to 11 because range() is exclusive of the stop value.
print("--- Patient 1 ---")
for i in range(1, 11):
    print(i)

# Patient 2 — should count down 3, 2, 1 — but never stops:
# FIXED: Decremented n inside the while loop (n -= 1) to prevent an infinite loop.
print("--- Patient 2 ---")
n = 3
while n > 0:
    print(n)
    n -= 1

# Patient 3 — should add up 1 + 2 + 3 + 4 + 5 = 15, but prints the wrong total:
# FIXED: Moved total = 0 outside the for loop so it doesn't reset to 0 on every iteration, and moved print(total) outside the loop to display the final sum.
print("--- Patient 3 ---")
total = 0
for i in range(1, 6):
    total = total + i
print(total)
