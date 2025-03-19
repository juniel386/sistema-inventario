productos = []

while True:
    print("Menú de opciones:")
    print("1- Agregar Productos")
    print("2- Mostrar Inventario")
    print("3- Salir")
    
    opcion =input("Elije una opción: ")
    
    if opcion == "1":
        nombre =input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))

        

        producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        productos.append(producto)
        print("Producto agregado con éxito.")
    
    elif opcion == "2":
        if not productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario Actual:")
            for producto in productos:
                print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")
    
    elif opcion == "3":
        print("¡Hasta luego!")
        break  
    
    else:
        print("Opción no válida, por favor intente nuevamente.")