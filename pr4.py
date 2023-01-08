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