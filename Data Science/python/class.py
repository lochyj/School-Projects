import math

G = 9.8 # G is the gravitational constant on earth

try:
    angle = int(input("Enter the initial angle of the arrow: "))
    velocity = int(input("Enter the initial velocity of the arrow: "))
except:
    print("Inputs must be an integer.")

angle_radians = angle * (math.pi/180)

arrow_range = (velocity**2)*math.sin(2*angle_radians) / G

print(f"The range of the arrow is {arrow_range}m")
