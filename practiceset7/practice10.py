# Write a program to print multiplication table of n using for loop in reserved order.

n = int(input("Enter number: "))
for i in range(10,0,-1):
    print(f"{n} * {i} = {n*i}")