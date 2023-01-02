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