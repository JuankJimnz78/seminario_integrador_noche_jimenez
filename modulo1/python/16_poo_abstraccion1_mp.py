from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def mostrar(self):
        pass

class Alimento(Producto):
    def mostrar(self):
        print(f"Alimento: {self.nombre} - Precio: ${self.precio}")

arroz = Alimento("Arroz", 1.25)
arroz.mostrar()
