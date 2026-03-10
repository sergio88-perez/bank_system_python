class CuentaBancaria:

    def __init__(self, titular, nro_cuenta):
        self.titular = titular
        self.nro_cuenta = nro_cuenta
        self.__saldo = 0

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print("Deposito exitoso")
        else:
            print("Monto invalido")

    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            print("Retiro exitoso")
        else:
            print("Monto invalido")

    def transferir(self, otra_cuenta, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            otra_cuenta.__saldo += monto
            print("Transferencia exitosa")
        else:
            print("Monto invalido")

    def mostrar_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Cuenta: {self.nro_cuenta}")
        print(f"Saldo: {self.__saldo}")