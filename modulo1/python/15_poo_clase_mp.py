class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"Producto: {self.nombre} - Precio: ${self.precio}")

p = Producto("Leche", 1.50)
p.mostrar()
