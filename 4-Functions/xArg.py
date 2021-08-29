def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

result = multiply(2, 3, 4, 5)
print(result)

