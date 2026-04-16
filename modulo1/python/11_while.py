print("Ciclos while")
contador=1
while contador<=5:
    print("Contador:",contador)
    contador+=1

dato=""
while dato!="salir":
    dato=input("Ingrese un dato (salir para terminar): ")
    print("Dato ingresado:", dato)

cantidad=int(input("cuantos productos compro"))
total=0
contador=1
while contador<=cantidad:
    precio=float(input(f"Precio del producto {contador}: "))
    total+=precio
    contador+=1
print("Total a pagar:", total)
if total>=100:
    print("aplica descuento")
    
else:
    print("no aplica descuento")