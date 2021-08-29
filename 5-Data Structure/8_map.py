items = [
    ("Product1",20),
    ("Product2",30),
    ("Product3",10)
]

prices = map(lambda item: item[1],items)


print(list(prices))