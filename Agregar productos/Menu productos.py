import os
from productos import agregar_producto, editar_producto, eliminar_producto, buscar_producto

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    limpiar_pantalla()
    print("# ############################################## #")
    print("#                                                #")
    print("#       Bienvenidos al Sistema de Productos      #")
    print("#                                                #")
    print("# ############################################## #")
    print("# 1. Gestionar Productos                         #")
    print("# 2. Salir                                       #")
    print("# ############################################## #")
    opcion = input("# Seleccione una Opción: ")
    return opcion

def sub_menu_productos():
    limpiar_pantalla()
    print("# ############################################## #")
    print("#                                                #")
    print("#              Gestionar Productos               #")
    print("#                                                #")
    print("# ############################################## #")
    print("# 1. Agregar Producto                            #")
    print("# 2. Editar Producto                             #")
    print("# 3. Eliminar Producto                           #")
    print("# 4. Buscar Producto                             #")
    print("# 5. Volver                                      #")
    print("# ############################################## #")
    opcion = input("# Seleccione una Opción: ")
    return opcion

def ejecutar():
    limpiar_pantalla()
    while True:
        opcion = mostrar_menu_principal()
        if opcion == '1':
            while True:
                opcion_producto = sub_menu_productos()
                if opcion_producto == '1':
                    limpiar_pantalla()
                    print("# ############################################## #")
                    print("#              Agregar Producto                  #")
                    print("# ############################################## #")
                    nombre = input("# Nombre del Producto: ")
                    cantidad = input("# Cantidad: ")
                    precio = input("# Precio: ")
                    agregar_producto(nombre, cantidad, precio)
                elif opcion_producto == '2':
                    limpiar_pantalla()
                    print("# ############################################## #")
                    print("#              Editar Producto                   #")
                    print("# ############################################## #")
                    nombre_buscar = input("# Nombre del producto a editar: ")
                    nuevo_nombre = input("# Nuevo Nombre: ")
                    nueva_cantidad = input("# Nueva Cantidad: ")
                    nuevo_precio = input("# Nuevo Precio: ")
                    editar_producto(nombre_buscar, nuevo_nombre, nueva_cantidad, nuevo_precio)
                elif opcion_producto == '3':
                    limpiar_pantalla()
                    print("# ############################################## #")
                    print("#              Eliminar Producto                 #")
                    print("# ############################################## #")
                    nombre_buscar = input("# Nombre del producto a eliminar: ")
                    eliminar_producto(nombre_buscar)
                elif opcion_producto == '4':
                    limpiar_pantalla()
                    print("# ############################################## #")
                    print("#              Buscar Producto                   #")
                    print("# ############################################## #")
                    nombre_buscar = input("# Nombre del producto a buscar: ")
                    resultados = buscar_producto(nombre_buscar)
                    for resultado in resultados:
                        print(f"Nombre: {resultado[0]}, Cantidad: {resultado[1]}, Precio: {resultado[2]}")
                    input("Presione Enter para continuar...")
                elif opcion_producto == '5':
                    break
        elif opcion == '2':
            print("Gracias por usar el sistema de gestión de productos. ¡Hasta pronto!")
            break
