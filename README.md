# **Catálogo de Requisitos**

## **Requisitos Funcionales**

1. **Registro de usuarios:**
    - El sistema debe permitir a los usuarios registrarse con un nombre, email y contraseña.

2. **Inicio de sesión:**
    - El sistema debe permitir a los usuarios iniciar sesión con sus credenciales.

3. **Verificación de correo electrónico:**
    - El sistema debe enviar un correo electrónico de verificación al registrarse.
    - Los usuarios deben verificar su correo electrónico para activar su cuenta.
    - El sistema debe impedir el acceso a la cuenta si el correo no ha sido verificado.

4. **Eliminación de usuarios no verificados:**
    - El sistema debe eliminar automáticamente a los usuarios que no hayan verificado su correo electrónico en una semana.
    - La eliminación debe ser gestionada mediante un schedule en Node.js.

5. **Gestión de contraseñas:**
    - Los usuarios deben poder solicitar un restablecimiento de contraseña si la olvidan.
    - El sistema debe enviar un enlace por correo electrónico para restablecer la contraseña, válido durante 2 horas.
    - El usuario debe poder cambiar su contraseña, siempre que no sea igual a las cinco últimas.

6. **Sesión:**
    - El sistema debe permitir la persistencia de la sesión mediante JSON Web Tokens durante un período de 2 horas.

7. **Chatbot:**
    - Los usuarios deben poder iniciar un nuevo chat con el chatbot LLM.
    - El chatbot debe responder preguntas teóricas sobre programación basándose en un modelo LLM.
    - El chatbot debe recordar el contexto del chat para respuestas coherentes durante una sesión activa.
    - El backend debe realizar las peticiones necesarias a la API de Gemini para obtener las respuestas del modelo LLM.

8. **Gestión de chats:**
    - El sistema debe permitir guardar chats históricos de los usuarios.
    - Los usuarios deben poder ver su historial de chats guardados y seleccionar uno para revisarlo.

9. **Configuraciones del usuario:**
    - La configuración debe permitir elegir el nivel de detalle de las respuestas del chatbot (básico o avanzado).
    - La configuración debe incluir la posibilidad de activar o desactivar el almacenamiento automático de chats (chats temporales).
    - La configuración debe permitir cambiar el idioma del chatbot.
    - La configuración debe permitir al usuario elegir entre un tema claro y oscuro.

10. **Layout:**
    - **Header:**
        - Botón para iniciar un nuevo chat.
        - Menú desplegable con opciones como "Información de cuenta", "Historial de chats", "Configuración" y "Cerrar sesión".
    - **Footer:**
        - Información legal y datos de contacto.

11. **Cierre de sesión:**
    - Los usuarios deben poder cerrar sesión desde cualquier página.

## **Requisitos No Funcionales**

1. **Rendimiento:**
    - El sistema debe garantizar una respuesta rápida del chatbot, con un tiempo máximo de respuesta de 2 segundos para cada consulta.
    - La comunicación entre el backend y la API de Gemini debe ser eficiente, manteniendo una latencia mínima.

2. **Compatibilidad:**
    - La aplicación debe ser accesible desde dispositivos móviles y de escritorio.

3. **Seguridad:**
    - El sistema debe garantizar la seguridad de los datos mediante contraseñas hash y comunicación segura (HTTPS).

4. **Interfaz:**
    - La interfaz debe ser intuitiva, utilizando React con TypeScript y estilización con TailwindCSS.

## **Requisitos Técnicos**

1. **Frontend:**
    - Desarrollado en React.js con TypeScript y utilizando React Router DOM para el manejo de rutas.
    - Gestión del estado global mediante Redux Toolkit.

2. **Backend:**
    - Desarrollado en Node.js con Express.
    - Debe incluir un módulo para comunicarse con la API de Gemini.

3. **Base de datos:**
    - Persistencia de datos utilizando MariaDB.

4. **Seguridad:**
    - Contraseñas almacenadas con hashing seguro (bcrypt).
    - Persistencia de sesión mediante JSON Web Tokens.

5. **Correo:**
    - Envío de correos electrónicos mediante Nodemailer.

6. **Eficiencia:**
    - Implementación de mecanismos para el manejo eficiente de solicitudes concurrentes a la API de Gemini.

7. **Componentes reutilizables:**
    - Diseño del layout como componentes reutilizables en React.

## **Requisitos de Usabilidad**

1. **Accesibilidad:**
    - La interfaz debe ser fácil de entender para usuarios con conocimientos básicos de tecnología.

2. **Diseño responsivo:**
    - El diseño debe adaptarse a pantallas de distintos tamaños.

3. **Footer:**
    - Debe proporcionar enlaces claros y accesibles a información legal y de contacto.

4. **Header:**
    - Las opciones del header deben estar organizadas y ser fácilmente accesibles.

5. **Retroalimentación:**
    - El sistema debe ofrecer retroalimentación visual para indicar el estado de las acciones (como "Contraseña cambiada exitosamente").

6. **Historial de chats:**
    - Los chats deben estar ordenados cronológicamente en el historial.

7. **Sección de ayuda:**
    - Las preguntas más frecuentes sobre el uso del chatbot deben estar disponibles en una sección de ayuda.

8. **Personalización:**
    - La configuración debe incluir opciones accesibles para personalizar el comportamiento del chatbot, como nivel de detalle o tipo de ejemplos en las respuestas.
