class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()

y="hello there"
print(dir(y))


#constructed destructed
class PartyAnimal:
    x=0

    def __init__(self):
        print("I'm constructed")

    def party(self):
        self.x = self.x +1
        print("so far", self.x)

    def __del__(self):
        print("I am destructured", self.x)

an = PartyAnimal()
an.party()
an.party()
an= 42
print("an contains", an)

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)#party count is parameter that will be used in nam

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()

#I jumped to SQLite browser