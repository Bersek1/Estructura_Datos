class Producto:
    def __init__(self, nombre):
        self.nombre = nombre


class Almacen:
    def __init__(self):
        self.productos_recibidos = []
        self.productos_despachar = []

    def agregar_producto(self, nombre):
        nuevo_producto = Producto(nombre)
        self.productos_recibidos.append(nuevo_producto)
        print(f"Se agregó el producto '{nombre}")

    def despachar_producto(self):
        if self.productos_despachar:
            producto_despachado = self.productos_despachar.pop(0)
            print(f"Se despacho el producto {producto_despachado.nombre}")
        else:
            print("No hay productos disponibles para despachar.")

    def pila_vacia(self):
        return len(self.productos_recibidos) == 0

    def cola_vacia(self):
        return len(self.productos_despachar) == 0

    def productos_recibidos(self):
        if self.pila_vacia():
            print("No hay productos recibidos.")
        else:
            print("Productos recibidos en el almacen:")
            for producto in self.productos_recibidos:
                print(producto.nombre)

    def productos_despachados(self):
        if self.cola_vacia():
            print("No hay productos para despachar.")
        else:
            print("Productos para despachar:")
            for producto in self.productos_despachar:
                print(producto.nombre)

    def cantidad_total_productos(self):
        cantidad_total = len(self.productos_recibidos) + len(self.productos_despachar)
        print(f"Cantidad total de productos: {cantidad_total}")


almacen = Almacen()

almacen.agregar_producto("Pan")
almacen.agregar_producto("Mantequilla")
almacen.agregar_producto("Azucar")

almacen.productos_recibidos()

almacen.despachar_producto()

almacen.productos_despachados()

almacen.cantidad_total_productos()