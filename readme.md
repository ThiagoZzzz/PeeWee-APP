# Propósito.
Este proyecto fue desarrollado en el contexto de Trabajo Final para la materia Programación Avanzada, en el cual debíamos investigar y llevar a una aplicación práctica una biblioteca de python, elegimos la biblioteca Peewee y creamos una pequeña aplicación para la gestión de inventarios para comercios. Esta aplicación proporciona operaciones básicas para el manejo de una base de datos la cual contendrá el inventario.

##  Uso de la app.
* El único modelo de datos definido es para los *productos*, pueden encontrar la forma en que se comporta y cómo se ingresan las filas en la base de datos en su archivo correspondiente.
* PeeWee solo trabaja con bases de datos relacionales, permite instanciar bases de datos SQLite, MySQL, MariaDB y Postgres. Dentro del modelo, la base de datos con la que se trabaja es SQLite, si quisiera usar una base de datos distinta puede acceder a la [documentación oficial](https://docs.peewee-orm.com/en/latest/peewee/database.html) para informarse como instanciar otro tipo de base de datos.
* Dentro de la carpeta *database* se creará el archivo *Inventario.db* dónde se almacenarán los datos ingresados.
* Los métodos para interactuar con la base de datos se encuentran en *service_gestor*. Lógicamente los métodos que deben usar los usuarios son aquellos declarados como públicos. <br>
En el archivo *example* puede encontrar una demostración del uso de la app.
* Es importante cerrar la conexión a la base de datos luego de haber realizado las operaciones necesarias para evitar errores o conexiones no deseadas.