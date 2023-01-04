x = input("what is your name?")
print(x , "chuck")
print(type(x))
type(x)

y = 5
if y>= 8:
    print("bigger")
else:
    print("smaller")
print("all done")


x = 5
print("hello")

#DEFİNİNG FUNCTİON

def lyrics():
    print("printed first")
    print("printed second")
lyrics()
print("third")

# function needs to be used after defining it bu you can use it whenever you wanted afterwards
x=x+2
print(x)


#USİNG ARGUMENTS
def greeting(lang):
    if lang == "es":
        print("hola")
    elif lang == "tr":
        print("merhaba")
    else:
        print("hello")

greeting("es")


# RETURN VALUES

def greet():
    return "hello"

print(greet(), "Beyza")

def greets(lang):
    if lang == "es":
        return "hola"
    elif lang == "tr":
        return "merhaba"
    else:
        return "hello"


print(greets("es"), "reha")

# MORE THAN 1 PARAMETER
def added(a,b):
    addtwo = a +b
    return addtwo

z = added(8,12)
print(z)


#WHİLE LOOP

n=5
while n>0:
    print(n)
    n = n-1
print("blastoff")
print(n)

#runs 5 times true and 1 time false in the end and stops
#n=5 ---- creates an infinite loop, true forever
while n>0:
    print("lather")
    print("rinse")
print("dry off1")

#zero-trip loops
n=0
while n>0:
    print("lather2")
    print("rinse2")
print("dry off2")


#BREAKİNG OUT OF A LOOP
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("finished")

#FİNİSHİNG AN İTERATİON WİTH CONTİNUE

while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("done!!!")


#excersize question
n = 0
while True:
    if n == 3: #work till you reach 3 and break it there
        break
    print(n)
    n = n + 1

#FOR LOOP
for i in [5,4,3,2,1,0]:
  print(i)
print("blastoff!")

friends = ["erdem", "ahmet","mehmet", "ali"]
for friend in friends:
    print("iyi ki doğdun", friend)
print("mutlu yıllar")


print("before")
for thing in [9,41,12,3,74,15]:
    print(thing)
print("after")


largest_so_far = -1
print("before", largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)#compares the numbers

print("after", largest_so_far)


#example error
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 1, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break #stops the loop in the first result
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)



#COUNTİNG İN A LOOP

zork = 0
print("before", zork)
for thing in [9,42,12,3,74,15]:
    zork = zork +1#go 1 value forward and count
    print(zork, thing)
print("after", zork)


#SUMMİNG A LOOP

zork = 0
print("before", zork)
for thing in [9,12,42,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print("after", zork)

#FİNDİNG THE AVARAGE İN A LOOP
count = 0
sum = 0
print("before", count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("after", count, sum, sum/count)


#FİLTERİNG İN A LOOP
print("beffoooree")
for value in [9,41,12,3,74,15]:
    if value > 20:
        print("large number", value)
print("affter")

#SEARCH USİNG A BOOLEAN

found = False
print("beforey", found)
for value in [9,41,55,23,68,4,17]:
    if value == 23:
        found = True #returns true after finding it because it has only 1 work
    print(found, value)
print("afterey", found)

#HOW TO FİND THE SMALLEST VALUE

smallest_so_far= -1
print("befores", smallest_so_far)
for the_num in [9,41,55,23,68,4,17]:
    if the_num < smallest_so_far:
        smallest_so_far= the_num
    print(smallest_so_far, the_num)
print("afters", smallest_so_far) #gives -1 , we can modify it if we know the data but what if we don't know tha data thats coming


smallest= None #none is a type and it has 1 value which is none, it is constant and empty
print("befores")
for value in [9,41,55,23,68,4,17]:
    if smallest is None: #if smallest is true
        smallest = value #runs this case, copies values, first goes to 9 and takes it then goes again and finds 41 than jumps to elif
    elif value < smallest: #asks if the 41 smaller than 9
        smallest = value # if yes, run this case, if no go again for another round
    print(smallest, value)
print("afterss", smallest)
#since the smallest is none and there is no value for it, when loop starts it takes the first number as the smallest and then starts to compare it with other numbers


#THE is AND is not OPERATORS

smallest = None
print("beforeis")
for value in [9,41,55,23,68,4,17]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest =value
    print(smallest, value)

print("afteris", smallest)


#STRİNG PLACEMENT

fruit = "banana"
letter = fruit[1]
print(letter)

print(len(fruit))

x=3#position 3
w= fruit[x-1]#1 backwards from position 3
print(w)


#LOOPİNG THROUGH A STRİNG

fruit = "banana"
index =0
while index <len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index +1


for letter in fruit:
    print(letter)#without counting them


#LOOPİNG AND COUNTİNG
word ="banana"
count=0
for letter in word:
    if letter == "a":
        count = count +1
print(count)
