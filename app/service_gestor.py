from peewee import *
from app.models.producto import Producto, db

class Gestor_de_Productos():
    def __init__(self):
        self.db = db
        self.db.connect()
        self.db.create_tables([Producto])

    def insertar_producto(self, nombre, descripcion, precio, categoria, existencias):
        producto = Producto.create(
            nombre= nombre,
            descripcion= descripcion,
            precio= float(precio),
            categoría= categoria,
            existencias= int(existencias)
        )
        return producto

    def __añadir_existencias(self, id, nuevas_existencias):
        producto = Producto.get_or_none(Producto.id == id)
        if producto:
                producto.existencias += int(nuevas_existencias)
                producto.save()
                return producto.nombre, producto.existencias
        else:
            raise ValueError(f"id {id} no encontrado dentro del inventario.")
    
    def __quitar_existencias(self, id, num_existencias):
        producto = Producto.get_or_none(Producto.id == id)
        if producto:
            if producto.existencias < int(num_existencias):
                raise ValueError (f"No hay suficientes existencias de {producto.nombre} para quitar.")
            elif producto.existencias >= num_existencias:
                producto.existencias -= int(num_existencias)
                producto.save()
                return producto.nombre, producto.existencias
        else:
                raise ValueError("id no encontrado dentro del inventario.")

    def __listar_productos(self):
        listado = []
        for prod in Producto.select():
            producto_dict = {
                "Nombre": prod.nombre,
                "id": prod.id,
                "Precio": prod.precio,
                "Categoría": prod.categoría,
                "Existencias": prod.existencias
            }
            listado.append(producto_dict)
        return listado
    
    def __listar_categoria(self, categoria):
        query = Producto.select().where(Producto._categoría == categoria)
        listado = []
        for prod in query:
            producto_dict = {
                "Nombre": prod.nombre,
                "id": prod.id,
                "Precio": prod.precio,
                "Categoría": prod.categoría,
                "Existencias": prod.existencias
            }
            listado.append(producto_dict)
        return listado

    def mostrar_listado(self):
        print(f"Los productos del inventario son:")
        for i in self.__listar_productos():
                print(f"\n {i}")

    def mostrar_categoria(self, categoria):
        print(f"Los productos de la categoría {categoria} son:")
        for i in self.__listar_categoria(categoria):
                print(f"\n {i}")

    def añadir_existencias(self, id, nuevas_existencias):
        print(f"Existencias totales del producto {self.__añadir_existencias(id, nuevas_existencias)}.")

    def restar_existencias(self, id, num_existencias):
        print(f"Existencias restantes del producto {self.__quitar_existencias(id, num_existencias)}.")

    def desconectar(self):
        if not self.db.is_closed():
            self.db.close()
            print("Conexión a la base de datos cerrada.")