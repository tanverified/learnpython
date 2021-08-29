items = [
    ("Product1", 20),
    ("Product2", 30),
    ("Product3", 9)
]

filtered = filter(lambda item: item[1] >= 10, items)

print(list(filtered))
