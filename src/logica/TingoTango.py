class TingoTango:
    def textoTingoTango(self, numero):
        if (numero % 5 == 0) and (numero % 3 == 0):
            return "TingoTango"
        elif(numero % 3 == 0):
            return "Tingo"
        elif(numero % 5 == 0):
            return "Tango"
        return str(numero)