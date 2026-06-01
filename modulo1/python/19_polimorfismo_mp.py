class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"Producto: {self.nombre} - Precio: ${self.precio}")

class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar(self):
        print(f"Ropa: {self.nombre} - Talla: {self.talla} - Precio: ${self.precio}")

class Alimento(Producto):
    def mostrar(self):
        print(f"Alimento: {self.nombre} - Precio: ${self.precio}")

lista = [
    Ropa("Jeans", 25.00, "M"),
    Alimento("Arroz", 1.25)
]

for p in lista:
    p.mostrar()
