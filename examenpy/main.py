from inventario import menu
from inventario import agregar_producto
from inventario import *
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

1
def main():
    
    while True:
        clear()
        menu()
        opcion=input('Eliga una opción: ')

        if not opcion.isdigit():
            print('')
            print('Por favor, ingrese lo pedido, Gracias!!')
            input('Presione enter para continuar...')
            continue

        opcion=int(opcion)
        
        if opcion > 5:
            print('')
            print('Por favor, ingrese lo pedido, Gracias!!')
            input('Presione enter para continuar...')
            continue

        match opcion:
            case 1: 
                clear()
                print('......Agregar producto......')
                agregar_producto()
            case 2:
                clear()
                print('...Actualizar Cantidad de Productos...')
                actualizar()
            case 3: 
                clear()
                print('...Mostrar Inventario...')
                mostrar()
            case 4:
                clear()
                print('...Buscar Producto...')
                buscar()     
            case 5:
                print('')
                print("¡Nos vemos pronto, Byebye 😊!")
                input('Presione enter para continuar...')
                exit()                       
main()      


    
