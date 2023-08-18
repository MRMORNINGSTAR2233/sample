class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create two Point objects
point1 = Point(3, 4)
point2 = Point(7, 9)

# Get the hexadecimal IDs
hex_id1 = hex(id(point1))
hex_id2 = hex(id(point2))

# Convert hexadecimal IDs to decimal
decimal_id1 = int(hex_id1, 16)
decimal_id2 = int(hex_id2, 16)

# Print the objects and their IDs
print("Point 1:", point1)
print("Point 2:", point2)
print("Hexadecimal ID 1:", hex_id1)
print("Hexadecimal ID 2:", hex_id2)
print("Decimal ID 1:", decimal_id1)
print("Decimal ID 2:", decimal_id2)

# Check if the decimal IDs match the original IDs
if decimal_id1 == id(point1) and decimal_id2 == id(point2):
    print("Decimal IDs match the original IDs.")
else:
    print("Decimal IDs do not match the original IDs.")
