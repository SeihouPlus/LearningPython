
class MyClass:

    def __init__(self, msg):
        self.__message = msg

    def __str__(self):
        return self.__message
    

myc = MyClass("わたしですよ")

#-- print(myc.__message)
print(myc)