class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


productos = {
    "A001": Producto("Lapiz", 8.50),
    "A002": Producto("Cuaderno", 35.00),
    "A003": Producto("Pluma", 12.00)
}

codigo = input("Codigo a buscar: ")

if codigo in productos:
    producto = productos[codigo]

    print("Producto:", producto.nombre)
    print("Precio: $", producto.precio)

else:
    print("Codigo no encontrado")
