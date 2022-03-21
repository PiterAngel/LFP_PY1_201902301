from Token import Token
from error import error


class analizador_lexico():
    def __init__(self):
        self.Tokenzz = []
        self.errorezz = []

    def analizar(self, textozz):
        self.Tokenzz = []
        self.errorezz = []  # PARA REINICIAR

        textozz += "#"  # para agregar un numeral para saber donde termina
        contadorzz = 0
        linea = 1
        columna = 1
        buffer = ""
        estado = "S0"  # primer estado

        while(contadorzz < len(textozz)):
            # texto en 0 para la primera letra y asi
            letra = textozz[contadorzz]
# ==============================estado=S0===================================================
            if estado == "S0":  # estado para todos los simbolos; estado de aceptacion
                if(letra == "["):
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(
                        Token("corcheteabre", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == "]"):
                    buffer = letra
                    columna += 1  # para ir en cada columna
                    self.Tokenzz.append(
                        Token("corchetecierra", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == "~"):
                    buffer = letra
                    columna += 1
                    if(textozz[contadorzz+1] == ">"):
                        buffer += textozz[contadorzz+1]
                        columna += 1
                        if(textozz[contadorzz+2] == ">"):
                            buffer += textozz[contadorzz+2]
                            columna += 1
                            self.Tokenzz.append(
                                Token("flecha", buffer, linea, columna))
                            buffer = ""
                            buffer = "S0"
                            contadorzz += 2  # aumentar 2 espacios xd
                elif(letra == "<"):
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(
                        Token("menorque", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == ">"):
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(
                        Token("mayorque", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"

                elif(letra == ":"):
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(
                        Token("dospuntos", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == ","):
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(Token("coma", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"

                elif(letra == "\n"):  # aumentar la linea
                    linea += 1
                    columna = 1
                elif(letra == " "):
                    columna += 1
                elif(letra == "\t"):
                    columna += 1
                elif(letra == "f" or letra == "t" or letra == "v" or letra == "n" or letra == "e"):
                    buffer = letra  # guardar primera letra
                    columna += 1
                    estado = "S1"
                elif(letra == '"'):  # si letra es comilla doble para cadena xd
                    buffer = letra
                    columna += 1
                    estado = "S2"
                elif(letra == "'"):
                    buffer = letra
                    columna += 1
                    estado = "S3"
                elif (letra == '#'):  # para cerrar
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(
                        Token("Fin de la lectura", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                    print("=========================================")
                else:
                    self.errorezz.append(
                        error(letra, "error lexico", linea, columna))
                    buffer = ""
                    columna += 1
# ======================estado==S1================================================
            elif estado == "S1":
                # estado para palabras reservadas
                if(letra.isalpha()):
                    buffer += letra
                    columna += 1
                    estado = "S1"
                else:
                    if(buffer == "formulario"):
                        self.Tokenzz.append(
                            Token("ID_formulario", buffer, linea, columna))
                    elif(buffer == "evento"):
                        self.Tokenzz.append(
                            Token("ID_evento", buffer, linea, columna))
                    elif(buffer == "tipo"):
                        self.Tokenzz.append(
                            Token("ID_tipo", buffer, linea, columna))
                    elif(buffer == "nombre"):
                        self.Tokenzz.append(
                            Token("ID_nombre", buffer, linea, columna))
                    elif(buffer == "valor"):
                        self.Tokenzz.append(
                            Token("ID_valor", buffer, linea, columna))
                    elif(buffer == "valores"):
                        self.Tokenzz.append(
                            Token("ID_valores", buffer, linea, columna))
                    elif(buffer == "fondo"):
                        self.Tokenzz.append(
                            Token("ID_fondo", buffer, linea, columna))
                    else:
                        self.errorezz.append(
                            error(buffer, "error lexico", linea, columna))
                    buffer = ""
                    estado = "S0"
                    contadorzz -= 1
# ===========================ESTADO=S2=================================================
# =======================COMILLAS=DOBLES============================================
            elif estado == "S2":
                # validar las cadenas
                if(letra == '"'):
                    buffer += letra
                    columna += 1
                    # segunda comilla
                    self.Tokenzz.append(
                        Token("cadena", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"  # validar para las comillas y regresa al estado 0
                elif(letra == '\n'):
                    columna = 1
                    linea += 1
                elif(letra == "'"):
                    buffer += letra
                    columna += 1
                    self.errorezz.append(
                        error(buffer, "error lexico", linea, columna))
                    buffer = ""
                    estado = "S0"
                else:
                    buffer += letra
                    columna += 1
                    estado = "S2"
# ======================COMILLAS=SIMPLES===================================
            elif estado == "S3":
                # validar las cadenas
                if(letra == "'"):
                    buffer += letra
                    columna += 1
                    # segunda comilla
                    self.Tokenzz.append(
                        Token("cadena", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"  # validar para las comillas y regresa al estado 0
                elif(letra == '\n'):
                    columna = 1
                    linea += 1
                elif(letra == '"'):
                    buffer += letra
                    columna += 1
                    self.errorezz.append(
                        error(buffer, "error lexico", linea, columna))
                    buffer = ""
                    estado = "S0"

                else:
                    buffer += letra
                    columna += 1
                    estado = "S3"

            contadorzz += 1

    def imprimir(self):
        print("Tokens: ")
        for T in self.Tokenzz:
            T.mostrar()
        print("errores")
        for E in self.errorezz:
            E.mostrar()
        print("cantidad de Tokens: " + str(len(self.Tokenzz)))
        print("cantidad de errores: " + str(len(self.errorezz)))
