from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
from PIL import Image, ImageTk
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from i_parser import analizador
from lexer import Analizador_lexico

class Aplicacion:
    nombrearch1 = ""
    bandera = False
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.config(bg = "sky blue")
        self.image2 = Image.open('marco.jpg')
        self.image1 = ImageTk.PhotoImage(self.image2)
        self.w = self.image1.width()
        self.h = self.image1.height()
        self.ventana1.geometry('%dx%d+0+0' % (self.w, self.h))
        self.ventana1.resizable(width=False , height= False)
        self.label1 = Label(self.ventana1, image=self.image1)
        self.label1.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana1.title("IDE karul")
        self.agregar_menu()
        self.agregar_campo_de_trabajo()
        self.ventana1.mainloop()

    def agregar_campo_de_trabajo(self):

        self.scrolledtext1 = st.ScrolledText(self.ventana1, width=80, height=15)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
        self.scrolledtext2 = st.ScrolledText(self.ventana1,state=DISABLED,width=80, height=10)
        self.scrolledtext2.grid(padx=0, pady=10)

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar archivo", command=self.guardar)
        opciones1.add_command(label="Recuperar archivo", command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
        menubar1.add_command(label="Compilar", command=self.compilar)
        menubar1.add_command(label = "Actualizar", command = self.actualizar)

    def salir(self):
        sys.exit()

    def guardar(self):
        self.scrolledtext2["state"] = NORMAL
        nombrearch=fd.asksaveasfilename(initialdir = self.nombrearch1,title = "Guardar como",filetypes = (("karul files","*.karul"),("todos los archivos","*.*")))+'.karul'
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            self.nombrearch1 = nombrearch
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")
            self.scrolledtext2.delete("1.0", tk.END)
            self.bandera = False
        self.scrolledtext2["state"] = DISABLED

    def recuperar(self):
        self.scrolledtext2["state"] = NORMAL
        nombrearch=fd.askopenfilename(initialdir = self.nombrearch1,title = "Seleccione archivo",filetypes = (("karul files","*.karul"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)
            self.nombrearch1 = nombrearch
            self.scrolledtext2.delete("1.0", tk.END)
            self.bandera = False
        self.scrolledtext2["state"] = DISABLED

    def actualizar(self):
        self.scrolledtext2["state"] = NORMAL
        if self.nombrearch1 != "":
            archi1 = open(self.nombrearch1, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            self.scrolledtext2.delete("1.0", tk.END)
            self.bandera = False
        else:
            mb.showerror("Error","Necesitas guardar los datos!!")
        self.scrolledtext2["state"] = DISABLED

    def compilar(self):
        self.scrolledtext2["state"]=NORMAL
        if self.bandera == False:
            resultado = str(Analizador_lexico(self.nombrearch1))
            if (resultado == ""):
                resultado = str(analizador(self.nombrearch1))
            self.scrolledtext2.insert("1.0", resultado)
            self.bandera = True
            #print(analizador(self.nombrearch1))
        else:
            mb.showerror("Error","No puedes compilar lo mismo otra ves")
        self.scrolledtext2["state"] = DISABLED



aplicacion1=Aplicacion()