print("Ciclos for")
print("for basico")

for i in range(1,6):
    print(i)

frutas=["manzana","banana","naranja"]
for fruta in frutas:
    print(fruta)

print("control de interrupcion")
for i in range(1,10):
    if i==3:continue
    if i==7:break
    print(i)
else:
    print("Terminado el ciclo")

print("for con rango step")
for i in range(0,10,2):
    print(i)

print("for con rango regresivo")
for i in range(10,0,-1):
    print(i)

print("for con enumerate")
nombres=["Ana","Luis","Carlos","pedro"]
for indice, nombre in enumerate(nombres):
    print(indice, nombre)

print("for con zip")
edades=[18,11,25,56]
for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

print("for anidados")
for i in range(1,4):
    for j in range(1,4):
        print(i, j)

cantidad=int(input("Ingrese la cantidad de notas"))
suma=0
for i in range(1,cantidad+1):
    nota=float(input(f"nota {i}: "))
    suma+=nota
promedio=suma/cantidad
print("El promedio es:", promedio)
if promedio>=7:
    print("Aprobado")
else:
    print("Reprobado")