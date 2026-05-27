
usuario=str(input("ingresa Usuario: "))
pago=str(input("ingresa si o no: "))

if usuario=="premium" and pago=="si":
    print("Acceso completo")
elif usuario=="premium" and pago=="no":
    print("Debe pagar")

else:
    print("Acceso limitado")

