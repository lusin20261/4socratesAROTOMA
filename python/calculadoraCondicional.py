print("================================")
print     ("MI CALCULADORA DE AURA")
print("================================")

while True:
    print("")
    print("¿que operación desea realizar?")
    print("1. sumar")
    print("2. restar")
    print("3 .multiplicar")
    print("4 .división")
    print("5 .salir")
    print("------------------------------")

    opción = input ("Elige una opción: ")

    if opción == "1":
        num1 = input("Ingreso el primer número: ")
        num1 = int(num1)
        num2 = input("Ingreso el segundo número")
        num2 = int(num2)
        print("El resultado de la suma es:", num1+num2 )

    elif opción == "2":
        num1 = input("Ingreso el primer número")
        num1 = int(num1)
        num2 = input("Ingreso ")