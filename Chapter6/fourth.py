a = int(input("Enter your age: "))

# statement 1
if(a%2==0):
    print("a is even")
#  end of statement 1

    # statement 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering in 0 which is not a valid age")
    
else:
    print("You are below the age of consent")
#  end of statement 1


print("End of the program")