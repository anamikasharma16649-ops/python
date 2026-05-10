# length of string

name = "anamika sharma"
print(len(name))


# string endswith

print(name.endswith("ma"))
print(name.endswith("am"))

#  string startswith

print(name.startswith("anam"))

# count krti hai hum koi bhi word bracets mai dalege vo uss word ki occurance ko count kregi.

print(name.count("a"))


# string capatalization

print(name.capitalize())

# find words

print(name.find("sharma"))   #8
print(name.find("anamika"))    # 0

# replace words

print(name.replace("anamika","annu"))