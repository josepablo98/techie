# **Catálogo de Requisitos**

## **Requisitos Funcionales**

1. **Registro de usuarios**
    - El sistema debe permitir que los usuarios se registren proporcionando un nombre, correo electrónico y contraseña.

2. **Inicio de sesión**
    - El sistema debe permitir que los usuarios inicien sesión utilizando su correo electrónico y contraseña registrados.

3. **Verificación de correo electrónico**
    - El sistema debe enviar un correo electrónico de verificación al registrarse.
    - Los usuarios deben verificar su correo electrónico para activar su cuenta.
    - El sistema debe impedir el acceso a la cuenta si el correo electrónico no ha sido verificado.

4. **Eliminación de usuarios no verificados**
    - El sistema debe eliminar automáticamente a los usuarios que no hayan verificado su correo electrónico en el plazo de una semana.
    - La eliminación debe gestionarse mediante un proceso programado (schedule) en Node.js.

5. **Gestión de contraseñas**
    - El sistema debe permitir que los usuarios soliciten el restablecimiento de contraseña en caso de olvido.
    - El sistema debe enviar un enlace por correo electrónico para restablecer la contraseña, con una validez de 2 horas.
    - El sistema debe permitir el cambio de contraseña, siempre que esta no coincida con ninguna de las cinco últimas utilizadas.

6. **Gestión de sesión**
    - El sistema debe mantener la sesión del usuario mediante JSON Web Tokens (JWT) con una validez de 2 horas.

7. **Chatbot**
    - El sistema debe permitir que los usuarios inicien un nuevo chat con el chatbot LLM.
    - El chatbot debe responder preguntas teóricas sobre programación en Python, utilizando un modelo LLM.
    - El chatbot debe conservar el contexto del chat durante la sesión activa para proporcionar respuestas coherentes.
    - El backend debe encargarse de realizar las peticiones necesarias a la API de Gemini para obtener las respuestas del modelo LLM.

8. **Gestión de chats**
    - El sistema debe permitir almacenar un historial de chats de los usuarios. Cada chat guardado debe incluir un título y la fecha de su última interacción.
    - El historial de chats debe estar ordenado cronológicamente.
    - El sistema debe permitir que los usuarios visualicen y seleccionen sus chats guardados para revisarlos.

9. **Configuraciones del usuario**
    - El sistema debe permitir que el usuario configure:
        - El nivel de detalle de las respuestas del chatbot (básico o avanzado).
        - La activación o desactivación del almacenamiento automático de chats (chats temporales).
        - El idioma del chatbot.
        - El tema visual de la interfaz (claro u oscuro).
        - Un contexto global personalizado que el chatbot tendrá en cuenta durante la conversación (por ejemplo, cómo debe dirigirse al usuario o el tono que debe usar), siempre y cuando no contradiga instrucciones prioritarias como el idioma o el nivel de detalle.

10. **Interfaz - Layout**
    
    10.1. **Header**
    - Botón para iniciar un nuevo chat.
    - Menú desplegable con opciones como: "Información de cuenta", "Historial de chats", "Configuración" y "Cerrar sesión".
    
    10.2. **Footer**
    - Información sobre el chatbot.
    - Enlaces accesibles a contacto y política de privacidad.

11. **Cierre de sesión**
    - El sistema debe permitir que los usuarios cierren sesión desde el menú del encabezado (header).

12. **Eliminación de chats**
    - El sistema debe permitir que los usuarios eliminen chats individuales o todos sus chats desde la sección "Configuración".
    - El sistema debe requerir una confirmación previa para evitar eliminaciones accidentales.

13. **Eliminación de cuenta**
    - El sistema debe permitir que los usuarios eliminen su cuenta desde la sección "Configuración".
    - El sistema debe requerir doble confirmación para evitar eliminaciones accidentales.

---

## **Requisitos No Funcionales**

1. **Rendimiento**
    - El sistema debe proporcionar una respuesta rápida del chatbot, con un tiempo máximo de 2 segundos por consulta.
    - La comunicación entre el backend y la API de Gemini debe ser eficiente, con latencia mínima.

2. **Compatibilidad**
    - La aplicación debe ser accesible desde dispositivos móviles y ordenadores de escritorio.

3. **Interfaz**
    - La interfaz debe ser intuitiva y estar desarrollada utilizando React con TypeScript y estilizada con TailwindCSS.

---

## **Requisitos Técnicos**

1. **Frontend**
    - El frontend debe estar desarrollado en React.js con TypeScript.
    - El sistema de rutas debe gestionarse con React Router DOM.
    - La gestión del estado global debe implementarse mediante Redux Toolkit.

2. **Backend**
    - El backend debe estar desarrollado en Node.js con Express para la lógica principal y la gestión de la base de datos.
    - Un segundo backend en Flask (Python) debe encargarse de la interacción con la API de Gemini.

3. **Base de datos**
    - El sistema debe utilizar MariaDB para la persistencia de datos.

4. **Seguridad**
    - Las contraseñas deben almacenarse utilizando hashing seguro con bcrypt.
    - Las sesiones deben mantenerse mediante JSON Web Tokens (JWT) y cookies seguras.

5. **Correo electrónico**
    - El sistema debe gestionar el envío de correos electrónicos utilizando Nodemailer.

6. **Componentes reutilizables**
    - El diseño del layout debe componerse a partir de componentes reutilizables en React.

---

## **Requisitos de Usabilidad**

1. **Accesibilidad**
    - La interfaz debe ser comprensible y fácil de usar para usuarios con conocimientos básicos de tecnología.

2. **Footer**
    - El pie de página debe incluir enlaces claros y accesibles a la política de privacidad, contacto e información del chatbot.

3. **Header**
    - Las opciones del encabezado deben estar bien organizadas y ser fácilmente accesibles.

4. **Retroalimentación**
    - El sistema debe proporcionar retroalimentación visual clara tras la realización de acciones, como por ejemplo: "Contraseña cambiada exitosamente".

5. **Historial de chats**
    - El historial debe mostrar los chats ordenados cronológicamente.

6. **Personalización**
    - Las opciones de configuración deben estar disponibles de forma accesible para permitir personalizar el comportamiento del chatbot, como el nivel de detalle o el tipo de ejemplos en las respuestas.
