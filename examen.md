# Instituto Tecnológico de Morelia
## Examen Diagnóstico - Fundamentos de Ingeniería de Software

**Materia:** Tópicos Selectos de Tecnologías Web y Móvil
**Profesor:** Jesús Eduardo Alcaraz Chávez
**Nombre del alumno:** Seth Ricardo Millán Dávalos
**Fecha:** 27/08/2026

**Instrucciones:** Responde de manera clara y concisa a cada una de las siguientes preguntas abiertas. El propósito de esta evaluación es medir tus conocimientos previos en Ingeniería de Software.

---

### 1. Metodologías
**Pregunta:** ¿Cuál es la diferencia principal entre una metodología de desarrollo tradicional (como Cascada) y una metodología ágil (como Scrum) frente a los cambios en los requisitos?

**Respuesta:** La principal diferencia entre las metodologías ágiles y las de cascada son los constantes procesos de iteración en las metodologías ágiles, mientras que las metodologías de cascada siguen una línea de tiempo más rígida. Las metodologías ágiles se dividen en ciclos de iteraciones conocidos como "sprints", de este modo en cada iteración se realiza una reunión con el equipo para revisar avances o bloqueos en el progreso del proyecto.

---

### 2. Requerimientos
**Pregunta:** Explica la diferencia entre requerimientos funcionales y no funcionales, dando un ejemplo de cada uno aplicable a una plataforma web.

**Respuesta:** Los requerimientos funcionales, como su nombre lo indica, se centran en la funcionalidad principal del sistema; en general se podría decir que en una plataforma web, los requerimientos funcionales serían los módulos o secciones específicas del sitio. Si fuera una plataforma web de reservas couch-surfing, uno de los requerimientos funcionales sería que el usuario pudiera tener una vista de los sitios que se ofertan en el área donde se va a hospedar.

Los requerimientos no funcionales no van relacionados a la funcionalidad, sino que se relacionan con el estilo o diseño del sitio, pudiendo ser la tipografía, la paleta de colores y otras cosas relacionadas principalmente con la UI.

---

### 3. Arquitectura
**Pregunta:** Describe el modelo Cliente-Servidor y explica brevemente cómo se comunican el frontend y el backend en una aplicación web moderna.

**Respuesta:** N/A

---

### 4. Bases de Datos
**Pregunta:** ¿En qué escenarios recomendarías utilizar una base de datos relacional (SQL) frente a una no relacional (NoSQL) para el almacenamiento de datos en una aplicación?

**Respuesta:** Normalmente siempre se usará una base de datos relacional por sobre una no relacional, esto debido al dinamismo y la forma práctica que nos permite trabajar sobre la misma; entre los principales beneficios de la misma está el "delete on cascade": al borrar un dato, la información relacionada a este se elimina. Como ejemplo, para un administrador inmobiliario tendríamos una tabla de propiedades y otra de imágenes; al borrar una propiedad se borrarían las imágenes relacionadas a esa propiedad, manteniendo nuestra base de datos controlada sin información basura que no necesitamos.

Vale más preguntar si realmente podríamos necesitar una base de datos no relacional; en ese caso la usaremos cuando los datos que tengamos en el sistema no se relacionen del todo entre sí y borrar una tupla no signifique dejar datos fantasma en nuestras tablas. El ejemplo más conocido es el de las redes sociales: al borrar un usuario no es necesario borrar más información relacionada a este, como sería la escuela en la que estudió, ya que son datos que sobreviven de manera independiente; por el mismo tamaño que pueden llegar a tomar este tipo de bases de datos, es conveniente usar una no relacional.

---

### 5. APIs
**Pregunta:** ¿Qué es una API REST y qué papel fundamental juega en la integración entre una aplicación móvil y los servidores (backend)?

**Respuesta:** Las API REST son la forma que tenemos de comunicarnos con una base de datos para mostrar información en nuestras aplicaciones o sitios; son fundamentales porque antes de las API REST la comunicación entre los sitios no estaba estandarizada, entonces todos los sitios mandaban información de manera diferente. REST llegó para "poner orden" y decir "así se van a pedir los datos", de este modo, al usar todos REST, sabemos que si necesitamos solicitar datos se usará una función GET, para actualizar UPDATE, y así sucesivamente con las demás funciones.

