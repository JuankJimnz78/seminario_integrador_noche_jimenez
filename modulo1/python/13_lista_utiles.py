print("Manipulacion de listas")
print("Crear una lista ")
vacia = []
print(vacia)
numeros = [1, 2, 3, 4, 5]
print(numeros)
nombres = ["Jimenez", "Maria", "Carlos"]
print(nombres)
mixta = [1, "Hola", 3.14, True]
print(mixta)
anidada = [1, [2, 3], [4, 5, 6]]
print(anidada)

print("Acceder a elementos de la lista")
print(nombres[1])
print(nombres[-1])
print(nombres[0:2])
print(nombres[::2])

print("CRUD en listas")
frutas = ["Manzana", "Pera", "Naranja", "Plátano"]
print(frutas)
#agregar
frutas.insert(1, "Kiwi")
print(frutas)
frutas.append("Mango")
print(frutas)
frutas.extend(["Fresa", "Melón"])
print(frutas)

#modificar
frutas[2] = "Limón"
print(frutas)

#eliminar
frutas.remove("Plátano")
print(frutas)
eliminado=frutas.pop(3)
print(eliminado)
print(frutas)
del frutas[0]
print(frutas)

print("Buscar valores en los elementos de una lista")
print("Pera" in frutas)
print(frutas.index("Mango"))
print(frutas.count("Fresa"))

print("Ordenar una lista")
numeros_desordenados = [5, 2, 9, 1, 5, 6]
print(numeros_desordenados)

numeros_desordenados.sort()
print(numeros_desordenados)

numeros_desordenados.sort(reverse=True)
print(numeros_desordenados)

ordenada = sorted(numeros_desordenados)
print(ordenada)
print(numeros_desordenados)


