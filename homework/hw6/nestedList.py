q = [['a','b','c'], ['d','e','f'], ['g','h']]

string = ''
for ele in q:
   for letter in ele:
      string = string + letter

print(string)
