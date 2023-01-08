#SLİCİNG STRİNGS
s = "monty python"
print(s[0:4])

#İN STATEMENT
fruit = "banana"
print("n" in fruit)

if "a" in fruit:
    print("its here")


#STRİNG LİBRARY

greet = "Hello BeYZa"
zap = greet.lower()
print(zap)

print("HeLLoDeAr".lower())#its like calling a function

fruit="banana"
pos = fruit.find("na")
print(pos)#returns the position



#SEARCH AND REPLACE
greet = "hello reha"
nstr = greet.replace("reha", "sezai")
print(nstr)


#WHİTE SPACE REMOVİNG
greet= "    helloü     "
z= greet.lstrip()
print(z)

#PREFİXERS
line="please have a nice day"
print(line.startswith("please"))#for example, just "p" is false


#searching for school
data = "from sephen.marquard@uct.ac.za sat han 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)#found @

sppos = data.find(" ",atpos)
print(sppos)#found space position after @

host = data[atpos+1 : sppos]#from 1 forward @ because @ is the position 0 and its included, and 1 backwards the end which also not included so we dont need to write -1
print(host)

#CHAPTER 7

#new line character \n

line = "hello\nworld"
print(line)


#FİLE HANDLE AS A SEQUENCE
#xfile = open("mbox.txt")
#for cheese in xfile:
 #   print(cheese)

#counting lines in a file

fhand =open("practise.py")
count=0
for line in fhand:
    count = count +1
print("line count", count)


#READİNG
fhand =open("practise.py")
inp=fhand.read()
print(len(inp))

print(inp[:20])

#SEARCHİNG
fhand =open("practise.py")
for line in fhand:
    if line.startswith("x"):
        print("yeah its starts with x")#prints evey line that matches

fhand =open("practise.py")
for line in fhand:
    line = line.rstrip()
    if line.startswith("x"):
        print("yes its starts with x")

#CONTİNUE
fhand =open("practise.py")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("x"):
        continue
    print(line)#prints every line in that file if there is no "not". it continues only with the value that we are searching

#WİTH İN OPERATOR
fhand =open("practise.py")
for line in fhand:
    line = line.rstrip()
    if not "x" in line:#prints all the lines with it
        continue
    print(line)



#PROMPT FOR FİLE NAME
fname=input("enter the file name:   ")
fhand = open(fname)
count=0
for line in fhand:
    if line.startswith("x"):
        count = count +1
print("there were", count, "subjhect lines in", fname)

#FOR BAD FİLE NAMES
fname=input("enter the file name:   ")
try:
    fhand = open(fname)
except:
    print("file cannot be found")
    quit()#it never returns and finishes

count=0
for line in fhand:
    if line.startswith("x"):
        count = count +1
print("there were", count, "subjhect lines in", fname)

#RANGE
friends = ["beyza", "fatmna", "bostancı"]
for friend in friends:
    print("happy birthday", friend)


friends = ["beyza", "fatmna", "bostancı"]
for i in range(len(friends)):
    friend = friends[i]
    print("same happy birthday", friend)

