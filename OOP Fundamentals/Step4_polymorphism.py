# idea:
# 1. same method name
# 2. different behavior
# 3. decided at runtime

from abc import ABC, abstractmethod
from token import NAME

class Animal(ABC):
    def  __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass

# Child classes override the method
class Dog(Animal):
    def make_sound(self): # from the parent class
        return "Bark"

class Cat(Animal):
    def make_sound(self): # from the parent class
        return "Meow"

# Polymorphic function
def play_sound(animal: Animal):
    print(animal.make_sound())

# usage
dog = Dog("Buddy")
cat = Cat("Kitty")

play_sound(dog)
play_sound(cat)

# this is polymorphism
# 1. same function: make_sound()
# 2. different behavior
# 3. depends on the object type, not the code calling it 
# easy to add new animals, clean and scalable