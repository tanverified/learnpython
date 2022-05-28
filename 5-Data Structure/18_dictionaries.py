# declare dictionary
# point = {"x": 10, "y": 20}
point = dict(x=10, y=20)

# Adding items
point["x"] = 30
point["z"] = 50

# checking items
if "a" in point:
    print(point["a"])
point.get("a",0)

# deleting items
del point["x"]

# looping over
for x in point.items():
    print(x)

for key, value in point.items():
    print(key,value)


