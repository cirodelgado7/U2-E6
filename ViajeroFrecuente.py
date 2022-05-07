class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, numero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = numero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def __str__(self):
        return "{}   {}   {:20}   {:20}   {}" \
            .format(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)

    def __gt__(self, other):
        return self.__millas_acum > other.__millas_acum

    def __add__(self, other):
        return self.__millas_acum + other

    def __sub__(self, other):
        return self.__millas_acum + other

    def obtenerNumero(self):
        return self.__num_viajero

    def obtenerDNI(self):
        return self.__dni

    def obtenerNombre(self):
        return self.__nombre

    def obtenerApellido(self):
        return self.__apellido

    def obtenerMillas(self):
        return self.__millas_acum

    def modificarMillas(self, c):
        self.__millas_acum += c
