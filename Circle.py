import math

# Function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius ** 2

# Input radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = area_of_circle(radius)

# Display the result
print(f"The area of the circle with radius {radius} is {area:.2f}")
