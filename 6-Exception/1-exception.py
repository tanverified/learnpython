try:
    age = int(input("age: "))
except ValueError as err:
    print("Please Enter Valid Age")
    # print(err)
    # print(type(err))
else:
    print(f"Your Age is {age}")

print("Execution completed")