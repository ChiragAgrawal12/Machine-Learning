add = lambda x, y: x + y

#oops-

class Arya:
    a=10
    print(type(a))
a1= Arya()
print(a1.a)

class Arya1:
    def hod():
        print("hod")
a1 = Arya1.hod()
print(a1)

class Arya2:
    def __init__(self):
        self.a=10 #instance var
a2=Arya2()
print(a2.a)


class AryaOld:
    def __init__(self, address, director):
        self.address=address
        self.director=director
obj=AryaOld("Kukas, Jaipur", "xyz")
print(obj.address)
print(obj.director)

class Arya3:
    def __init__(self, name, position):
        self.name=name
        self.position=position
    def mussu(self):
        print(self.name)
        print(self.position)
obj=Arya3("Chirag Agrawal","Student")
obj.mussu()