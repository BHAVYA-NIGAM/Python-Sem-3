#WAP to find smallest of given 2 numbers


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if a < b:
  print(str(a) + " is less than " + str(b))
else:
  print(str(b) + " is less than " + str(a))