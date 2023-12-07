# Fábrica abstrata
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing Circle"

class Square(Shape):
    def draw(self):
        return "Drawing Square"

# Fábrica de cores
class Color:
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        return "Filling with Red"

class Blue(Color):
    def fill(self):
        return "Filling with Blue"

# Fábrica abstrata
class AbstractFactory:
    def create_shape(self):
        pass

    def create_color(self):
        pass

# Fábrica concreta
class ConcreteFactory1(AbstractFactory):
    def create_shape(self):
        return Circle()

    def create_color(self):
        return Red()

# Uso do Abstract Factory
factory1 = ConcreteFactory1()
shape = factory1.create_shape()
color = factory1.create_color()

print(shape.draw())  
print(color.fill())  
