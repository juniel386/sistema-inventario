import os

# Funciones simuladas para gestionar productos
def agregar_producto(nombre, cantidad):
    print(f"Producto '{nombre}' agregado con cantidad {cantidad}.")

def editar_producto(nombre, nueva_cantidad):
    print(f"Cantidad del producto '{nombre}' actualizada a {nueva_cantidad}.")

def eliminar_producto(nombre):
    print(f"Producto '{nombre}' eliminado.")

def buscar_producto(nombre):
    # Simulamos que encontramos un producto
    return [(nombre, 10)]  # Retorna una lista con el nombre y cantidad

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    limpiar_pantalla()
    print("# ############################################## #")
    print("#                                                #")
    print("#          Bienvenidos a la Gestión de          #")
    print("#                Productos                       #")
    print("#                                                #")
    print("# ############################################## #")
    print("# 1. Gestionar Productos                         #")
    print("# 2. Salir                                       #")
    print("# ############################################## #")
    opcion = input("# Seleccione una Opcion:")
    return opcion

def sub_menu_productos():
    limpiar_pantalla()
    print("# ############################################## #")
    print("#                                                #")
    print("#               Gestionar Productos              #")
    print("#                                                #")
    print("# ############################################## #")
    print("# 1. Agregar Producto                            #")
    print("# 2. Editar Producto                             #")
    print("# 3. Eliminar Producto                           #")
    print("# 4. Buscar Producto                             #")
    print("# 5. Volver                                      # ")
    print("# ############################################## #")
    opcion = input("# Seleccione una Opcion:")
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
                    print("#               Agregar Producto                 #")
                    print("# ############################################## #")
                    nombre = input("# Nombre del Producto:")
                    cantidad = input("# Cantidad:")
                    agregar_producto(nombre, cantidad)
                elif opcion_producto == '2':
                    limpiar_pantalla()
                    print("# ############################################## #")
                    print("#               Editar Producto                  #")
                    print("# ############################################## #")
                    nombre_buscar = input("# Nombre del producto a editar:")
                    nueva_cantidad = input("# Nueva Cantidad:")
                    editar_producto(nombre_buscar, nueva_cantidad)
                elif opcion_producto == '3':
                    limpiar_pantalla()
                    print("# ############################################## #")
                    print("#               Eliminar Producto                #")
                    print("# ############################################## #")
                    nombre_buscar = input("# Nombre del producto a eliminar:")
                    eliminar_producto(nombre_buscar)
                elif opcion_producto == '4':
                    limpiar_pantalla()
                    print("# ############################################## #")
                    print("#                Buscar Producto                 #")
                    print("# ############################################## #")
                    nombre_buscar = input("# Nombre del producto a buscar:")
                    resultados = buscar_producto(nombre_buscar)
                    for resultado in resultados:
                        print(f"Nombre: {resultado[0]}, Cantidad: {resultado[1]}")
                    input("Presione Enter para continuar...")
                elif opcion_producto == '5':
                    break
        elif opcion == '2':
            print("Gracias por usar el sistema de gestión de productos. Hasta luego...")
            break

# Ejecutar el programa
ejecutar()