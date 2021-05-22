# Formulario de registro de Usuario usando Python y Tkinter

# Vamos a importar tkinter desde  tkinter  import  *
#importar tkinter como tk
from tkinter import *
# creacion de sen_data para recuperar los datos que se guardan en las variables y paa que el boton de enviar informacion funcione
def send_data():
    nombredeusuario_data =nombredeusuario.get()
    contraseña_data =str(contraseña.get())
    nombrecompleto_data =nombrecompleto.get()
    edad_data =str(edad.get())
    correoelectronico_data =correoelectronico.get()

#se emplea get que nos permite obtener el texto que contenga este campo, no lo de vuelve.

    print(nombredeusuario_data, "\t",contraseña_data,"\t", nombrecompleto_data, "\t",edad_data,"\t", correoelectronico_data ) # se utilizo ("\t") para tabular y dar espacios en el formato de datos

#Creacion de un archivo de texto donde se guarda la informacion que agrega el usuario, se utiliza la txt que indica que sera de texto, y con open para crearlo.

    nuevoarchivo = open ("REGISTRO.txt", "a")# a:append(nos permite agregar la informacion al final de lo que ya existe en el archivo)
    nuevoarchivo.write(nombredeusuario_data)
    nuevoarchivo.write("\t")
    nuevoarchivo.write (contraseña_data)
    nuevoarchivo.write("\t")
    nuevoarchivo.write(nombrecompleto_data)
    nuevoarchivo.write("\t")
    nuevoarchivo.write(edad_data)
    nuevoarchivo.write("\t")
    nuevoarchivo.write(correoelectronico_data)
    nuevoarchivo.write("\n")
    # ("\n") nos permitira espaciar el texto para que se vea mas estetico.
    nuevoarchivo.close()
    print(" Nuevo Usuario Registrado. Nombre de Usuario: {} | Nombre Completo: {} ".format(nombredeusuario_data,  nombrecompleto_data))
    # se imprime por consola para verificar como se esta guardando en el registro de texto.
# Creacion de ingreso de datos del usuario, despues de entrar los datos con entry y enviarlos.Nos aseguaramos que las casillas se limpien con delete (0,END)
    nombredeusuario_entry.delete(0,END)
    contraseña_entry.delete(0,END)   
    nombrecompleto_entry.delete(0,END)
    edad_entry.delete(0,END)
    correoelectronico_entry.delete(0,END)
    # delete limpiara los index y (0,END) permitira que el recorrido de borrado sea desde cero hasta el final en ese campo. se puede verificar ingresando al registro y vemos quqe se agrago bien.

# Creacion y diseño de la ventana principal.
miventana=Tk() # TK SE LLAMA LA LIBRERIA  QUE UTLIZAMOS
miventana.geometry("650x550")# geometry se utliza para el tamaño o dimension de la ventana.
miventana.title("Registro de Usuario")
miventana.resizable(False,False)#resizable para ampliar el boton de la ventana
miventana.config(background="lightsteelblue")# config el color de fondo de nuestra ventana.
titulo_principal = Label(text="Registro de Usuario | UbicuiLAB", font=("Arial" ,15), bg="steelblue", fg="white", width="550", height="2")
titulo_principal.pack() # pack sirve para que el titulo se posicione en la parte superior.
# se utiliza Label para que nos servira para definir el campo de texto de cada uno de nuestros variables de nuestro formulario.

nombredeusuario_label= Label(text="Nombre de Usuario", bg="lightsteelblue")
nombredeusuario_label.place(x=270, y=70)
contraseña_label= Label(text="Contraseña", bg="lightsteelblue")
contraseña_label.place(x=298, y=140)
nombrecompleto_label= Label(text="Nombre Completo", bg="lightsteelblue")
nombrecompleto_label.place(x=276, y=220)
edad_label= Label(text="Edad",bg="lightsteelblue")
edad_label.place(x=312, y=300)
Correoelectronico_label= Label(text="Correo Electronico", bg="lightsteelblue")
Correoelectronico_label.place(x=274, y=380)
# place se utiliza para posicionar ese texto dentro de nuestra ventana.

#Creacion de variables del Registro de Usuario
#DECLARAMOS "stringVar" como tipo de dato para lo siguiente. esta provine de LA LIBRERIA TK. 

nombredeusuario = StringVar()
contraseña = StringVar()
nombrecompleto= StringVar()
edad = StringVar()
correoelectronico = StringVar()

#Es importante crear las variables StringVar y en el campo de entrada de datos entry, estamos utilizando la sentencia textvariable, para asociar la entrada de datos se hace para cada uno de las variables creadas anteriormente.

nombredeusuario_entry = Entry(textvariable=nombredeusuario, width="40")
contraseña_entry = Entry(textvariable=contraseña, width="40", show="*")  
nombrecompleto_entry = Entry(textvariable=nombrecompleto, width="40") 
edad_entry = Entry(textvariable=edad, width="40") 
correoelectronico_entry = Entry(textvariable=correoelectronico, width="40") 
#Se utiliza en campo de entrada de datos de contraseña,la sentencia show* para que no se vea lo que se escriba en ese campo.
 
 # Se continua posicionando con place ese texto dentro de nuestra ventana.

nombredeusuario_entry.place(x=160, y=108)
contraseña_entry.place(x=160, y=182)   
nombrecompleto_entry.place(x=160, y=260)
edad_entry.place(x=160, y=340)
correoelectronico_entry.place(x=160, y=420) 
# se crea un boton para que los datos que introduzca el usuario sean capturados, al hacer click en ese boton.

enviarinformacion_btn = Button(miventana, text= "Enviar Información", command= send_data, width= "30", height= "2", bg= "lightgrey")
# se utiliza la sentencia command para que indique donde queremos dirigirnos cuando hacemos click en el botón.
enviarinformacion_btn.place(x=190, y=470)

miventana.mainloop() #mainloop es el método que indica que la ventana esta lista para ejecutarse.



