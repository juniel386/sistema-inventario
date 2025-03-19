inventario = {
    'producto_01': {'nombre': 'Producto A', 'cantidad': 10},
    'producto_02': {'nombre': 'Producto B', 'cantidad': 5},
    'producto_03': {'nombre': 'Producto C', 'cantidad': 20},
}

def actualizar_cantidad(producto_id, nueva_cantidad):
    if producto_id in inventario:
        inventario[producto_id]['cantidad'] = nueva_cantidad
        print(f"Cantidad actualizada: {inventario[producto_id]['nombre']} ahora tiene {nueva_cantidad} unidades.")
    else:
        print("Producto no encontrado.")

actualizar_cantidad('producto_2', 8)