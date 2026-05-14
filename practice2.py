def f_to_c(f):
    c = (f-32)*5/9
    return c

f = int(input("Enter tempreature in fahrenheit: "))
c = f_to_c(f)
print("Temperature in Celsius:", c)