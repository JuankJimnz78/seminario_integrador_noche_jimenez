class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"Producto: {self.nombre} - Precio: ${self.precio}")

class Bebida(Producto):
    def __init__(self, nombre, precio, tamano):
        super().__init__(nombre, precio)
        self.tamano = tamano

    def mostrar(self):
        print(f"Bebida: {self.nombre} ({self.tamano}) - Precio: ${self.precio}")

jugo = Bebida("Jugo de naranja", 2.00, "1L")
jugo.mostrar()
