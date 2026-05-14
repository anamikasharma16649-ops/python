# Question 1 (Easy → start coding):

# Ek program likho jo check kare:

# 👉 agar number positive hai to "Positive" print karo
# 👉 agar number negative hai to "Negative" print karo
# 👉 agar number 0 hai to "Zero" print kar


n = int(input("Enter number:"))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")


# Question 2 (coding 🔥):

# Ab ye likho:

# 👉 User se number lo
# 👉 Check karo:

# even hai to "Even"
# odd hai to "Odd"

n = int(input("enter number:"))
if n % 2 ==0:
    print("even")
else:
    print("odd")

# ❓ Question 3 (slightly tricky 🔥):

# Ab ye code likho:

# 👉 User se age input lo
# 👉 conditions:

# age >= 18 → "Eligible to vote"
# else → "Not eligible to vote"


age = int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")