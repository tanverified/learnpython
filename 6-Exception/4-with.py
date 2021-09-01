try:
    with open("app.py") as file:
        print("file opened")
    age = int(input("age: "))
    xfactor = age/0
except (ValueError, ZeroDivisionError):
    print("Please Enter Valid Age")
else:
    print(f"Your Age is {age}")
finally:
    file.close()