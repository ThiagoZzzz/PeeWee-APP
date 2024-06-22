from peewee import *
import os

database_folder = "database"
if not os.path.exists(database_folder):
    os.makedirs(database_folder)

db_path = os.path.join(database_folder, "Inventario.db")

db = SqliteDatabase(db_path)

class Producto (Model): 
    id = AutoField()
    _nombre = CharField(max_length=50)
    _descripcion = TextField()
    _precio = FloatField()
    _categoría = CharField(max_length=50)
    _existencias = IntegerField()

    class Meta:
        database = db

    @property
    def id(self):
        return self.id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = value

    @property
    def categoría(self):
        return self._categoría

    @categoría.setter
    def categoría(self, value):
        self._categoría = value

    @property
    def existencias(self):
        return self._existencias

    @existencias.setter
    def existencias(self, value):
        if value < 0:
            raise ValueError("Las existencias no pueden ser negativas.")
        self._existencias = value