# Idea: a child class inherits attributes and methods from a parent class
# The child can reuse and extend behaviors

# Base Class (parent)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

# Child classes (inheritance)
class Dog(Animal):
    def bark(self): # extend function
        print(f"{self.name} is barking")

class Cat(Animal):
    def meow(self): # extend function
        print(f"{self.name} is meowing")

# Usage
dog = Dog("Buddy")
cat = Cat("Kitty")

dog.eat()
dog.bark()

cat.eat()
cat.meow()
