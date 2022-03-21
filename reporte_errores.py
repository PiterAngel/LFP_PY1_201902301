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
    <title>Reporte de Errores</title>
  </head>
  <body>
    
    <div class="p-3 mb-2 text-white" style="background-color:#900C3F">
        <h1><center>Reporte de Errores</center></h1>
    </div>"""


def tablaer(Errores):
    global contenido
    contenido += """<table class="table table-dark table-hover table-bordered">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Tipo de Error</th>
      <th scope="col">Caracter(es)</th>
     
      <th scope="col">Linea</th>
      <th scope="col">Columna</th>
    </tr>
  </thead>
  <tbody>"""
    contador = 1
    for error in Errores:
        contenido += """
        <tr class="table-secondary">
      <th scope="row">""" + str(contador) + """</th>
      <th>""" + str(error.tipo) + """</th>
      <th>""" + str(error.caracter) + """</th>
 
      <th>""" + str(error.linea) + """</th>
      <th>""" + str(error.columna) + """</th>
    </tr>
        """
        contador += 1

    contenido += """</tbody>
</table>"""


def creararchivo():
    global contenido
    archivo = open('Reporte_Errores.html', 'w', encoding='utf8')
    archivo.write(contenido)
    archivo.close()
    os.startfile("Reporte_Errores.html")


def generararchivoE(Errores):
    Inicio()
    tablaer(Errores)

    creararchivo()
