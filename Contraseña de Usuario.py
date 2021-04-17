listaclaves=["Viviam06","loVecit7","Vivitas6"]
clave = input("Ingrese la clave a usar:")
print(clave)

valida=0

while valida !=6:

  if len(clave)<6:
    print("La clave debe tener una longitud de 6 caracteres")
  else:
     valida=valida+1

 
  may = 0
  for i in clave:
    if i.isupper():
        #may+=1
        may = may + 1

  if may>0:
    print("Si hay mayusculas")
    valida=valida+1
  else:
    print("No hay mayusculas")

  min = 0
  for i in clave:
    if i.islower():
        #may+=1
        min = min + 1

  if min>0:
    print("Si hay minisculas")
    valida=valida+1
  else:
    print("No hay minisculas")

  num = 0
  for i in clave:
    if i.isnumeric():
        #num+=1
        num = num+1

  if num > 0:
    print("Si hay numeros")
    valida=valida+1
  else:
    print("No hay numeros")

#print(len(clave)-may-min-num)
  if (len(clave)-may-min-num)>0:
    print("Hay caracteres especiales")
  else:
    print("No hay caracteres especiales")
    valida=valida+1  
 
#--"Viviam06","loVecit7","Vivitas6"
  usada=0

  for h in listaclaves:
    if clave==h:
      print("La contraseña ya fue utilizada anteriormente")
      usada=usada+1
  if usada==0:
     #listaclaves=listaclaves+[clave] 
     #listaclaves.append(clave)
     valida=valida+1


  if valida!=6:
     print("Clave invalida")
     clave = input("Ingrese la clave a usar:")
     print(clave)
     valida=0
if valida==6:
    #listaclaves=listaclaves+[clave] 
    listaclaves.append(clave)
     

print(listaclaves)

