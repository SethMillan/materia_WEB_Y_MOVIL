# Paradigmas de programación y patrones de diseño

## 1. Paradigmas de programación (clasificados)

### 1.1 Imperativos
Se centra en describir **cómo** lograr un resultado mediante instrucciones que cambian el estado del programa paso a paso.

- **Procedural**: el programa se organiza en procedimientos/funciones que operan sobre datos compartidos. Ej: C, Pascal.
- **Estructurado**: subconjunto del procedural que restringe el flujo a secuencia, selección e iteración, evitando `goto`. Ej: C, Ada.
- **Modular**: agrupa procedimientos y datos relacionados en módulos con interfaces públicas y detalles ocultos. Ej: Modula-2, Python (módulos).
- **Orientado a objetos (OOP)**: organiza el estado y comportamiento en objetos que se comunican mediante mensajes; se apoya en encapsulación, herencia y polimorfismo. Ej: Java, C++, Smalltalk, Ruby.

### 1.2 Declarativos
Describe **qué** se quiere lograr, dejando el "cómo" al motor de ejecución.

- **Funcional**: computación como evaluación de funciones matemáticas puras, sin efectos secundarios ni estado mutable; usa funciones de orden superior. Ej: Haskell, Elixir, Clojure, F#.
- **Lógico**: el programa es un conjunto de hechos y reglas; la ejecución es un proceso de inferencia/resolución de consultas. Ej: Prolog, Datalog.
- **Funcional-lógico (híbrido)**: combina evaluación funcional con unificación y búsqueda lógica. Ej: Curry, Mercury.
- **Basado en restricciones (constraint)**: se declaran relaciones/restricciones entre variables y un solver encuentra valores que las satisfacen. Ej: MiniZinc, Prolog con CLP.
- **De flujo de datos (dataflow)**: el cómputo se modela como un grafo donde los nodos se ejecutan cuando sus datos de entrada están disponibles. Ej: LabVIEW, TensorFlow (grafos), Apache Beam.

### 1.3 Orientados a eventos y reactivos
- **Dirigido por eventos**: el flujo de control lo determinan eventos (clics, mensajes, señales) capturados por manejadores. Ej: JavaScript (DOM), Node.js.
- **Reactivo**: se modelan flujos de datos asíncronos (streams) que se propagan automáticamente a los observadores cuando cambian. Ej: RxJS, ReactiveX, Elm.

### 1.4 Concurrentes / paralelos
- **Basado en actores**: unidades independientes (actores) con estado privado que se comunican exclusivamente por mensajes asíncronos. Ej: Erlang, Akka (Scala/Java).
- **CSP (Communicating Sequential Processes)**: procesos concurrentes que se sincronizan e intercambian datos mediante canales. Ej: Go, occam.
- **Paralelo de datos**: la misma operación se aplica simultáneamente sobre grandes colecciones de datos repartidos entre unidades de cómputo. Ej: CUDA, OpenMP.

### 1.5 Otros paradigmas relevantes
- **Orientado a aspectos (AOP)**: separa incumbencias transversales (logging, seguridad, transacciones) del código de negocio mediante "aspectos" tejidos en puntos de corte. Ej: AspectJ, Spring AOP.
- **Genérico**: algoritmos y estructuras de datos escritos en términos de tipos a especificar después, maximizando reutilización con seguridad de tipos. Ej: C++ (templates), Java (generics), Rust.
- **Simbólico**: manipula símbolos y estructuras de conocimiento en lugar de solo números; típico de IA clásica. Ej: LISP.
- **Basado en prototipos**: la herencia se logra clonando objetos existentes ("prototipos") en vez de instanciar clases. Ej: JavaScript, Self, Lua.

---

## 2. Patrones de diseño (catálogo GoF completo)

### 2.1 Creacionales
Resuelven **cómo se crean los objetos**, ocultando la lógica de instanciación para desacoplar al cliente de las clases concretas.

