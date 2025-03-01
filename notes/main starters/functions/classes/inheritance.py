class animal:
    def walk(self):
        print("Walking")


class Dog(animal):
    def bark(self):
        print("Barking")
    

class Cat(animal):
    def meow(self):
        print("Meowing")
    
    
dog1 = Dog()
cat1 = Cat()
dog1.walk()

