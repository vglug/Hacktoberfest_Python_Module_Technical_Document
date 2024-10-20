class area_rectangle:
  
   def area_of_rectangle(length, width):
       return length * width


    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))


    area = area_of_rectangle(length, width)


    print(f"The area of the rectangle is: {area}")
