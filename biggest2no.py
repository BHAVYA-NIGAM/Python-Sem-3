#WAP to find biggest of given 2 numbers from the command prompt

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if a > b:
  print(str(a) + " is greater than " + str(b))
elif b > a :
  # print(str(b) + " is greater than " + str(a))
  print("Biggest number is", b)
else :
  print("Both numbers are equal")