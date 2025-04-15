class AryaStudent:
    def __init__(self, name, age):
        self.name =name
        self.__age =age     #private

    def get_age(self):
        return self.__age

p= AryaStudent("Chirag",22)
print(p.name)
print(p.get_age())            
print(p._AryaStudent__age)
