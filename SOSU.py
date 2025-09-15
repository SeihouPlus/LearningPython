def getPrimes(x=2):
    while True:
        for i in range(2,x):
            if x % i == 0:
                break
        else:
            yield x
        x+=1

i = getPrimes()

for c in range(20):
    print(next(i))
