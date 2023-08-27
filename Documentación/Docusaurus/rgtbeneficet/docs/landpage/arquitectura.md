# Arquitectura de Proyecto de Software

### Componentes Principales:

1. **Front-End (React):**
   - El front-end estará construido utilizando React y el diseño fue creado en Figma.
   - Los usuarios interactúan con la interfaz de usuario, que ofrece funcionalidades para la lista de clientes, consulta de clientes y registro/actualización de clientes.

2. **Back-End (Python y Flask):**
   - Flask maneja las solicitudes HTTP y proporciona una API REST para las operaciones de gestión de clientes.
   - Se implementa un sistema de autenticación basado en JWT.
   - Las operaciones en la base de datos se gestionan a través del back-end.

3. **Base de Datos (MongoDB):**
   - Se almacenan los detalles de los clientes, incluida la información de aceptación de promociones.
   - Se tiene una colección que contiene los registros de los clientes.

4. **Docker:**
   - Se utilizan contenedores Docker para empaquetar y desplegar la aplicación y sus componentes.

5. **Pruebas de Estrés (JMeter):**
   - JMeter se utiliza para pruebas de estrés en las operaciones del back-end.

### Flujo de Datos y Funcionalidades:

1. **Lista de Clientes:**
   - El front-end consume la API para obtener la lista de clientes desde el back-end.
   - Los datos se recuperan de la base de datos MongoDB y se presentan en la interfaz de usuario.

2. **Consulta de Clientes:**
   - Los usuarios pueden buscar y consultar información de clientes.
   - El front-end envía una solicitud de búsqueda al back-end a través de la API, que recupera los datos de la base de datos y los devuelve al front-end.

3. **Registro/Actualización de Clientes:**
   - Los usuarios pueden registrar nuevos clientes o actualizar los datos existentes utilizando un formulario en el front-end.
   - El front-end consume la API para enviar los datos al back-end.
   - El back-end valida y procesa la solicitud, actualiza los datos en la base de datos MongoDB y devuelve una respuesta al front-end.

4. **Aceptación de Promociones:**
   - El formulario de registro incluye un campo "Acepta Promociones".
   - Esta preferencia se almacena en la base de datos MongoDB junto con los demás datos del cliente.

5. **Diseño en Figma:**
   - El diseño del front-end se crea utilizando la herramienta de diseño Figma.
   - El diseño guía la creación de la interfaz de usuario en React.


## Diseño de arquitectura
:::tip 
![Arquitec design](/img/Fulldiagrama.jpg)
:::