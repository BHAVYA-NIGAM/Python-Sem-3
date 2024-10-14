#Find all primes between a given range

num = int(input("Enter a number to find prime number from 1 to that numbe : "))

for i in range(1, num) : 
  count=0
  for j in range(1, i) :
    if(i % j == 0) :
      count = count + 1
  if(count == 1) :
    print(i)