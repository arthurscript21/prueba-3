from funciones_prueba import *
import os, time
while True:
    os.system("cls")
    print("\nGAxplosive")
    print("1.registrar pedido")
    print("2.Lista Pedidos")
    print("3.Buscar pedido (rut)")
    print("4.imprimir csv")
    print("5.salir")
    print("")
    opc=int(input("ingrese una opcion: "))
    os.system("cls")
    if opc ==1:
        agregar_pedido()
    elif opc ==2:
        ver_pedido()
    elif opc ==3:
        buscar_rut()
    elif opc ==4:
        imprimir_csv()
    elif opc ==5:
        print("gracias, adios")
        break
    time.sleep(5)
