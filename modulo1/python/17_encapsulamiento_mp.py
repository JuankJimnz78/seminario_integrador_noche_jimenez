class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("Precio inválido")

    def mostrar(self):
        print(f"Producto: {self._nombre} - Precio: ${self._precio}")

p = Producto("Aceite", 3.50)
p.mostrar()
p.precio = 4.00
p.mostrar()