**Abstract Factory**
Define una interfaz para crear familias de objetos relacionados o dependientes entre sí sin especificar sus clases concretas. El cliente trabaja únicamente contra interfaces abstractas, y una fábrica concreta decide qué variante de la familia instanciar, lo que permite intercambiar toda una familia de productos (por ejemplo, componentes de UI para distintos sistemas operativos) cambiando solo la fábrica utilizada, sin tocar el código cliente.
*Uso típico*: Java Swing (`UIManager` de Look and Feel), .NET (`DbProviderFactory`), toolkits multiplataforma como Qt.

**Builder**
Separa la construcción de un objeto complejo de su representación final, permitiendo que el mismo proceso de construcción, ejecutado paso a paso mediante métodos encadenables, genere distintas representaciones. Es especialmente útil cuando un objeto tiene muchos parámetros opcionales, evitando constructores con decenas de argumentos ("telescoping constructor") y mejorando la legibilidad del código de ensamblado.
*Uso típico*: Java (`StringBuilder`, `Lombok @Builder`), Kotlin (DSL builders), Android (`AlertDialog.Builder`).

**Factory Method**
Define una interfaz para crear un objeto, pero delega en las subclases la decisión de qué clase concreta instanciar. El código base trabaja contra el tipo abstracto devuelto y no necesita conocer la clase real creada, lo que facilita extender el sistema con nuevos productos simplemente agregando una nueva subclase creadora, cumpliendo el principio abierto/cerrado.
*Uso típico*: Java (`Calendar.getInstance()`, `Collection.iterator()`), .NET (`Activator.CreateInstance`).

**Prototype**
Permite crear nuevos objetos clonando una instancia existente ("prototipo") en lugar de construirlos desde cero, lo cual es útil cuando la creación es costosa o cuando se desea evitar una jerarquía de fábricas. Requiere implementar una operación de copia (superficial o profunda) que el propio objeto expone, desacoplando al cliente de las clases concretas de los objetos que clona.
*Uso típico*: JavaScript (herencia prototípica nativa, `Object.create`), Java (interfaz `Cloneable`).

**Singleton**
Garantiza que una clase tenga una única instancia global y proporciona un punto de acceso centralizado a ella, típicamente mediante un constructor privado y un método estático que crea la instancia de forma perezosa o anticipada. Se usa para recursos compartidos como configuración, logging o conexiones, aunque es criticado por introducir estado global y dificultar las pruebas unitarias si se abusa de él.
*Uso típico*: Java (`enum` singleton), Python (módulos, que son singletons por naturaleza), Spring (beans con scope "singleton" por defecto).

### 2.2 Estructurales
Resuelven **cómo se componen clases y objetos** para formar estructuras más grandes manteniéndolas flexibles y eficientes.

**Adapter**
Convierte la interfaz de una clase en otra interfaz que el cliente espera, permitiendo que clases con interfaces incompatibles colaboren sin modificar su código fuente. Actúa como un traductor intermedio: envuelve al objeto adaptado (adaptee) y traduce las llamadas del cliente en llamadas que el adaptado entiende, siendo muy común al integrar librerías de terceros o código heredado.
*Uso típico*: Java (`Arrays.asList()`), Spring (`HandlerAdapter`), integraciones de APIs externas en cualquier lenguaje.

**Bridge**
Desacopla una abstracción de su implementación de modo que ambas puedan variar de forma independiente, evitando una explosión combinatoria de subclases cuando existen dos dimensiones de variación (por ejemplo, forma y renderizador). La abstracción mantiene una referencia a un objeto de la jerarquía de implementación y delega en él el trabajo real, en vez de heredar directamente de ella.
*Uso típico*: Java (`JDBC`, separando la API de acceso a datos del driver concreto), interfaces gráficas con múltiples backends de renderizado.

