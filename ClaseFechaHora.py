class FechaHora:
    __dd = 0
    __mm = 0
    __aa = 0
    __hs = 0
    __min = 0
    __seg = 0

    def __init__(self, dd, mm, aa, hs, min, seg):
        self.__dd = dd
        self.__mm = mm
        self.__aa = aa
        self.__hs = hs
        self.__min = min
        self.__seg = seg

    def Mostrar(self):
        print('%.2d/%.2d/%.2d\t --- \t%.2d:%.2d:%.2d' % (self.__dd, self.__mm, self.__aa, self.__hs, self.__min, self.__seg))
        self.validaEntrada(self.__dd, self.__mm, self.__aa, self.__hs, self.__min, self.__seg)

    def validaEntrada(self, dd, mm, aa, hs, min, seg):
        valido = False
        if hs in range(0, 24):
            if min in range(0, 60):
                if seg in range(0, 60):
                    if mm in [1, 3, 5, 7, 8, 10, 12]:
                        if dd in range(1, 32):
                            valido = True
                    elif mm in [4, 6, 9, 11]:
                        if dd in range(1, 31):
                            valido = True
                    elif mm == 2:
                        bisiesto = self.bisiesto(aa)
                        if bisiesto:
                            if dd in range(1, 30):
                                valido = True
                        else:
                            if dd in range(1, 29):
                                valido = True
        if valido:
            print('La fecha y la hora ingresadas son válidas')
        else:
            print('La fecha y la hora ingresadas no son válidas')
        return valido

    def bisiesto(self, aa):
        bisiesto = False
        if aa % 4 == 0 and (aa % 100 != 0 or aa % 400 == 0):
            bisiesto = True
        return bisiesto

    def getDia(self):
        return self.__dd

    def getMes(self):
        return self.__mm

    def getAño(self):
        return self.__aa

    def getHora(self):
        return self.__hs

    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg

    def __add__(self, fechahora):
        self.arreglarFechaHora(self.__dd + fechahora.getDia(), self.__mm + fechahora.getMes(),
                               self.__aa + fechahora.getAño(), self.__hs + fechahora.getHora(),
                               self.__min + fechahora.getMin(), self.__seg + fechahora.getSeg())
        return FechaHora(self.__dd, self.__mm, self.__aa, self.__hs, self.__min, self.__seg)

    def __sub__(self, fechahora):
        self.arreglarFechaHora(self.__dd - fechahora.getDia(), self.__mm - fechahora.getMes(),
                          self.__aa - fechahora.getAño(), self.__hs - fechahora.getHora(),
                          self.__min - fechahora.getMin(), self.__seg - fechahora.getSeg())
        return FechaHora(self.__dd, self.__mm, self.__aa, self.__hs, self.__min, self.__seg)

    def __gt__(self, fechahora):
        bool = False
        if self.__aa > fechahora.getAño():
            bool = True
        elif self.__aa < fechahora.getAño():
            pass
        elif self.__mm > fechahora.getMes():
            bool = True
        elif self.__mm < fechahora.getMes():
            pass
        elif self.__dd > fechahora.getDia():
            bool = True
        elif self.__mm < fechahora.getDia():
            pass
        elif self.__hs > fechahora.getHora():
            bool = True
        elif self.__hs < fechahora.getHora():
            pass
        elif self.__min > fechahora.getMin():
            bool = True
        elif self.__min < fechahora.getMin():
            pass
        elif self.__seg > fechahora.getSeg():
            bool = True
        elif self.__seg < fechahora.getSeg():
            pass
        return bool

    def arreglarFechaHora(self, dd, mm, aa, hs, min, seg):
        self.__dd = dd
        self.__mm = mm
        self.__aa = aa
        self.__hs = hs
        self.__min = min
        self.__seg = seg
        acumulador = 0
        if seg >= 60:
            self.__seg = seg % 60
            self.__min += seg // 60
        if min >= 60:
            self.__min = min % 60
            self.__hs += min // 60
        if hs >= 24:
            self.__hs = hs % 24
            self.__dd += hs // 24
        if mm in [1,3,5,7,8,10,12]:
            if self.__dd >= 31:
                if self.__mm >= 12:
                    self.__aa += 1
                    self.__mm = 1
                    self.__dd = (dd % 31) + 1
        elif mm in [4,6,9,11]:
            if dd >= 30:
                self.__mm += dd // 30
                self.__dd = (dd % 30) + 1
        elif mm==2: #  Controlar si el año es bisiesto
            bisiesto = self.bisiesto(aa)

            if bisiesto == True: #  Cambio para los meses de 29 dias
                if dd >= 29:
                    self.__mm += dd // 29  #  suma el resultado de la division.
                    self.__dd = (dd % 29) + 1  #  si la division no da exacta sumo el resto
            else:
                if dd >= 28: #  Cambio para los meses de 28 dias
                    self.__mm += dd // 28
                    self.__dd = (dd % 28) + 1

         #  Actualizacion de meses y años en quinto lugar y ultimo lugar.
        if mm > 12:
            self.__aa += mm // 24
            self.__mm = mm % 24