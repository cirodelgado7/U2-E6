import os
import sys

from ManejadorViajero import Manejador


class Menu:
    __switcher = None

    def __init__(self):
        __switcher = None
        self.__switcher = {
            1: self.consultarM,
            2: self.acumularM,
            3: self.canjearM,
            4: self.compararM,
            5: self.acumularS,
            6: self.canjearS,
            7: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, mv, unViajero):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mv, unViajero)

    def consultarM(self, mv, unViajero):
        m = unViajero.obtenerMillas()
        print('\n El viajero tiene {} millas disponibles \n'.format(m))
        os.system('pause')

    def acumularM(self, mv, unViajero):
        c = int(input('\n Cantidad de millas recorridas: '))
        a = unViajero.acumularMillas(c)
        print('\n El viajero acumuló {} millas \n'.format(a))
        os.system('pause')

    def canjearM(self, mv, unViajero):
        c = int(input('\n Ingrese la cantidad de millas a canjear: '))
        m = unViajero.canjearMillas(c)
        print('\n El Viajero dispone de {} millas para canjear \n'.format(m))
        os.system('pause')

    def compararM(self, mv, unViajero):
        mv.compararMillas(unViajero)

    def acumularS(self, mv, unViajero):
        unViajero = unViajero + 100
        print('\nEl viajero acumuló {} millas'.format(unViajero))

    def canjearS(self, mv, unViajero):
        unViajero = unViajero - 100
        print('\nEl viajero canjeó {} millas'.format(unViajero))

    def salir(self, mv, unViajero):
        sys.exit(0)
