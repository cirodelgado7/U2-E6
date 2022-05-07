import csv
from ViajeroFrecuente import ViajeroFrecuente


class Manejador:
    __listaViajeros = []

    def __init__(self):
        self.__listaViajeros = []

    def __str__(self):
        s = ""
        for lista in self.__listaViajeros:
            s += str(lista) + '\n'
        return s

    def testViajeros(self):
        archivo = open('ViajeroFrecuente.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                numero = int(fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas = int(fila[4])
                unViajero = ViajeroFrecuente(numero, dni, nombre, apellido, millas)
                self.__listaViajeros.append(unViajero)
        archivo.close()
        print('\n ***** Lista de Viajeros Frecuentes *****')
        print(self.__str__())

    def buscarViajero(self, clave):
        i = 0
        while i < len(self.__listaViajeros):
            if self.__listaViajeros[i].obtenerNumero() == clave:
                return i
            i = i + 1

    def obtenerViajero(self, indice):
        return self.__listaViajeros[indice]

    def acumularMillas(self, unViajero, cantidad):
        m = unViajero.modificarMillas(unViajero, cantidad)
        return m

    def canjearMillas(self, unViajero, cantidad):
        if ViajeroFrecuente.obtenerMillas(unViajero) >= cantidad:
            ViajeroFrecuente.modificarMillas(unViajero, - cantidad)
            print('\n El canje se realizó con éxito ')
        else:
            print('\n La cantidad de millas que dispone es insuficiente para realizar el canje \n')
        return ViajeroFrecuente.obtenerMillas(unViajero)

    def compararMillas(self, unViajero):
        print("El/los viajero/s con mayor contidad de millas:")
        m = self.__listaViajeros[0].obtenerMillas()
        for i in range(len(self.__listaViajeros)):
            if self.__listaViajeros[i] > unViajero:
                m = self.__listaViajeros[i].obtenerMillas()
        for i in range(len(self.__listaViajeros)):
            if self.__listaViajeros[i].obtenerMillas() == m:
                print(self.__listaViajeros[i])

