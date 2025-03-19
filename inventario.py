import os

ARCHIVO_INVENTARIO = "inventario.txt"

def leer_inventario():
    """Lee el archivo de inventario y devuelve una lista de productos"""
    productos = []
    if not os.path.exists(ARCHIVO_INVENTARIO):
        return productos
    with open(ARCHIVO_INVENTARIO, "r") as f:
        for linea in f:
            datos = linea.strip().split(", ")
            if len(datos) == 3:  # Verificar formato correcto
                nombre, cantidad, precio = datos
                productos.append({"nombre": nombre, "cantidad": int(cantidad), "precio": float(precio)})
    return productos

def guardar_inventario(productos):
    """Guarda la lista de productos en el archivo inventario.txt"""
    with open(ARCHIVO_INVENTARIO, "w") as f:
        for producto in productos:
            f.write(f"{producto['nombre']}, {producto['cantidad']}, {producto['precio']}\n")

def eliminar_producto(nombre_producto):
    """
    Elimina un producto del inventario si existe.
    :param nombre_producto: Nombre del producto a eliminar.
    """
    productos = leer_inventario()
    productos_actualizados = [producto for producto in productos if producto["nombre"].lower() != nombre_producto.lower()]
    
    if len(productos) == len(productos_actualizados):
        print(f"❌ Producto '{nombre_producto}' no encontrado en el inventario.")
        return
    
    guardar_inventario(productos_actualizados)
    print(f"✅ Producto '{nombre_producto}' eliminado correctamente.")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\nOpciones del Inventario:")
    print("1. Ver inventario")
    print("2. Eliminar producto")
    print("3. Salir")

def listar_inventario():
    """Lista todos los productos en el inventario"""
    productos = leer_inventario()
    if productos:
        print("\nInventario actual:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
    else:
        print("El inventario está vacío.")

def gestionar_inventario():
    """Función principal para gestionar el inventario"""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            listar_inventario()
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == '3':
            print("Gracias por usar el sistema de inventario.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutar el sistema
if __name__ == "__main__":
    gestionar_inventario()
