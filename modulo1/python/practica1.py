print ("Hola Mundo")

texto = "Aprediendo Python"

print(texto.upper())
print(texto.lower())
print(texto[0:12])

#texto = input("Ingresa un texto:")
#print(texto)

#edad = input("Ingresa tu edad:")
#print("Tu edad es: ", edad)

a, b = 3,5
suma= a+b
resta=a-b
dividir=a/b
multiplicar=a*b
residuo=a%b
potencia=a**b
cociente=a//b

print("Lasuma es: ", suma)
print("La resta es: ", resta)
print("La division es: ", dividir)
print("La multiplicacion es: ", multiplicar)
print("El residuo es:", residuo)   

print(5>3)
print(10==10)

print(True and False)
print(True or False)
print(not True)

def saludar(nombre):
    return f"Buenos dias {nombre}"
nombre=input("Ingresa tu nombre:")
print(saludar(nombre))

numeros = [1,2,3,4,5]
numeros.append(7)
print(numeros)

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(persona["ciudad"], persona["edad"])

print(saludar(nombre))


