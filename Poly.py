

class Animal:
    def sound(self):
        
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"


def make_sound(animal):
    print(animal.sound())


dog = Dog()
cat = Cat()
cow = Cow()


make_sound(dog)  
make_sound(cat)  
make_sound(cow)  
