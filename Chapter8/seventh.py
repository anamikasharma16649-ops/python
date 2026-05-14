#  write a recursive function that compute the sum of 1 to N numbers.

def sum(n):
    if n == 1:
        return 1
    else:
        return (n + sum(n-1))



n = int(input("Enter number:"))
x = sum(n)
print(x)