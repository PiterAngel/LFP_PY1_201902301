import os
contenido = ""


def Inicio():
    global contenido
    contenido += """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="shortcut icon" href="Icono.ico">
    <title>Reporte de Tokens</title>
  </head>
  <body>
   
    <div class="p-3 mb-2 text-white" style="background-color:#3DBFD3;">
        <h1><center>Reporte de Tokens</center></h1>
    </div>"""


def tablat(Tokens):
    global contenido
    contenido += """</div>
    <table class="table table-dark table-hover table-bordered">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Tipo de Token</th>
      <th scope="col">Lexema</th>
      <th scope="col">Linea</th>
      <th scope="col">Columna</th>
    </tr>
  </thead>
  <tbody>"""
    contador = 1
    for token in Tokens:
        contenido += """
        <tr class="table-secondary">
      <th scope="row">""" + str(contador) + """</th>
      <th>""" + str(token.tipo) + """</th>
      <th>""" + str(token.lexema) + """</th>
      <th>""" + str(token.linea) + """</th>
      <th>""" + str(token.columna) + """</th>
    </tr>
        """
        contador += 1

    contenido += """</tbody>
</table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
</html>"""


def creararchivo():
    global contenido
    archivo = open('Reporte_Tokens.html', 'w', encoding='utf8')
    archivo.write(contenido)
    archivo.close()
    os.startfile('Reporte_Tokens.html')


def generararchivoT(Tokens):
    Inicio()
    tablat(Tokens)
    creararchivo()
