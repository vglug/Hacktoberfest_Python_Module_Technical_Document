# for example take input as 7.

radius = int(input())
def area_of_a_circle(radius):
    pi = 3.14
    area = pi*(radius**2)
    return round(area,2)
area_of_a_circle(radius)
print(area_of_a_circle(radius))
