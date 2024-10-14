#WAP to find biggest of given 3 numbers from the command prompt

a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")

if a > b and a > c:
  print(a + " is greater than " + b + " and " + c)
elif b > a and b > c:
  print(b + " is greater than " + a + " and " + c)
else :
  print(c + " is greater than " + a + " and " + b)