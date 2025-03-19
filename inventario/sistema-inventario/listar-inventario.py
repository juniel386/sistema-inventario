
with open('productos.txt', 'r') as file:
    
    productos = file.readlines()

print("Productos almacenados:")
for producto in productos:
    
    nombre, cantidad, precio = producto.strip().split(", ")
    print(f"Producto: {nombre}, Cantidad: {cantidad}, Precio: {precio}")
