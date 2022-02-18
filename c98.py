#f=open("test.txt")
#f.read()
from itertools import count


f=open("test.txt")


fileLines=f.readlines()
for line in fileLines:
    print(line)

name="Dev Here,I Am 15year old"
words=name.split()
print(words)

def countwordsfromfile():
    filename=input("Enter The File Name:")
    numberofword=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numberofword=numberofword+len(words)
    print("number of words:")
    print(numberofword)
        
countwordsfromfile()