**Composite**
Compone objetos en estructuras de árbol para representar jerarquías parte-todo, permitiendo que los clientes traten de manera uniforme tanto a objetos individuales (hojas) como a composiciones de objetos (nodos), gracias a una interfaz común. Esto simplifica enormemente el código cliente al recorrer o manipular estructuras recursivas sin distinguir tipos.
*Uso típico*: sistemas de archivos, DOM de HTML/XML, componentes de UI en frameworks como React o vistas de Android (`ViewGroup`).

**Decorator**
Añade responsabilidades adicionales a un objeto de forma dinámica envolviéndolo en uno o más objetos decoradores que implementan la misma interfaz, ofreciendo una alternativa flexible a la herencia para extender funcionalidad. Cada decorador puede añadir comportamiento antes o después de delegar la llamada al objeto envuelto, permitiendo combinar responsabilidades en tiempo de ejecución.
*Uso típico*: Java I/O (`BufferedReader` envolviendo `FileReader`), Python (`@decorador` de funciones), middlewares web.

**Facade**
Proporciona una interfaz simplificada y unificada a un conjunto de interfaces de un subsistema complejo, reduciendo el acoplamiento entre el cliente y las clases internas del subsistema. No oculta el acceso directo a las clases internas si se necesita, pero ofrece un punto de entrada cómodo para los casos de uso más comunes, mejorando la legibilidad y facilitando el mantenimiento.
*Uso típico*: jQuery (fachada sobre el DOM y XHR), Spring (`JdbcTemplate` sobre JDBC), SDKs de servicios en la nube.

**Flyweight**
Minimiza el uso de memoria compartiendo eficientemente el estado común (intrínseco) entre múltiples objetos similares, mientras el estado que varía (extrínseco) se pasa como parámetro en tiempo de ejecución en lugar de almacenarse en cada instancia. Es especialmente valioso cuando se necesitan crear grandes cantidades de objetos parecidos, como en editores de texto o motores gráficos.
*Uso típico*: Java (`Integer.valueOf()` con caché de valores pequeños), renderizado de glifos de texto, motores de videojuegos con miles de sprites.

**Proxy**
Proporciona un objeto sustituto o representante que controla el acceso a otro objeto, pudiendo añadir lógica adicional como carga diferida (lazy loading), control de acceso, caché o registro de llamadas, de forma transparente para el cliente que interactúa con el proxy como si fuera el objeto real. Existen variantes: proxy virtual, de protección, remoto y de caché.
*Uso típico*: Java (`java.lang.reflect.Proxy`, Hibernate lazy loading), Spring AOP (proxies dinámicos), JavaScript (`Proxy` nativo).

### 2.3 De comportamiento
Resuelven **cómo interactúan y se distribuyen responsabilidades** entre objetos, centrándose en algoritmos y comunicación.

**Chain of Responsibility**
Evita acoplar al emisor de una petición con su receptor, dando a más de un objeto la oportunidad de manejarla: los objetos receptores se encadenan y la petición viaja a lo largo de la cadena hasta que alguno la procesa o se llega al final. Permite añadir o reordenar manejadores dinámicamente sin modificar el código cliente que origina la solicitud.
*Uso típico*: middlewares de Express.js, filtros de Servlets en Java, pipelines de ASP.NET Core.

**Command**
Encapsula una petición o acción como un objeto independiente, incluyendo el receptor y los parámetros necesarios para ejecutarla, lo que permite parametrizar clientes con distintas peticiones, encolarlas, registrarlas en un log y soportar operaciones deshacer/rehacer. Desacopla al objeto que invoca la operación del que sabe cómo realizarla.
*Uso típico*: sistemas de "undo/redo" en editores, colas de tareas (`java.util.concurrent.Callable`/`Runnable`), atajos de teclado configurables.

