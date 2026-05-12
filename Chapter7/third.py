#  for loops
for x in range(4):
    print(x)

# 
for y in range(0,100,4):
    print(y)

# 

l = [1,4,67,"radhe", True]
for i in l:
    print(i)

    # break

for i in range(100):
    if i == 34:
        break   # exit the loop right now
    print(i)

#  continue

for i in range(100):
    if i == 34:
        continue   # skip this iteration
    print(i)

# pass

for i in range(100):
    pass
# baad mai kaam krege yaha to use pass

