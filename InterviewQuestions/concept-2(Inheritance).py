class Parent:

    def greet(self):
        return "Hello Parent class Rutuja"




class Child(Parent):

    def __init__(self, title):
        self.title = title



    def helloGreet(self):
        return "Hello from child class"

    def greet(self):
        return super().greet()+ " Hello from child "+ self.title


c = Child("Himalaya Shinde Academy")

print(c.greet())
print(c.helloGreet())

# O/P below
# Hello Parent class Rutuja Hello from child Himalaya Shinde Academy
# Hello from child class

