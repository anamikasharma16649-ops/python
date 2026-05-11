#  dictionary
# list of key value pair

marks = {
    "Anamika" : 100,
    "Harry" : 99,
    "Nitika" : 98
}

print(marks)
print(type(marks))
print(len(marks))

# list = [32,54,65,65]
# print(list[2])

print(marks["Anamika"])


#  items method

print(marks.items())

#  key method

print(marks.keys())

#  value method)

print(marks.values())


# update method

marks.update({"Anamika" : 99.9, "Anjali" : 97})
print(marks)

#  get method

print(marks.get("Anamika1"))    # prints None
print(marks["Anamika1"])  # prints error

#  dono alag hai concept