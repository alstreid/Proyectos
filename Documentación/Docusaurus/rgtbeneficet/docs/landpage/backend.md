# Backend del Sitio Web

El backend de este sitio web fue desarrollado utilizando el lenguaje de programación **Python** junto con varias librerías y el microframework **Flask** para establecer la estructura y las rutas. Se implementaron métodos **GET**, **POST**, **PUT** y **DELETE** para gestionar la interacción con la API.

### Base de Datos

Para almacenar y manipular todos los datos ingresados, se utilizó **MongoDB** como base de datos. Esto permite guardar los registros de los clientes, los beneficios otorgados y otros datos relacionados, y también posibilita realizar consultas y obtener respuestas de manera eficiente.

### Funcionalidad Principal

La API se centra en recibir datos de los clientes mediante formularios y registrarlos en la base de datos. Durante este proceso, se otorga un "beneficio" que solo puede ser canjeado una vez por el cliente. Esto permite administrar promociones o beneficios únicos.

### Seguridad y Autenticación

Para asegurar la protección de las rutas, se utilizó el mecanismo de **token** de seguridad con **JWT (JSON Web Tokens)**. Esto garantiza que solo los usuarios autorizados puedan acceder a las rutas protegidas.

### Pruebas y Validaciones

Todas las rutas y funcionalidades del backend se sometieron a pruebas exhaustivas utilizando **Postman**. Esto asegura que las rutas estén correctamente estructuradas y que las funcionalidades se comporten según lo esperado.

### Pruebas de Estrés y Calidad

Para garantizar el rendimiento y la calidad del backend, se realizaron pruebas de estrés y calidad utilizando la herramienta **JMeter**. Los resultados de estas pruebas se documentaron y se tomaron en cuenta para mejorar el rendimiento del sistema.

### Integración con Docker

El backend se integró en un **Dockerfile**, lo que permite mantener el backend dockerizado. Esto facilita la portabilidad y la capacidad de ejecutar y manipular el backend desde cualquier computadora con Docker instalado.

