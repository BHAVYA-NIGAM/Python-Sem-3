#If a four digit number is input through the keyboard, write a program to obtain the sum of the first and last digit of this number

digit = int(input("Enter a number"))

first_digit = digit % 10
fourth_digit = digit // 1000

sum = first_digit + fourth_digit

print("Sum is ", sum)