---

### 6. Control de Versiones
**Pregunta:** Explica la importancia de utilizar Git en un equipo de desarrollo de software y describe brevemente qué es un "merge conflict" (conflicto de fusión).

**Respuesta:** La importancia de usar un sistema de control de versiones (Git, no GitHub) radica en poder mantener un "historial" de nuestro código y poder retroceder en versiones en caso de haber hecho cambios "destructivos" que busquemos reparar. Asimismo, podemos trabajar con ramas en las cuales podríamos dejar diferentes "fases" de avance o avances de "módulos" de nuestro sistema. En cuanto a integrarlo con GitHub, permite una colaboración de equipos fluida, permitiendo trabajar desde cualquier computadora, evitando así perder nuestro código en caso de que el equipo en el que trabajamos se dañe.

Un merge conflict es un conflicto al intentar juntar los cambios de dos ramas; generalmente sucede cuando dos personas están trabajando en un mismo archivo y hay una incompatibilidad en cuanto a cambios (por ejemplo, uno borra una función y otro solo la modifica). Para solucionarlo hay que revisar el código manualmente y se puede reescribir, o ver las dos versiones y decidir cuál se queda.

---

### 7. Pruebas
**Pregunta:** ¿Qué son las pruebas unitarias (unit testing) y por qué son cruciales para asegurar la calidad del software antes de su paso a producción?

**Respuesta:** Las pruebas unitarias se encargan de probar una única función en el sistema. El ejemplo más sencillo es que si tenemos una aplicación de calculadora con la función sumar, la prueba unitaria se encarga de que el resultado de 1 + 1 siempre sea 2; en caso de modificar la función, al momento de ejecutar el programa se realizan las pruebas unitarias y se verifica que todas funcionen de manera adecuada. Son cruciales para evitar que código equivocado llegue a producción; de hecho, existe un "paradigma" o forma de programar que consiste en realizar primero las pruebas de nuestro código y después programarlo, asegurando que pase las pruebas.

---

### 8. POO
**Pregunta:** Define los conceptos de encapsulamiento y polimorfismo de la Programación Orientada a Objetos, y menciona cómo ayudan a crear un código más mantenible.

**Respuesta:** El encapsulamiento es cuando tenemos una variable en un único objeto y la asignamos como "private" o variable privada.

El polimorfismo es la manera que tenemos de generar un molde de un objeto para hacer objetos con características similares; podríamos poner el ejemplo de figuras geométricas como la clase padre, y como clases hijas tener círculo, cuadrado, etc. Esto ayuda a tener un código mantenible al permitirnos modificar las características generales de la clase padre en caso de que necesitemos cambios en todas las clases hijo, o agregar funcionalidades únicas a cada clase hijo que ninguna otra tendría.

---

### 9. Patrones de Diseño
**Pregunta:** ¿Qué es el patrón de arquitectura Modelo-Vista-Controlador (MVC) y cómo ayuda a organizar el código en el desarrollo de software?

**Respuesta:** En el modelo vista controlador tenemos un diseño modular en el que dividimos el código en controller, models y services. En models tenemos las entidades que se generan para que coincidan con la información en nuestra base de datos; en servicios tenemos las interfaces y la implementación de las funciones que realizarán nuestras entidades; y el controlador solo llama a estas funciones asociadas a métodos HTTP como @Get para indicar con qué método se puede encontrar la función.

Ayuda a organizar el código manteniendo todo separado y simple, sin generar cientos de líneas de código para una sola entidad, aunque implica muchas carpetas y en proyectos más grandes podríamos tener problemas. Al tener separado dónde se crea la entidad, dónde se crean las funciones y dónde se utilizan, mantenemos el código sencillo y escalable.

---

### 10. Seguridad
**Pregunta:** Explica la diferencia técnica entre "autenticación" y "autorización" en el contexto de seguridad de una aplicación.

**Respuesta:** Autenticación es verificar que una persona tenga la identidad que dice tener; autorización es verificar que esta persona tenga los permisos para acceder a los datos que busca acceder.