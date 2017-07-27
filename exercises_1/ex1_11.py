"""
Convert
"8.8" to a float.
8.8 to an integer (with rounding).
"8.8" to an integer (with rounding).
8.8 to a string.
8 to a string.
8 to a float.
8 to a boolean.
"""
print("8.8", "to float is", float("8.8"), type(float("8.8")))
print(8.8, "to integer is", int(8.8), type(int(8.8)))
print("8.8", "to integer is", int(float("8.8")), type(int(float("8.8"))))
print(8.8, "to string is", str(8.8), type(str(8.8)))
print(8, "to string is", str(8), type(str(8)))
print(8, "to float is", float(8), type(float(8)))
print(8, "to boolean is", bool(8), type(bool(8)))

# Bonus
print(0, "to boolean is", bool(0), type(bool(0)))