**Interpreter**
Define una representación para la gramática de un lenguaje sencillo junto con un intérprete que usa esa representación para evaluar sentencias del lenguaje, típicamente mediante un árbol sintáctico donde cada nodo sabe interpretarse a sí mismo. Es útil para lenguajes de dominio específico (DSL) pequeños, aunque puede volverse difícil de mantener con gramáticas complejas.
*Uso típico*: motores de expresiones regulares, parsers de SQL simplificado, motores de reglas de negocio.

**Iterator**
Proporciona una forma de acceder secuencialmente a los elementos de una colección sin exponer su representación interna (array, lista enlazada, árbol), ofreciendo una interfaz uniforme (`hasNext()`/`next()`) que permite recorrer distintas estructuras de datos de manera consistente y soporta múltiples recorridos simultáneos e independientes sobre la misma colección.
*Uso típico*: Java (`Iterator`, `Iterable`), Python (protocolo `__iter__`/`__next__`, generadores con `yield`), C# (`IEnumerable`).

**Mediator**
Define un objeto que encapsula cómo interactúa un conjunto de objetos, promoviendo bajo acoplamiento al evitar que se refieran explícitamente unos a otros; en su lugar, cada objeto colega se comunica solo con el mediador, que coordina la interacción global. Simplifica la topología de comunicación de una red de "muchos a muchos" a "muchos a uno".
*Uso típico*: controladores de diálogos de UI, `java.util.Timer`, salas de chat en aplicaciones en tiempo real.

**Memento**
Sin violar la encapsulación, captura y externaliza el estado interno de un objeto para poder restaurarlo posteriormente a ese estado, típicamente para implementar funciones de deshacer o puntos de control (checkpoints). El objeto originador crea el memento, un cuidador (caretaker) lo almacena sin inspeccionar su contenido, y solo el originador puede usarlo para restaurar su estado.
*Uso típico*: guardado de partidas en videojuegos, transacciones con rollback, historial de versiones en editores.

**Observer**
Define una dependencia uno-a-muchos entre objetos, de forma que cuando el objeto observado (sujeto) cambia de estado, todos sus observadores registrados son notificados y actualizados automáticamente. Es la base de la programación orientada a eventos y de la arquitectura MVC, permitiendo que múltiples partes de un sistema reaccionen a cambios sin acoplamiento directo con la fuente del cambio.
*Uso típico*: eventos de DOM en JavaScript, `PropertyChanged` en .NET, RxJS/Rx (Observables), Vue.js (reactividad).

**State**
Permite que un objeto altere su comportamiento cuando cambia su estado interno, dando la apariencia de que el objeto cambia de clase; cada estado se modela como una clase separada que implementa la interfaz común, y el objeto delega en el estado actual el comportamiento correspondiente. Evita largas cadenas de condicionales `if/switch` basadas en el estado.
*Uso típico*: máquinas de estado en pedidos de e-commerce, controladores de reproductores multimedia, protocolos de red (TCP).

**Strategy**
Define una familia de algoritmos, encapsula cada uno en una clase separada y los hace intercambiables en tiempo de ejecución, permitiendo que el algoritmo varíe independientemente de los clientes que lo usan. El contexto mantiene una referencia a una estrategia y delega en ella el trabajo, favoreciendo la composición sobre la herencia para variar comportamiento.
*Uso típico*: Java (`Comparator`), algoritmos de ordenamiento/compresión intercambiables, motores de validación configurables.

**Template Method**
Define en una clase base el esqueleto invariable de un algoritmo, delegando en subclases la implementación de ciertos pasos específicos sin cambiar la estructura general del algoritmo. Usa el principio de "Hollywood" (no llames tú, te llamaremos): la clase base controla el flujo y llama a los métodos que las subclases sobrescriben (hooks).
*Uso típico*: Spring (`JdbcTemplate`, `RestTemplate`), frameworks de testing (`setUp`/`tearDown`), servlets Java (`doGet`/`doPost`).

