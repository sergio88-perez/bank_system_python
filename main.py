from service.banco_service import banco, crear_cuenta, buscar_cuenta
from utils.menu import mostrar_menu

while True:

    mostrar_menu()

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:

        nombre = input("Nombre: ")
        numero = int(input("Numero de cuenta: "))

        crear_cuenta(nombre, numero)

    elif opcion == 2:

        numero = int(input("Ingrese el numero de cuenta para realizar deposito: "))
        cuenta = buscar_cuenta(numero)

        if cuenta:
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        else:
            print ("cuenta no encontrada")

    elif opcion == 3:
        numero = int(input("Ingrese el numero de cuenta para realizar retiro: "))
        cuenta = buscar_cuenta(numero)

        if cuenta:
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        else:
            print ("cuenta no encontrada")

    elif opcion == 4:

        origen = int(input("Ingrese cuenta de origen: "))
        destino = int(input ("Ingrese cuenta de destino: "))
        cuenta_origen = buscar_cuenta(origen)
        cuenta_destino = buscar_cuenta (destino)

        if cuenta_origen and cuenta_destino:

            monto = float(input("Ingrese el montro a transferir: "))
            cuenta_origen.transferir(cuenta_destino, monto)

        else:
            print ("Una de las cuentas no existe")

    elif opcion == 5:

        if not banco:
            print("No hay cuentas")

        else:
            for cuenta in banco:
                cuenta.mostrar_datos()

    elif opcion == 6:
        print("Saliendo del sistema")
        break