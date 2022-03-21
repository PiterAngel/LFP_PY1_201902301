import tkinter as tk
from tkinter import scrolledtext
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import webbrowser
from tkinter import *
from tkinter import messagebox
from analizador_lexico import analizador_lexico
from reporte_token import *
from reporte_errores import *


class Aplicacion:

    def __init__(self):
        self.scanner = analizador_lexico()
        self.ventana1 = tk.Tk()
        self.agregar_menu()
        self.scrolledtextxd = scrolledtext.ScrolledText(
            self.ventana1, width=80, height=20,)
        self.scrolledtextxd.grid(column=0, row=0, padx=80, pady=10)
        # self.ventana1.config(bg='#00144F')
        self.ventana1.iconbitmap('fondoss.ico')
        self.ventana1.resizable(0, 0)
        self.ventana1['bg'] = '#49A'
        # self.ventana1.PhotoImage(file="fondoss.jpg")
# =====================BOTON=============================
        self.boton1 = tk.Button(self.ventana1, text="Menú",
                                width=10, height=3, bg="gray", fg="red")
        self.boton1.place(x=0, y=5)
# =====================BOTON=============================
        self.boton2 = tk.Button(self.ventana1, text="Analizar",
                                width=10, height=3, command=self.mensaje, bg="gray")
        self.boton2.place(x=0, y=70)
# ========================================================
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubarxd = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubarxd)
        opciones1 = tk.Menu(menubarxd, tearoff=0)
        #opciones1.add_command(label="Guardar archivo", command=self.guardar)
        opciones1.add_command(label="Abrir archivo",
                              command=self.abrir)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubarxd.add_cascade(label="Archivo", menu=opciones1)
        # ============================================
        self.ventana1.config(menu=menubarxd)
        opciones2 = tk.Menu(menubarxd, tearoff=0)
        opciones2.add_command(label="Reporte de Tokens",
                              command=self.generarRt)
        opciones2.add_command(label="Reporte de errores",
                              command=self.generarRe)
        opciones2.add_command(label="Manual de Usuario", command=self.pdf1)
        opciones2.add_command(label="Manual Tecnico", command=self.pdf2)
        opciones2.add_separator()
        opciones2.add_command(label="Salir", command=self.salir)
        menubarxd.add_cascade(label="Reportes", menu=opciones2)
        # ============================================

    def generarRt(self):

        generararchivoT(self.scanner.Tokenzz)

    def generarRe(self):
        generararchivoE(self.scanner.errorezz)

    def salir(self):
        sys.exit()

    def guardar(self):
        nombrearch = fd.asksaveasfilename(initialdir="/", title="Guardar como", filetypes=(
            ("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombrearch != '':
            archi1 = open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtextxd.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información",
                        "Los datos fueron guardados en el archivo.")

    def abrir(self):
        nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo de extensión .form", filetypes=(
            ("form files", "*.form"), ("todos los archivos", "*.*")))
        if nombrearch != '':
            archi1 = open(nombrearch, "r", encoding="utf-8")
            contenido = archi1.read()
            archi1.close()
            self.scrolledtextxd.delete("1.0", tk.END)
            self.scrolledtextxd.insert("1.0", contenido)

    def htmlToken(self):
        f = open('Tokens.html', 'w')

        mensaje = """<html>
        <head></head>
        <body><p>Hola Mundo!</p></body>
        </html>"""

        f.write(mensaje)
        f.close()

        webbrowser.open_new_tab('Tokens.html')

    def htmlerrores(self):
        t = open('errores.html', 'w')

        mensaje = """<html>
        <head></head>
        <body><p>Hola Mundo!</p></body>
        </html>"""

        t.write(mensaje)
        t.close()

        webbrowser.open_new_tab('errores.html')

    def pdf1(self):
        path = 'MANUAL DE USUARIO_PY1.pdf'
        webbrowser.open_new(path)

# [LFP]Tarea2_201902301
    def pdf2(self):
        path = 'MANUAL TECNICO_PY1.pdf'
        webbrowser.open_new(path)

    def mensaje(self):

        if (self.scrolledtextxd.get(1.0, END) != ""):
            contenidoxd = self.scrolledtextxd.get(1.0, END)

            print(contenidoxd)
            self.scanner.analizar(contenidoxd)
            self.scanner.imprimir()

            messagebox.showinfo(
                message="Se analizó correctamente", title="Analizar :0")
        else:
            messagebox.showinfo(
                message="Error, esta vació :c", title="Analizar :0")


aplicacion1 = Aplicacion()