**Visitor**
Representa una operación a realizar sobre los elementos de una estructura de objetos heterogénea, permitiendo definir nuevas operaciones sin modificar las clases de los elementos sobre los que opera, mediante doble despacho (`accept`/`visit`). Es útil cuando la jerarquía de clases es estable pero se necesitan añadir frecuentemente nuevas operaciones sobre ella.
*Uso típico*: compiladores (recorrido de AST), procesadores de documentos XML/JSON, herramientas de análisis estático de código.

### 2.4 Patrones de concurrencia (complementarios al catálogo GoF)
Diseñados específicamente para sistemas multihilo o distribuidos, donde el reto principal es coordinar acceso a recursos compartidos y comunicación entre unidades de ejecución independientes.

**Active Object**
Desacopla la invocación de un método de su ejecución, ejecutando las peticiones en un hilo dedicado mediante una cola de solicitudes, de modo que el llamador no se bloquea y puede continuar de forma asíncrona mientras el resultado se resuelve en segundo plano.
*Uso típico*: Akka (actores en Scala/Java), `ExecutorService` de Java combinado con `Future`.

**Actor Model**
Modela la concurrencia como actores independientes con estado privado que solo se comunican mediante paso de mensajes asíncronos, eliminando la necesidad de locks explícitos porque cada actor procesa un mensaje a la vez de su propia bandeja de entrada, favoreciendo sistemas tolerantes a fallos y distribuidos.
*Uso típico*: Erlang/Elixir (OTP, `GenServer`), Akka.

**Monitor Object**
Sincroniza la ejecución concurrente de métodos de un objeto asegurando que solo un hilo pueda ejecutar un método a la vez sobre ese objeto, combinando mutua exclusión con variables de condición para esperar y notificar cambios de estado de forma segura.
*Uso típico*: `synchronized` en Java, `Lock`/`Condition` en C#.

**Producer-Consumer**
Coordina dos tipos de procesos mediante una cola compartida: los productores generan datos y los depositan en la cola mientras los consumidores los retiran y procesan, desacoplando la velocidad de generación de la de procesamiento y evitando condiciones de carrera mediante sincronización de la cola.
*Uso típico*: `BlockingQueue` en Java, canales (`channels`) en Go.

**Reactor**
Gestiona múltiples solicitudes de servicio entregadas concurrentemente por uno o más clientes, demultiplexando y despachando eventos de E/S entrantes de forma síncrona a los manejadores correspondientes desde un único hilo, evitando el costo de un hilo por conexión.
*Uso típico*: Node.js (event loop), Netty, Nginx.

---

## 3. Lenguajes y frameworks con su patrón de diseño característico

| # | Lenguaje / Framework | Patrón de diseño asociado |
|---|---|---|
| 1 | Smalltalk | Observer (origen de MVC) |
| 2 | Java (Collections/JDK) | Iterator y Factory Method |
| 3 | JavaScript | Prototype y Decorator |
| 4 | Python | Iterator y Decorator |
| 5 | C# / .NET | Observer (eventos) e Iterator |
| 6 | Go | Strategy (interfaces implícitas) y Producer-Consumer (channels) |
| 7 | Rust | Builder y Strategy (traits) |
| 8 | Erlang / Elixir | Actor Model |
| 9 | Swift / Objective-C (Cocoa) | Delegate (variante de Observer/Strategy) |
| 10 | Haskell | Decorator funcional (composición de funciones) |
| 11 | Ruby on Rails | Active Record (variante de Template Method) |
| 12 | Django | Active Record + Template Method |
| 13 | Laravel | Facade e Inyección de Dependencias |
| 14 | Spring / Spring Boot | Proxy (AOP) y Template Method |
| 15 | Angular | Observer (RxJS) y Dependency Injection |
| 16 | React | Composite y Observer (estado y props) |
| 17 | Vue.js | Observer (reactividad) y MVVM |
| 18 | Redux | Command y Mediator (store centralizado) |
| 19 | Express.js | Chain of Responsibility (middleware) |
| 20 | Node.js | Reactor (event loop no bloqueante) |
