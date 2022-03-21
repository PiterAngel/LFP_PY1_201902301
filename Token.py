

class Token():
    def __init__(self, tipo, lexema, linea, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.linea = linea
        self.columna = columna

    def mostrar(self):
        print("=================================")

        print("Tipo: " + self.tipo)
        print("lexema: " + self.lexema)
        print("Linea: " + str(self.linea))
        print("Columna: " + str(self.columna))
