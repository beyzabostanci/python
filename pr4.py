abc = "words really matter;for sure"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[2])

for w in stuff:
    print(w)

#DİCTİONARİES

purse = dict()
purse["money"] = 12
purse["candy"]=3
purse["tissue"]=8
print(purse)

purse["candy"]= purse["candy"]+6
print(purse)

jjj = {"chuck":1, "fred":34, "jan":100}
print(jjj)

#HİSTOGRAM

counts = dict()
names = ["csev", "cwen","csev","zqian","cwen"]
for name in names :
    if name not in counts:
        counts[name] = 1#adds new one
    else:
        counts[name]= counts[name] + 1 #adds 1 more to the already created one

print(counts)


counts = dict()
names = ["csev", "cwen","csev","zqian","cwen"]
if name in counts:
    x= counts[name]
else:
    x=0
#above 4 lines equal to below 1 line
counts = dict()
names = ["csev", "cwen","csev","zqian","cwen"]
x = counts.get(name, 0)#key and default value, if the key doesnt exist you get the default

print(x)


counts = dict()
names = ["csev", "cwen","csev","zqian","cwen"]
for name in names:
    counts[name]= counts.get(name,0) + 1# if the name is in there its 1+1 if its not then default

print(counts)


counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))


#COUNTİNG PATTERN


counts = dict()
print("enter a line of text:")
line= input("")

words = line.split()
print("words:", words)

print("counting...")
for word in words:
    counts[word]= counts.get(word,0) +1
print("counts", counts)#counts is the dictionary

jjj = { "chuck":1, "fred":42, "reha":89}
for aaa,bbb in jjj.items():
    print(aaa, bbb)# aaa is for the names(key) and bbb is for the numbers(values)

# TUPLES

#z = (5,4,3)
#z[2]=0

#tuples and assignment
(x,y)=("beyza", 23)
print(x)

print((1,2,3)<(4,5,6))

#sorting lists of tuples

d={"a":10, "b":1, "c":22}
t = sorted(d.items())

[("a", 10), ("b", 1), ("c", 22)]
for k,v in sorted(d.items()):
    print(k,v)

#top 10 most common words in a file
fhand = open("pr3.py")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

lst = list()
for key,val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key,val)

#shorter version for middle part
c={"a":10, "b":1, "c":22}
print(sorted([(v,k) for k,v in c.items()]))


#1 and 2 are the same
#1
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

#2
print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )