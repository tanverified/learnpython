def add_user(**user):
    return user["name"]


result = add_user(id=1, name="John", age=22)

print(result)