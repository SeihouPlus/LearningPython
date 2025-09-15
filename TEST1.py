def method1(func):
    def methodIn(*args):
        print("引数:", args)
        return func(*args)
    return methodIn

@method1
def delMethod(a, b):
    return a + b

# newFunc = method1(delMethod)

result = delMethod(10, 20)
print(result)
