#Two numbers are input through the keyboard into two locations C and D. Write a program to interchange the contents of C and D

# C = int(input("Enter first number : "))
# D = int(input("Enter second number : "))

# print("Before swap :")
# print("C = " + str(C))
# print("D = " + str(D))

# C = C + D
# D = C - D
# C = C - D

# print("After swap :")
# print("C = " + str(C))
# print("D = " + str(D))

C = int(input("Enter first number : "))
D = int(input("Enter second number : "))

print("Before swap :")
print("C = ", C, " D = ", D)

C, D = D, C

print("After swap :")
print("C = ", C, " D = ", D)
