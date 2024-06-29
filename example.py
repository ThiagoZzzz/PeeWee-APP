from app.service_gestor import Gestor_de_Productos
Gestor = Gestor_de_Productos()

Gestor.agregar_producto("Producto 1", "Descripción del producto 1", 10.99, "Categoría A", 5)
Gestor.agregar_producto("Producto 2", "Descripción del producto 2", 12, "Categoría B", 80)
Gestor.agregar_producto("Producto 3", "Descripción del producto 3", 3.80, "Categoría B", 140)
Gestor.agregar_producto("Producto 4", "Descripción del producto 4", 100, "Categoría C", 4)
Gestor.agregar_producto("Producto 5", "Descripción del producto 5", 28.50, "Categoría A", 36)
Gestor.agregar_producto("Producto 6", "Descripción del producto 6", 6, "Categoría B", 45)

Gestor.mostrar_listado()

Gestor.añadir_existencias(1, 20)

Gestor.restar_existencias(3, 40)

Gestor.cambiar_precio(6, 7.55)

Gestor.eliminar_producto(3)

Gestor.mostrar_categoria("Categoría B")

Gestor.desconectar()