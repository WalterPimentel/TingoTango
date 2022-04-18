class TingoTango:
    def textoTingoTango(self, numero):
        s = ""
        if not type(numero) is int:
            return "Error: Ingresa un entero"
        if(numero % 3 == 0):
            s += "Tingo"
        if(numero % 5 == 0):
            s += "Tango"
        if(len(s)):
            return s
        else:
            return str (numero)