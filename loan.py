# WAP to calculate and display the interest on a loan amount(Rupees)
#     You would need three variables to hold 'principal', 'Rate_of_Interest'(%), and 'time' in years and can use the formula
#     interest = (principal * Rate_of_Interest * time) / 100;
#     Note: Take user input

print("To display the interest on a loan amount(Rupees)")
principal = int(input("Enter the principal value of the loan : "))
Rate_of_Interest = int(input("Enter the rate of interest of loan (%) : "))
time = int(input("Enter the time of loan : "))

interest = principal * Rate_of_Interest * time / 100
print("Interest on loan amount will be : " + str(interest) + "₹")