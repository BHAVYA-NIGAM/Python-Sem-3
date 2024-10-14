#A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denominations the cashier will have to give to the withdrawer.

price = int(input("Enter the price : "))
count100 = 0
count50 = 0
count10 = 0

while price >= 100 :
  price -= 100
  count100 = count100 + 1

while price >= 50 :
  price -= 50
  count50 = count50 + 1

while price >= 10 :
  price -= 10
  count10 = count10 + 1

print("Cashier will have to give " + str(count100) + " notes of ₹100 and " + str(count50) + " notes of ₹50 and " + str(count10) + " notes of ₹10")

