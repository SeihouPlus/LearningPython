
class MyClass:
    test = "だれですねん"
    def __init__(self, msg):
        self.__message = msg
        if msg != "":
            self.test = msg

    def __str__(self):
        return self.message
    
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, msg):
        self.__message = msg
        

myc1 = MyClass("わたしですよ")
myc2 = MyClass("")

print(myc1.test)
print(myc2.test)

MyClass.test = "aaaaa"

print(myc1.test)
print(myc2.test)