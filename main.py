def find(word, letter):
   index = 0
   while index < len(word):
       if word[index] == letter:
         return index
       index = index + 1
       return -1
word = input("Enter a word:")
search = input("Enter a letter to search:")
c = find(word, search)
if c == -1:
   print("Letter is not found in search")
else:
   print("The index of search letter",search, "is in",c, "position")