print("Diccionarios")
print("Crear diccionario")
vacio = {}
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Quito"}
config=dict(host= "localhost", puerto= 8080)

#acceso
print(persona["nombre"])

#CRUD en diccionarios
#modificar
persona["nombre"] = "Carlos"
print(persona)
del persona["edad"]
print(persona)

#verificar existencia de clave
print("nombre" in persona)
print("ciudad" in persona)

#metodos escenciales
print(persona.keys())
print(persona.values())
print(persona.items())

#iterar sobre un diccionario
for clave, valor in persona.items():
    print(f"clave: {clave}, valor: {valor}")