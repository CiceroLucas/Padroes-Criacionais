from abc import ABC, abstractclassmethod

# Produto
class Carro:
    
    def __init__(self):
        self.modelo = None
        self.cor = None
        self.ano = None

    def __str__(self):
        return f"Carro: Modelo - {self.modelo}, Cor - {self.cor}, Ano - {self.ano}"

# Interface do construtor
class Builder(ABC):

    @abstractclassmethod
    def build_modelo(self):
        pass

    @abstractclassmethod
    def build_cor(self):
        pass

    @abstractclassmethod
    def build_ano(self):
        pass

    @abstractclassmethod
    def get_carro(self):
        pass

# Construtor
class CarroBuilder(Builder):

    def __init__(self):
        self.carro = Carro()

    def build_modelo(self, modelo):
        self.carro.modelo = modelo

    def build_cor(self, cor):
        self.carro.cor = cor

    def build_ano(self, ano):
        self.carro.ano = ano

    def get_carro(self):
        return self.carro

# Diretor - Responsável por construir o objeto usando o construtor
class Diretor:

    def __init__(self, builder):
        self.builder = builder

    def construir_carro(self, modelo, cor, ano):
        self.builder.build_modelo(modelo)
        self.builder.build_cor(cor)
        self.builder.build_ano(ano)

if __name__ == "__main__":
    builder = CarroBuilder()
    diretor = Diretor(builder)

    diretor.construir_carro("Sedan", "Prata", 2023)
    carro = builder.get_carro()

    print(carro)
