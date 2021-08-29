letters = ["a","b","c"]

# Add
letters.append("d")
letters.insert(0,"-")


# Remove
letters.pop()
letters.pop(0)
letters.remove('b')

del letters[0:3]
letters.clear()


print(letters)
