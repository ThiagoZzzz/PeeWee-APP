from peewee import *
from app.models.producto import Producto, db

class Gestor_de_Productos():
    def __init__(self):
        self.db = db
        self.db.connect()
        self.db.create_tables([Producto])

    def __insertar_producto(self, nombre, descripcion, precio, categoria, existencias):
        producto = Producto.create(
            nombre= nombre,
            descripcion= descripcion,
            precio= float(precio),
            categoría= categoria,
            existencias= int(existencias)
        )
        return producto

    def __remover_producto (self, id):
        producto = Producto.get_or_none(Producto.id == id)
        if producto:
            producto.delete_instance()
        else:
            raise ValueError(f"id {id} no encontrado dentro del inventario.")
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

    def __set_precio(self, id, nuevo_precio):
        producto = Producto.get_or_none(Producto.id == id)
        if producto:
                producto.precio = nuevo_precio
                producto.save()
                return producto.nombre, producto.precio
        else:
            raise ValueError(f"id {id} no encontrado dentro del inventario.")

    def agregar_producto(self, nombre, descripcion, precio, categoria, existencias):
        print(f"\nEl producto: {self.__insertar_producto(nombre, descripcion, precio, categoria, existencias).nombre}, fue agregado al inventario.")

    def eliminar_producto(self, id):
        print(f"\nEl producto: {self.__remover_producto(id).nombre}, fue eliminado del inventario.")

    def mostrar_listado(self):
        print(f"Los productos del inventario son:")
        for i in self.__listar_productos():
                print(f"{i} \n")

    def mostrar_categoria(self, categoria):
        print(f"Los productos de la categoría {categoria} son:")
        for i in self.__listar_categoria(categoria):
                print(f"{i} \n")

    def añadir_existencias(self, id, nuevas_existencias):
        print(f"\nExistencias totales del producto {self.__añadir_existencias(id, nuevas_existencias)}.")

    def restar_existencias(self, id, num_existencias):
        print(f"\nExistencias restantes del producto {self.__quitar_existencias(id, num_existencias)}.")

    def cambiar_precio(self, id, nuevo_precio):
        print(f"\nEl precio del producto se ha actualizado: {self.__set_precio(id, nuevo_precio)}.")

    def desconectar(self):
        if not self.db.is_closed():
            self.db.close()
            print("Conexión a la base de datos cerrada.")