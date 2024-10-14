# WAP to find difference of two small integers (not greater than 10) without using minus(-) operation [Hint: Use ^ operator]
a = 10
b = 9
# diff = b^a
# diff = diff ^ a
diff = (a^b)-((~a & b) << 1)
print(diff)