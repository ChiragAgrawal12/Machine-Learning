class Arya:
    def __init__(self):
        self.__accountno = 1234    #private
        self._name = "Arya"        #protected
        self.labno = 306           #public
class Student(Arya):
    print("AIETM")
S1=Student()
print(S1.labno)
print(S1._name)
print(S1.__accountno)
