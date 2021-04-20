f=open('abc.txt')
fileLines=f.readlines()
for line in fileLines:
    print(line)

intro='My name is Mananjay, I am 14 years old'
word=intro.split()
print(word)

word1=intro.split(',')
print(word1)