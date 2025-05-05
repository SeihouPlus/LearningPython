
year = 2025

if 1 in [0, 1, 2, [1 , 3], 2, 4]:
    print(year, "あったよ")
else:
    print("ないね")

# -- -- -- 

import random

def viewer(maxNum):
    for num in range(maxNum):
        print(num)

maxN = random.randint(1, 10)
viewer(maxN)

#---

dice1 = {1, 1, 2, 3 ,3 ,5, 7, 9}
dice2 = {2, 3, 6, 7}

dice3 = dice1 ^ dice2

print(dice3)


#--

import matplotlib.pyplot as plt

def ShowPlot():
    str_speeds = "38 42 20 40 39"
    str_armor = "80 50 17 50 51"

    speeds = str_speeds.split()
    armors = str_armor.split()

    markers = ["o", "v", "^", "<", ">"]

    for idx in range(len(speeds)):
        x = int(speeds[idx])
        y = int(armors[idx])

        plt.scatter(x, y, marker=markers[idx])

    plt.show()

ShowPlot()

#--
val = "{0:.2%}".format(6381/12708, 1.5)

print(val)

#--


test = {"o":4}

test["a"] = 1
test["b"] = 2

test2 = test.pop("e", 3)
#del test["a"]

print(test2)
print(test)

#--



def Naihou():

    monks = [158, 157, 163, 157, 145]

    total = sum(monks)
    leng = len(monks)
    ave = total / leng

    return ([(monk-ave) for monk in monks ])

test = Naihou()

print(test)

#--



def getPrimes(x = 2):
    
    while True:
        
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            yield x
        
        x += 1
        

ret = getPrimes()

for r in range(10):
    print(next(ret))


#--


class MyClass:

    def __init__(self, msg):
        self.__message = msg

    def __str__(self):
        return self.message
    
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, msg):
        self.__message = msg
        

myc = MyClass("わたしですよ")

#-- print(myc.__message)
print(myc.message)

myc.message += "　わたしももね"

print(myc.message)

myc.test = "aaa"

print(myc.test)

#--


