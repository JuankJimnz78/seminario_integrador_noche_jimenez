print("Funciones en Python")
print("Funcion basica")
def saludar():
    print("Hola, bienvenido a UTE")

saludar()
print("Funcion con parametros")
def saludarConNombre(nombre):
    print(f"Hola, {nombre}, Que tal")

saludarConNombre("Jimenez")
saludarConNombre("Maria")

print("Funcion con retorno")
def sumar(a, b):
    return a + b
print(sumar(5, 3))

print("Funcion por posicion y por nombre")
def presentar(nombre, edad, ciudad):
    print(f"Senor(a): {nombre} edad: {edad}, ciudad: {ciudad} ")
presentar("Jimenez", 30, "Quito")
presentar("Maria", 25, "Guayaquil")
presentar(ciudad="Cuenca", nombre="Carlos", edad=40)

print("Funcion con valor de parametros por defecto")
def saludo_con_valores(nombre="Amigo", saludo="Hola", puntuacion="!"):
    print(f"{saludo} {nombre}{puntuacion}")
saludo_con_valores()
saludo_con_valores("Jimenez", puntuacion="...")
saludo_con_valores(saludo="Bienvenido", nombre="Maria")

print("Funcion con parametros posicionales variables")
def sumar_todos(*args):
    print(f"Los numeros a sumar son: {args}")
    return sum(args)
print(sumar_todos(1, 2, 3))
print(sumar_todos(5, 10, 15, 20))
print(sumar_todos(2, 4, 6, 8, 10))

print("Funciones parametros combinados con posicionales variables")
def mostrar_info(titulo, *datos):
    print(f"parametros recibidos {datos},{titulo}")
    print(titulo)
    for dato in datos:
        print(f"- {dato}")
mostrar_info("Frutas", "Naranja", "Pera", "Manzana")
    

print("Funciones parametros clave valor variables")
def crear_perfil(**kwargs):
    print(f"parametros recibidos: {kwargs}")
    for clave, valor in kwargs.items():
        print(f"- {clave}: {valor}")
crear_perfil(nombre="Jimenez", apellido="Garcia", edad=30, ciudad="Quito")

print("Funciones con parametros combinados con todos los tipos")
def configurar(host, *puertos, debug=False, **opciones):
    print(f"Host: {host}")
    print(f"Puertos: {puertos}")
    print(f"Debug: {debug}")
    print(f"Opciones: {opciones}")

configurar("localhost", 80, 443, debug=True, ssl=True, timeout=30)

print("Devolver multiples valores")
def minmax(numeros):    
    return min(numeros), max(numeros)

minimo, maximo = minmax([3, 1, 4, 1, 5, 9])
print(f"Minimo: {minimo}, Maximo: {maximo}")
_, maximo = minmax([3, 1, 4, 1, 5, 9])
print(f"Maximo: {maximo}")
minimo, _ = minmax([3, 1, 4, 1, 5, 9])
print(f"Minimo: {minimo}")

print("Devolver direccionar en el caso de muchos valores")
def analizar(numeros):
    total=sum(numeros)
    n=len(numeros)
    return {
        "total": total,
        "media": total/n if n > 0 else 0,
        "minimo": min(numeros) if numeros else None,
        "maximo": max(numeros) if numeros else None,
        "count": n,
    }

datos= [12,334,56,78,90]
stats=analizar(datos)
print(f"Total: {stats['total']}")
print(f"Media: {stats['media']}")
print(f"Rango: {stats['minimo']} - {stats['maximo']}")
print(f"Count: {stats['count']}")

print("Funciones lambda")
def doble(numero):
    return numero * 2
duplicar=lambda x: x * 2
print (doble(2))
print(duplicar(3))
sumar=lambda a, b: a + b
print(sumar(5, 7))

