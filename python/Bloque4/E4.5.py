from abc import ABC, abstractmethod

from math import pi

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
            pass

class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2

    def perimetro(self):
        return 2 * pi * self.radio

class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
            return self.lado * 4



class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Cuadrado(3)
]

for figura in figuras:
    print("Área:", figura.area())
    print("Perímetro:", figura.perimetro())
    print()