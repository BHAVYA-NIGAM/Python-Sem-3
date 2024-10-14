s = input("Enter main string ")
subs = input("Enter sub string ")

try: 
  n = s.index(subs)
except ValueError:
  print("Substring not found!")
else :
  print("Substring Found!")