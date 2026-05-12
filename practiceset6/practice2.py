# m1 = int(input("Enter the marks of subject1:"))
# m2 = int(input("Enter the marks of subject2:"))
# m3 = int(input("Enter the marks of subject3:"))

# if(m1 and m2 and m3 >= 33):
#     print("pass")
# else:
#     print("fails")




m1 = int(input("Enter the marks of subject1:"))
m2 = int(input("Enter the marks of subject2:"))
m3 = int(input("Enter the marks of subject3:"))

total_percentage = (100*(m1 + m2 + m3))/300 

if total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("You are pass")
else:
    print("fails")