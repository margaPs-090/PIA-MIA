# E4.1 Clase CuentaBancaria con saldo privado, ingresar, retirar
#(valida saldo suficiente) y propiedad saldo de solo lectura

class CuentaBancaria:

    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self._saldo = saldo

    
    @property
    def saldo(self):
        return self._saldo

     def ingresar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print("Ingreso realizado")
        else:
            print("Error, cantidad incorrecta")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print("Retirada realizada")
        else:
            print("Saldo insuficiente, no se puede realizar la operación")

cuenta = CuentaBancaria("Marga", 100)
print("Saldo inicial:", cuenta.saldo)
cuenta.retirar(30)

print("Titular:", cuenta.titular)
print("Saldo:", cuenta.saldo)