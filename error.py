

class error():
    def __init__(self, caracter, tipo, linea, columna):
        self.caracter = caracter
        self.tipo = tipo 
        self.linea = linea 
        self.columna = columna 

    def mostrar(self):
        print("=================================")
        print("caracter: " + self.caracter)
        print("Tipo: " + self.tipo)
        print("Linea: " + str(self.linea))
        print("Columna: " + str(self.columna))
        