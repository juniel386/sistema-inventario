import os

ARCHIVO_INVENTARIO = "inventario.txt"


def eliminar_producto(nombre_producto):
    """
    Elimina un producto del inventario si existe.
    :param nombre_producto: Nombre del producto a eliminar.
    """
    if not os.path.exists(ARCHIVO_INVENTARIO):
        print("❌ No hay productos en el inventario.")
        return

    productos = []
    eliminado = False

    # Leer el archivo y guardar los productos en una lista
    with open(ARCHIVO_INVENTARIO, "r") as f:
        for linea in f:
            datos = linea.strip().split(", ")
            if len(datos) == 3:  # Verificar formato correcto
                nombre, cantidad, precio = datos
                if nombre.lower() != nombre_producto.lower():
                    productos.append(linea.strip())
                else:
                    eliminado = True

    # Si no se encontró el producto, mostrar mensaje
    if not eliminado:
        print(
            f"❌ Producto '{nombre_producto}' no encontrado en el inventario.")
        return

    # Sobrescribir el archivo sin el producto eliminado
    with open(ARCHIVO_INVENTARIO, "w") as f:
        for producto in productos:
            f.write(producto + "\n")

    print(f"✅ Producto '{nombre_producto}' eliminado correctamente.")


# Ejemplo de uso
if __name__ == "__main__":
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    eliminar_producto(nombre)
