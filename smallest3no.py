#WAP to find smallest of given 3 numbers 

a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")

if a < b and a < c:
  print(a + " is less than " + b + " and " + c)
elif b < a and b < c:
  print(b + " is less than " + a + " and " + c)
else :
  print(c + " is less than " + a + " and " + b)