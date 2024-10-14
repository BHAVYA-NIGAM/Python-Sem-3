#Write a python program that accepts a word from the user and reverse it

word = input("Enter a word ")
size = len(word)
j=0
revWord

for i in range (size - 1, -1, -1) : 
  revWord[j] = word[i]
  j = j + 1

print(revWord)