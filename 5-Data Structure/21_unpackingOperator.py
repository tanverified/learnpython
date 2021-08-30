from typing import Collection


first = [1, 2]
second = [3]

combined = [*first, *second]

print(combined)

third = {"x": 1, "y": 2}
fourth = {"z": 3}

together = {**third,**fourth,"z":1}

print(together)