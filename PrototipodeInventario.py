#Creacion de inventario para ser utilizado en un laboratorio de Biociencias
ListaInstrumento=[]
ListaKardex=[]
VectorInstrumento=[]
Vector=[]
 
#Verificacion del  vector, si se encuentra vacío o lleno
def Buscar(Codigo):
    Posicion=len(ListaInstrumento)
    return Posicion

#Buscamos el nombre del Instrumento a consultar
def BuscarNombre(Codigo):
    Posicion=len(ListaInstrumento)
    if Posicion==0:
        Nombre=''
    else:
        for VectorInstrumento in ListaInstrumento:
            if VectorInstrumento[0]==Codigo:
                Nombre=VectorInstrumento[1]
            else:
                Nombre=''
    return Nombre
#Extraemos todos los datos del Instrumento a buscar
def BuscarInstrumento(Codigo):
    VINSTRUMENTO=[]
    for VectorInstrumento in ListaInstrumento:
        if VectorInstrumento[0]==Codigo:
            VINSTRUMENTO.append(VectorInstrumento[0])
            VINSTRUMENTO.append(VectorInstrumento[1])
            VINSTRUMENTO.append(VectorInstrumento[2])
            VINSTRUMENTO.append(VectorInstrumento[3])
            return VINSTRUMENTO

    #Mostramos los datos del Insrumento buscado
def BuscarInstrumento2(Codigo):
    VINSTRUMENTO=[]
    for VINSTRUMENTO in ListaInstrumento:
        if VINSTRUMENTO[0]==Codigo:
            print("Codigo: ",VINSTRUMENTO[0])
            print("Nombre: ",VINSTRUMENTO[1])
            print("Saldo Disponible: ",VINSTRUMENTO[2])
            print("Total: ",VINSTRUMENTO[2])
          

            #Actualizamos de la cantidad del Instrumento de acuerdo al movimiento (Ingreso/Egreso)
def ActualizarSaldo(Codigo,TipoMovimiento,Cantidad,Total):
    VINSTRUMENTO=[]
    for VectorInstrumento in ListaInstrumento:
        if VectorInstrumento[0]==Codigo:
            ListaInstrumento.remove(VectorInstrumento)
            CantidadT=float(VectorInstrumento[2])
            TotalT=float(VectorInstrumento[3])
            if TipoMovimiento=='IngresoInstrumento':
                CantidadT=CantidadT+float(Cantidad)
                TotalT=TotalT+float(Total)
                print('IngresoInstrumento',CantidadT)
                print('IngresoInstrumento',TotalT)
            else:
                CantidadT=CantidadT-float(Cantidad)
                TotalT=TotalT-float(Total)
                print('EgresoInstrumento',CantidadT)
                print('EgresoInstrumento',TotalT)
            if CantidadT==0:
                Costo=0
            else:
                Costo=TotalT/CantidadT
            VINSTRUMENTO.append(VectorInstrumento[0])
            VINSTRUMENTO.append(VectorInstrumento[1])
            VINSTRUMENTO.append(CantidadT)
            VINSTRUMENTO.append(Costo)
            VINSTRUMENTO.append(TotalT)
            ListaInstrumento.append(VINSTRUMENTO)
            #Realizamos el Ingreso del Instrumento
def Ingreso():
    VKARDEX=[]
    print('')
    print('       INGRESO DE INSTRUMENTO       ')
    Codigo=input("Ingrese el Código del Instrumento: ")
    Nombre=BuscarNombre(Codigo)
    if Nombre=='':
        Nombre=input("Ingrese la Descripción del Instrumento: ")
    else:
        Nombre=BuscarNombre(Codigo)
        print("Nombre del Instrumento: ",Nombre)
    Cantidad=input("Ingrese la Cantidad del Instrumento: ")
    Total=float(Cantidad)
    if Buscar(Codigo)==0:
        VectorInstrumento.append(Codigo)
        VectorInstrumento.append(Nombre)
        VectorInstrumento.append(Cantidad)
        VectorInstrumento.append(Total)
        ListaInstrumento.append(VectorInstrumento)
    else:
        ActualizarSaldo(Codigo,'IngresoInstrumento',Cantidad,Total)
    VKARDEX.append("IngresoInstrumento")
    VKARDEX.append(Codigo)
    VKARDEX.append(Nombre)
    VKARDEX.append(Cantidad)
    VKARDEX.append(Total)
    ListaKardex.append(VKARDEX)
    print('')
 #Realizamos el Egreso de Instrumento (baja)
def Egreso():
    VKARDEX=[]
    print('')
    print('        EGRESO DEL INSTRUMENTO       ')
    Codigo=input("Ingrese el Código del Instrumento: ")
    Vector=BuscarInstrumento(Codigo)

    if len(Vector)>0:
        print("Nombre del Instrumento: ",Vector[1])
        Cantidad=float(input("Ingrese la Cantidad a Egresar: "))
        Total=Cantidad
        VKARDEX.append("EgresoInstrumento")
        VKARDEX.append(Codigo)
        VKARDEX.append(Vector[1])
        VKARDEX.append(Cantidad)
        VKARDEX.append(Total)
        ActualizarSaldo(Codigo,'EgresoInstrumento',Cantidad,Total)
        ListaKardex.append(VKARDEX)
        print('')
    else:
        print("Instrumento No Existe!!")
        #Mostramos el Kardex de un Instrumento
def Kardex():
    VKARDEX=[]
    VINSTRUMENTO=[]
    print('')
    print('       KARDEX DEL INSTRUMENTO       ')
    print('')
    Codigo=input("Ingrese el Código del Instrumento: ")
    print('')
    print('CODIGO','NOMBRE','TIPO MOVIMIENTO','CANTIDAD',sep="\t")
    if BuscarNombre(Codigo)=='':
        print("Código No Existente")
    else:
        for VKARDEX in ListaKardex:
            if VKARDEX[1]==Codigo:
                print(VKARDEX[1],VKARDEX[2],VKARDEX[0],VKARDEX[3],sep="\t")
    print('')
 # Menú Principal
while True:
    print('SISTEMA DE INVENTARIO')
    print('')
    print('        Menú Principal       ')
    print('0. SALIR')
    print('1. INGRESO DE INSTRUMENTO')
    print('2. EGRESO DE INTRUMENTO')
    print('3. KARDEX')
    print('4. BUSQUEDA DE INSTRUMENTO')
    opcion=input('Digitar una Opción: ')
    if opcion=='0':
        break
    elif opcion=='1':
        Ingreso()
    elif opcion=='2':
        Egreso()
    elif opcion=='3':
        Kardex()
    elif opcion=='4':
        
        print('')

        print('        BUSQUEDA DE INSTRUMENTO       ')
        Codigo=input("Ingrese el Código del Instrumento: ")
        BuscarInstrumento2(Codigo)
    else:
        print('Opción no válida')


