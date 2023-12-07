# Método de Fábrica
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()

# Uso do Factory Method
factory = AnimalFactory()
dog = factory.create_animal('dog')
print(dog.make_sound()) 
