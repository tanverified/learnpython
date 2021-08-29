# Sorting simple Data Types

numbers = [3,5,43,99,1]

# numbers.sort()
# numbers.sort(reverse=True)

result = sorted(numbers)
reverseList = sorted(numbers,reverse=True)

print(result)
print(numbers)

# ---------------------------------------------
# Sorting complex Data types

items = [
    ("Product1",20),
    ("Product2",30),
    ("Product3",10)
]

items.sort(key=lambda item:item[1])

print(items)




