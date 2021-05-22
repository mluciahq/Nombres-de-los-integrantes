#Creacion de un aventana de acceso general que muestre informacion de aplicacion y  redireccione al usuario con registro y al no regisrtado.

# se crearara con tkinter y python, y para ello debemos importar la libreria la libreia tkinter.

import tkinter as tk  # se indica a python que estamos importando esta libreria.
from tkinter import*

ventana = tk.Tk()
ventana.title("UbicuiLAB App")


ventana.geometry('600x700')  # tamaño de la ventana en pixeles ancho por alto
ventana.configure(background='lightsteelblue')


mensaje1 = tk.Label(ventana, text="Bienvenid@", bg='steelblue', fg='white')

mensaje1.pack()

# con image se puede introducir una imagen predeterminada y se llama con Photoimage de la libreria, el archivo debe estar en gif.

image = tk.PhotoImage(file="azuldescrip.gif")
image = image.subsample(2, 2)
label = tk.Label(image=image)
label.pack()

#Crear boton
boton = tk.Button(ventana,text="Ingresar")
boton.pack()

#boton
#CREACION DE VENTANA DE OPCIONES, con topleves se pueden crear las ventanas que se deseen, en este caso estamos creando la de las funciones basicas y avanzadas.

vopciones= Toplevel()
vopciones.title("UbicuiLAB App")
vopciones.geometry('370x400')
mensaje2 = Label(vopciones,text="Funciones Basicas y Avanzadas")
mensaje2.pack()

mensaje3 = tk.Label(vopciones, text="Inventario", bg='steelblue', fg='white')

mensaje3.pack()
mensaje4 = tk.Label(vopciones, text="conteo de colonias", bg='steelblue', fg='white')

mensaje4.pack()



ventana.mainloop()
