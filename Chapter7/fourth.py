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