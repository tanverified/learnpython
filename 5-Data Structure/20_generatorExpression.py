from sys import getsizeof

values = (x * 2 for x in range(1000000))

values2 = [x * 2 for x in range(1000000)]


print("gen",getsizeof(values))
print("list",getsizeof(values2))
