@@ -0,0 +1,5 @@
number = int(input("Enter a number for the times table: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
