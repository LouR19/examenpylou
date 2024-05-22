inventario={}

def menu():
    print("...Sistema de Gestión...\n 1- Agregar un producto. \n 2- Actualizar cantidad de un producto. \n 3- Mostrar inventario. \n 4- Buscar un producto. \n 5- Salir.")
    return

def agregar_producto():
            nprod=input('Ingrese el nombre del producto: ')
            cantp=input('Ingrese la cantidad de productos: ')
            precio=input('Ingrese el precio del producto: ')
            codigo=input('Ingrese el codigo del producto: ')
            
            inventario[nprod] = {
                'Codigo' : codigo,
                'Nombre' : nprod,
                'Cantidad' : cantp,
                'Precio' : precio
            } 
            input('Presione enter para continuar...')
    
def buscar():
    while True:
        nprod = input("Ingrese el nombre del producto que desee buscar: ")
        producto = inventario.get(nprod)
        
        if nprod.isdigit():
            print('Invalido, intente nuevamente. ')
            input('Presione enter para continuar...')
            continue
        elif not producto:
            print(f'No se encontró el producto: {nprod}')
            input('')
            break
        else:
            print(f'ID: {producto["Codigo"]} - Nombre: {producto["Nombre"]} - Cantidad: {producto["Cantidad"]} - Precio: {producto["Precio"]} - Encontrado exitosamente!!')
            #print(producto)
            input('Presione enter para continuar...')
            break

def actualizar():
    nprod = input('Ingrese el nombre del producto: ')
    producto = inventario.get(nprod)
    
    if not producto:
        print('No se encontró el producto.')
    else:
        ncantp = int(input('Ingrese la cantidad de productos: '))
        inventario[nprod]['Cantidad'] = ncantp
        input('Presione enter para continuar...')

def mostrar():
    for keys, values in inventario.items():
        print(f"ID: {values['Codigo']} - Nombre: {keys} - Cantidad: {values['Cantidad']} - Precio: {values['Precio']}")
    input('Presione enter para continuar...')

        
    
    
    

    
    



    
