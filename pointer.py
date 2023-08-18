class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Create a Point object
point = Point(3, 5)

# Print the hexadecimal memory address
hex_id = hex(id(point))
print("Hexadecimal ID:", hex_id)

# Translate hexadecimal to decimal
decimal_id = int(hex_id, 16)
print("Decimal ID:", decimal_id)

# Confirm if the IDs match
if decimal_id == id(point):
    print("Memory addresses match!")
else:
    print("Memory addresses do not match.")
