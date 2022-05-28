items = [
    ("Product1", 20),
    ("Product2", 30),
    ("Product3", 9)
]


# prices = list(map(lambda item: item[1],items))
prices = [item[1] for item in items]
print(prices)


# filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)

