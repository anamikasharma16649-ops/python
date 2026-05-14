def xyz():
    a = int(input("Enter the number1:"))
    b = int(input("Enter the number2:"))
    c = int(input("Enter the number3:"))
    if a >b and a > c :
        print("a is greatest")
    elif b > a and b > c:
        print("b is greatest")
    else:
        print("c is greatest")

xyz()