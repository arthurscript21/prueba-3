import csv

comunas=("santiago","colina","pirque")
pedidos=[]
def agregar_pedido():
    total=0
    galon5=0
    galon15=0
    rut=ingresar_rut()
    nombre=ingresar_nombre()
    direccion=ingresar_direccion()
    comuna=ingresar_comuna()
    while True:
        cilindro= ingreasar_cilindro()
        if cilindro == 1:
            galon5 = int(input("cuantos cilindros de 5 va a llevar?: "))
            total1= 12500*galon5
        elif cilindro == 2:
            galon15 =int(input("cuantos cilindros de 15 va a llevar?: "))
            total2=25500*galon15
        elif cilindro== 3:
            print("gracias por comprar")
            break

    total1= 12500*galon5
    total2=25500*galon15
    total=total1+total2
    pedido = [rut, nombre,direccion,comunas[comuna-1],galon5,galon15,total]
    pedidos.append(pedido)
    

def ver_pedido():
    if len(pedidos) == 0:
        print("no hay ningun pedido registrado")
    else:
        for lulo in pedidos:
            print(f"rut: {lulo[0]} - nombre: {lulo[1]} - direccion: {lulo[2]} - comuna: {lulo[3]} - cilindro de 5: {lulo[4]} - cilindro de 15: {lulo[5]} - total: {lulo[6]}")


def buscar_rut():
    if len(pedidos)==0:
        print("no hay ningun pedido registrado")
    else:
        print("\nbuscar por rut")
        buscar=int(input("ingrese rut a buscar:"))
        if buscar == pedidos:
            for buscar in pedidos:
                print(f"rut: {buscar[0]} - nombre: {buscar[1]} - direccion: {buscar[2]} - comuna: {buscar[3]} - cilindro de 5: {buscar[4]} - cilindro de 15: {buscar[5]} - total: {buscar[6]}")


       

def imprimir_csv():
    csv_comun=int(input("ingrese comuna que desea archivar 1.santiago 2.colina 3.pirque"))
    try:
        with open(comunas[csv_comun-1] + ".csv", "x" )as file:
            escritor= csv.writer(file)
            escritor.writerow(comunas[csv_comun-1])
    except:
        print("error,este archivo ya fue creado")

       








#funciones
def ingresar_rut():
    while True:
        try:
            rut=int(input("ingrese su rut: "))
            if len(str(rut))==9:
                return rut
            else:
                print("el rut no debe tener ni espacio, ni guion o punto")
        except:
            print("porfavor solo numeros enteros")

def ingresar_nombre():
    while True:
        nombre=input("ingrese su nombre: ")
        if len(nombre) >3 and nombre.isalpha:
            return nombre
        else:
            print("el nombre debe tener almnos 3 letras")


def ingresar_direccion():
    while True:
        direccion=input("ingrese su direccion: ")
        if len(direccion)>3 and direccion.isalpha:
            return direccion
        else:
            print("la direccion debe tener 3 letras minimo")

def ingresar_comuna():
    while True:
        try:
            comuna=int(input("ingrese su comuna 1.santiago 2.colina 3.pirque"))
            if comuna in(1,2,3):
                return comuna
            else:
                print("error, seleccione solo 1,2 o 3")
        except:
            print("ingrese solo numeros enteros")
def ingreasar_cilindro():
    while True:
        cilindro= int(input("ingrese una opcion 1.cilindro de 5, 2.cilindro de 15 y 3.salir"))
        if cilindro in(1,2,3):
            return cilindro
