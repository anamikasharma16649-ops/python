# 1 se 10 tak numbers print karo using for loop

for i in range(1,11):
    print(i)


# 1 se 20 tak sirf even numbers print karo



for i in range(1,21):
    if i % 2 == 0:
        print(i)

# Kisi number n ka multiplication table print karo (1 to 10)


n = int(input("Enter number: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

# 1 se 10 tak numbers print karo using while loop


i = 1
while i <= 10:
    print(i)
    i += 1

# 1 se 20 tak sirf odd numbers print karo using while loop
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1


# 👉 Reverse counting print karo: 10 to 1 using while loop


i = 10
while i >= 1:
    print(i)
    i -= 1


fact = 1
a = int(input("Enter number: "))
for i in range(1, a+1):
    fact = fact*i
print(f"The factorial is: {fact}")