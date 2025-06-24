# Classes are basically user defined prototype or blueprint
class Calculator:
    num = 100

    #Default Constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2,3)
obj.getData()
print(obj.Summation())
#print(obj.num)

print("\n************ Another Object **************\n")

obj = Calculator(4,5)
obj.getData()
print(obj.Summation())
#print(obj.num)