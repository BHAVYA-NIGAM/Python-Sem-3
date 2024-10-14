#Check whether a number is Armstrong

num = int(input("Enter a number to check if it is Armstrong or not : "))
org = num
sum = 0
digitCount = 0


while num > 0 : 
  digitCount = digitCount + 1
  num = num // 10

num = org

while num > 0 :
  digit = num % 10
  num = num // 10
  sum = sum + pow(digit, digitCount)

if sum is org : 
  print("Yes number is Armstrong")
else :
  print("No number is not Armstrong")