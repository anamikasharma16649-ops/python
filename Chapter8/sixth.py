#  practice of function


#  No arguments no return value 


def add():
    a = int(input("Enter the number1:"))
    b = int(input("Enter the number2:"))
    c = a + b
    print(c)

add()
print("doneeeeee")


#  With arguments no return value  


def add(a,b):
    c = a + b
    print(c)

#  __main__ 

# add(5,6)

x = int(input("Enter the number1:"))
y = int(input("Enter the number2:"))
add(x,y)


# no arguments with return value 

def add():
    a = int(input("Enter the number1:"))
    b = int(input("Enter the number2:"))
    c = a + b
    return c

x = add()
print(x)

# with arguments with return value 

def add(a,b):
    return a + b

# __main__
a = int(input("Enter the number1:"))
b = int(input("Enter the number2:"))
c = add(a,b)
print(c)


#  reverse

def reverse(i):
    rev = 0
    while i > 0:
        rev = (rev * 10) + i % 10
        i = i // 10
    print(rev)

i = int(input("Enter number: "))
reverse(i)
