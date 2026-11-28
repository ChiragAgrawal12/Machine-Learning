class Arya:
    def __init__(self):
        self.__accountno = 1234    #private    ( double underscore makes it private)
        self._name = "Arya"        #protected  ( single underscore makes it protected)
        self.labno = 306           #public     ( no underscore makes it public)
class Student(Arya):
    print("AIETM")
S1=Student()
print(S1.labno)                    # public access modifier can be accessed anywhere
print(S1._name)                    # protected access modifier can be accessed in derived class but not outside the class
print(S1.__accountno)              # private access modifier cannot be accessed outside the class

# How to access private variable outside the class
print(S1._Arya__accountno)         # private access modifier can be accessed outside

