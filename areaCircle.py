#Write a Python program which accepts the radius of a circle from the user and compute the area

radius = int(input("Enter the radius of the circle to find the area (in cm) : "))
area = 3.14*radius*radius

print("The area of the circle with radius " + str(radius) + " is " + str(area) + "cm^2")