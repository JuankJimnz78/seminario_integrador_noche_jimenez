print("Match - case")
comando=input("Comando iniciar/parar/reiniciar: ")
match comando:
    case "iniciar":
        print("Sistema iniciado")
    case "parar":
        print("Sistema detenido")
    case "reiniciar":
        print("Sistema reiniciado")
    case _:
        print(f"Comando {comando} no reconocido")

print("match con condiciones")
numero=int(input("Ingrese un número: "))
match numero:
    case n if n<0:
        print("Número negativo")
    case 0:
        print("Número cero")
    case n if n % 2 == 0:
        print(f"el número {n} es positivo y par")

    case n:
        print(f"el número {n} es positivo e impar")
        