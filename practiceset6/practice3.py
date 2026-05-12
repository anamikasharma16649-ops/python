# A spam comment is defind as a text containning following keywords

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

m = input("Enter your comment: ")

if (p1 in m) or (p2 in m) or (p3 in m) or (p4 in m):
    print("This message is spam")

else:
    print("This message is not a spam")
    
    