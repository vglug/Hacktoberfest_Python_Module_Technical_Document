import math

# Function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius ** 2

# Main function
def main():
    try:
        # Input radius from the user
        radius = float(input("Enter the radius of the circle: "))
        
        if radius < 0:
            print("Radius cannot be negative. Please enter a positive value.")
            return

        # Calculate the area
        area = area_of_circle(radius)

        # Display the result
        print(f"The area of the circle with radius {radius} is {area:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a numerical value for the radius.")

# Execute the main function
if __name__ == "__main__":
    main()
