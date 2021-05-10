import sys
from ClaseFechaHora import FechaHora

class Menu:
    __switcher = None

    def __init__(self):
        __switcher = None
        self.__switcher = {
            1: self.sumar,
            2: self.restar,
            3: self.comparar,
            4: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, r1,r2):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(r1,r2)

    def sumar(self, r1, r2):
        suma = r1 + r2
        FechaHora.Mostrar(suma)

    def restar(self, r1, r2):
        if r1 > r2:
            resta = r1 - r2
            FechaHora.Mostrar(resta)
        else:
            resta = r2 - r1
            FechaHora.Mostrar(resta)

    def comparar(self, r1, r2):
        mayor = r1 > r2
        if mayor:
            print('La primera fecha ingresada es mayor')
        else:
            print('La segunda fecha ingresada no es mayor')

    def salir(self, r1,r2):
        sys.exit(0)