#Check whether a number is prime

num = int(input("Enter a number to check whether it is prime or not : "))
count = 0

for i in range(1, num) : 
  if(num%i == 0) : 
    count = count + 1

if count == 1 :
  print("Yes it is prime")
else :
  print("No it is not prime")