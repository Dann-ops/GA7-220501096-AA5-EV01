# Mi Primer Servicio Web de Autenticación 

¡Hola! Soy aprendiz del SENA y este es mi proyecto para la evidencia **GA7-220501096-AA5-EV01**. Aquí he diseñado y programado un servicio web (API) que permite registrar usuarios y validar su inicio de sesión.

## ¿De qué trata este proyecto?
El objetivo principal fue crear una herramienta que reciba un usuario y una contraseña y nos diga si la persona puede entrar o no. Para lograrlo, seguí estos puntos:
* Creé un sistema de **Registro**: Para guardar nuevos usuarios en una lista interna.
* Creé un sistema de **Login**: Que revisa si los datos coinciden y nos da un mensaje de éxito o de error.
* Todo está bajo **control de versiones** usando Git y GitHub.

## Herramientas que utilicé
Para que este proyecto funcionara, elegí herramientas sencillas pero muy potentes:
1. **Python**: El lenguaje de programación principal.
2. **Flask**: Un "marco de trabajo" que me facilitó convertir mi código de Python en un servicio que funciona en internet.
3. **Git/GitHub**: Para llevar el historial de mis cambios y subir el código a la nube.

## Cómo está organizado mi código
* `app.py`: Es el corazón del proyecto. Aquí escribí toda la lógica de los mensajes y el guardado de datos.
* `requirements.txt`: Es una lista pequeña que le dice a otros programadores qué librerías deben instalar (en este caso, Flask).
* `enlace_repositorio.txt`: El archivo con el link directo a este repositorio.

## Cómo probarlo en tu equipo
Si quieres ver mi trabajo en acción, solo debes:
1. Clonar este repositorio.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Correr el servidor con `python app.py`.
4. Usar herramientas como **Postman** o comandos de terminal para enviar datos a las rutas de `/registro` y `/login`.

---
**Nota personal:** Este trabajo me permitió entender cómo se comunican las aplicaciones modernas y la importancia de dar respuestas claras (como "Autenticación satisfactoria") cuando alguien intenta ingresar a un sistema.
