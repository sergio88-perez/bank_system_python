from models.cuenta import CuentaBancaria

banco = []

def crear_cuenta(nombre, numero):

    cuenta = CuentaBancaria(nombre, numero)
    banco.append(cuenta)

def buscar_cuenta(numero):

    for cuenta in banco:
        if cuenta.nro_cuenta == numero:
            return cuenta

    return None