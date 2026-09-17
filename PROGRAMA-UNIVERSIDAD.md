# El problema
Una universidad pública mantiene el alta de materias, el pago de inscripción, las constancias y las becas en decenas de páginas sueltas (PHP, ASP clásico y un par de servicios nuevos). Se requiere un portal web único para el siguiente ciclo.

El estado actual, documentado por control escolar y por caja, es el siguiente.

1. Cada trámite es un archivo distinto. En todos se copia el mismo bloque de «¿hay sesión?», el mismo registro en bitácora y el mismo encabezado HTML. Cuando cambia la regla de caducidad de la sesión, hay que tocar cuarenta archivos; siempre se olvida uno.
2. El pago de inscripción admite tarjeta, transferencia SPEI y referencia de ventanilla. El script de pagar.php es un switch de doscientas líneas. Cada banco nuevo obliga a editar ese archivo. El protocolo de un banco habla de «créditos» y códigos 00/01; el reglamento interno habla de «pago de inscripción» y estados pendiente / acreditado / rechazado.
3. La plantilla del kardex ejecuta consultas SQL para armar la tabla de calificaciones. Los reportes de constancias duplican esas consultas con otro formato.
4. Cuando el pago se acredita, el mismo script llama a control escolar (alta de materias), dispara un correo al estudiante y avisa a caja. Si el correo falla, a veces no se registra el alta. Si el estudiante pulsa dos veces «pagar» porque la página tarda, se han cobrado dos cargos.
5. La aplicación móvil de la universidad y el kiosco de la biblioteca deben mostrar el mismo trámite. La app pide un JSON mínimo (folio, saldo, plazo). El kiosco pide una página HTML con el escudo y la tabla de vencimientos. Hoy el equipo de la app hace doce peticiones para pintar la pantalla de inicio.
6. El servicio de un banco y el de un validador de CURP externo se caen con frecuencia. Mientras no responden, el estudiante ve la rueda de espera y no puede ni consultar el kardex, que no depende de esos colaboradores.
7. Un proveedor propone, para la descarga de una constancia en PDF, Event Sourcing, CQRS, una malla de microservicios y un almacén global Redux en el navegador. El trámite de la constancia es: autenticar, consultar un registro ya existente y generar un archivo.

## Qué se evalúa
| Criterio | Se espera |
|---|---|
| Composición | El portal no se etiqueta con un solo patrón. Cada conflicto tiene una estructura y una capa. |
| Cuándo y por qué | Se justifica con una fuerza del problema, no con «porque sale en el temario». |
| Vecino rechazado | Adapter no se confunde con Facade; Observer no sustituye a Unit of Work. |
| Marco | Se nombra qué no hay que reescribir si el equipo usa Spring, Laravel o Express. |
| Sobreingeniería |	Se rechaza el catálogo donde no hay problema. |

## Misión 1 — El portal no es un patrón
Enuncie seis problemas distintos del relato (un renglón cada uno). Para cada uno indique:

- la capa (presentación, políticas transversales, aplicación/dominio, datos, integración);
- el patrón (o la pareja de patrones) que corresponde;
- por qué ese y no el vecino más fácil de confundir (por ejemplo Adapter frente a Facade, Observer frente a Unit of Work);
- cuándo no aplicaría, aunque el nombre «quede bonito».

**Entregable:** una tabla de seis filas. El portal no puede aparecer como «es MVC» ni como «es hexagonal».

### Misión 2 — Una petición, varios patrones
Siga el caso de uso pagar la inscripción desde el clic (o desde POST) hasta persistir y notificar. Liste, en orden, las estructuras que atraviesa la petición. Para cada paso: qué objeto o mecanismo es (enrutador, filtro, servicio, repositorio…) y qué patrón está realizando.

Apóyese en el esquema de composición a lo largo de una petición HTTP del apartado web. No invente una capa vacía que solo delega.

---

## Respuesta — Misión 1: seis problemas, seis estructuras

| # | Problema (un renglón) | Capa | Patrón / pareja | Por qué ese y no el vecino | Cuándo no aplicaría |
|---|---|---|---|---|---|
| 1 | El bloque de «¿hay sesión?», el registro en bitácora y el encabezado HTML se copian en cada archivo; cambiar la caducidad obliga a tocar cuarenta. | Políticas transversales | **Front Controller + cadena de middlewares** (Chain of Responsibility); *layout* / Template Method para el encabezado. | El vecino es Decorator. Se elige la cadena porque cada eslabón decide si continúa o corta la petición (redirige a login) y el orden importa; no se envuelve un servicio para añadirle una operación de negocio manteniendo su interfaz, se construye un *pipeline* de entrada sobre la solicitud. | Con dos o tres páginas y una sola regla transversal, un `include` basta; la tubería añade indirección que no se paga. |
| 2 | `pagar.php` es un `switch` de 200 líneas; cada banco nuevo lo edita. El banco habla de «créditos» y códigos 00/01; el reglamento habla de «pago de inscripción» y pendiente/acreditado/rechazado. | Integración (y aplicación para el vocabulario) | **Strategy** (una `PasarelaPago` por medio de pago) **+ Adapter** (traduce protocolo y códigos del banco al lenguaje del dominio). | Adapter y no **Facade**: el fin es traducir un contrato y un vocabulario ajenos, no dar una cara simple a un subsistema propio complejo. Strategy y no **State**: varía el algoritmo de cobro elegido por un dato de entrada, no un ciclo de vida del objeto. | Si todos los bancos se integraran por el mismo estándar y solo cambiaran credenciales: eso es configuración, no un patrón. |
| 3 | La plantilla del kardex ejecuta SQL para armar las calificaciones; los reportes de constancias duplican esas consultas con otro formato. | Datos | **Repository + Query Object** para la tabla de calificaciones. | Repository y no **Active Record**: hay varios consumidores (kardex, constancias) que necesitan la misma consulta con distinta presentación; el registro no debe cargar su SQL ni la vista ejecutarlo. No es un **DAO** genérico: expone una colección del dominio (`calificacionesDe(estudiante, ciclo)`), no CRUD por tabla. | Un reporte único, de una sola pantalla, que nadie más consume: la consulta directa es honesta. |
| 4 | Al acreditar el pago, el mismo script da de alta materias, manda correo y avisa a caja; si el correo falla, a veces no se registra el alta; dos clics generan dos cargos. | Aplicación / dominio | **Observer / eventos de dominio** (`PagoAcreditado` con suscriptores independientes) **+ Unit of Work** (pago y eventos en una transacción) **+ clave de idempotencia** (Idempotent Receiver). | Observer **no sustituye** a Unit of Work: Observer desacopla el abanico de reacciones (que el correo no tumbe el alta); Unit of Work asegura que el estado del pago y la lista de eventos se guarden juntos o nada. Son dos fuerzas —acoplamiento y atomicidad— y hacen falta las dos. La idempotencia es la única que evita el segundo cargo. | Si las tres reacciones tuvieran que ser síncronas y consistentes con el pago en el mismo instante, un Observer asíncrono sería un error: ahí va un coordinador explícito. |
| 5 | La app pide un JSON mínimo (folio, saldo, plazo); el kiosco pide HTML con escudo y tabla de vencimientos; la app hace doce peticiones para pintar el inicio. | Presentación (representación) + aplicación (agregación) | **Negociación de contenido con un Presenter / DTO Assembler por cliente + Facade de lectura / BFF** que agrega en una respuesta lo que hoy son doce llamadas. | Facade y no **Adapter**: el problema de la app es la cantidad y el desmenuzamiento de llamadas; se ofrece una entrada gruesa que orquesta varias consultas internas. Adapter sería si la app ya esperara una interfaz concreta preexistente y hubiera que encajar la nuestra en esa forma. | Si ambos clientes consumieran el mismo cuerpo y no hubiera problema de N+1 llamadas: una sola representación y basta. |
| 6 | El servicio del banco y el validador de CURP se caen seguido; mientras no responden, el alumno ni siquiera puede consultar el kardex, que no depende de ellos. | Integración | **Circuit Breaker** (+ timeout + *fallback*) **+ Bulkhead** (aislar el pool del colaborador lento). | Circuit Breaker y no **Retry**: reintentar contra un servicio caído lo hunde más y alarga la rueda de espera; el *breaker* corta rápido y devuelve error o un valor de reserva. Bulkhead y no «subir el timeout»: el timeout largo es justo lo que propaga la caída a trámites que no dependen del colaborador. | Una dependencia local, rápida y fiable, o una llamada sin alternativa posible que de verdad deba bloquear. |

## Respuesta — Misión 2: `pagar la inscripción`, paso a paso

| Paso | Objeto / mecanismo | Patrón que realiza | Qué resuelve aquí |
|---|---|---|---|
| 1 | Punto de entrada único (`index.php` / kernel HTTP) recibe `POST /inscripcion/pago`. | **Front Controller** | Un solo lugar de entrada; aquí vive lo que antes se copiaba en 40 archivos. |
| 2 | Enrutador / *dispatcher* mapea verbo + ruta → `PagoInscripcionController`. | **Router** (+ el manejador se invoca como **Command**) | Añadir un trámite es registrar una ruta, no crear un archivo suelto. |
| 3 | Cadena de middlewares: sesión, caducidad de sesión, bitácora, encabezado común. | **Chain of Responsibility** | La regla de caducidad se cambia en un punto; cada eslabón deja pasar o redirige a login. |
| 4 | Middleware de idempotencia: lee el token del formulario / `Idempotency-Key` y descarta el reenvío. | **Idempotent Receiver** | El doble clic no produce un segundo cargo. |
| 5 | *Form Request* / validador: convierte el `POST` crudo en un comando tipado (monto, medio, folio). | **DTO + Validación** (Specification para las reglas) | El dominio no ve `$_POST`. |
| 6 | Servicio de aplicación `PagarInscripcion.ejecutar(comando)`; abre la unidad de trabajo. | **Application Service / Command Handler** | Un método = un caso de uso; el controlador no lleva lógica de negocio. |
| 7 | `InscripcionRepository.obtener(folio)` recupera el agregado. | **Repository** | La consulta vive aquí, no en una plantilla. |
| 8 | Agregado `Inscripcion` + `Pago` aplica la regla y transiciona `pendiente → acreditado / rechazado`. | **Domain Model + State** | El reglamento interno manda sobre el vocabulario del banco. |
| 9 | `PasarelaPagoFactory` devuelve la estrategia según el medio (tarjeta / SPEI / ventanilla). | **Factory + Strategy** | Banco nuevo = clase nueva, no editar un `switch`. |
| 10 | Adaptador del banco: traduce la petición al protocolo del colaborador y su respuesta (00/01, «créditos») a un resultado de dominio. | **Adapter / capa anticorrupción** | Aísla el vocabulario y el contrato ajenos. |
| 11 | Envoltura de resiliencia sobre la llamada externa: timeout + reintento acotado + corte. | **Circuit Breaker** | Si el banco no responde, falla rápido y no arrastra al resto del portal. |
| 12 | El agregado registra el evento `PagoAcreditado` (todavía no llama a nadie). | **Domain Event** | Separa «qué pasó» de «quién reacciona». |
| 13 | *Unit of Work* confirma en una transacción: estado del pago + fila del evento en la tabla *outbox*. | **Unit of Work + Transactional Outbox** | O se guardan pago y evento juntos, o ninguno: se acabó el «alta sin registrar». |
| 14 | Despachador de eventos (tras el *commit*) entrega `PagoAcreditado` por cola. | **Observer / Publish-Subscribe + Message Queue** | El fallo de un suscriptor no toca a los demás. |
| 15 | Suscriptores: `AltaDeMaterias` (control escolar), `NotificaciónCorreo`, `AvisoCaja`; cada uno un *handler* idempotente con su reintento. | **Observer** | El correo caído ya no impide el alta de materias. |
| 16 | Presentador de respuesta: según `Accept`, DTO JSON (folio, saldo, plazo) para la app o vista HTML con escudo y tabla de vencimientos para el kiosco. | **Content Negotiation + DTO Assembler / View** | Misma operación, dos representaciones; la app deja de hacer doce llamadas. |
| 17 | La respuesta vuelve por la cadena de middlewares; se cierra la bitácora con el resultado. | **Chain of Responsibility** (mismo pipeline) | Traza completa de la petición, de entrada a salida. |

## Explicación — la razón de las decisiones

**El portal no es «un patrón».** El enunciado insiste en ello y el análisis lo respeta: cada conflicto del relato tiene su propia fuerza dominante, y esa fuerza —no el temario— elige la estructura. Por eso la Misión 1 sale como una tabla de capas distintas y no como «esto es MVC» o «esto es hexagonal». MVC y hexagonal son el marco donde estos patrones encajan, no la respuesta a ninguno de los seis problemas.

**Por qué se razona por capas.** Ubicar cada problema en una capa (transversales, presentación, aplicación/dominio, datos, integración) obliga a nombrar *dónde* duele y evita mezclar soluciones. La duplicación del punto 1 es transversal: no se arregla en el dominio. La caída del banco del punto 6 es de integración: no se arregla con más validación. La consistencia del punto 4 es de aplicación/dominio: no se arregla con un *retry* de red. La capa es la primera pista del patrón correcto.

**Los vecinos rechazados.** El criterio «Adapter no se confunde con Facade; Observer no sustituye a Unit of Work» es la columna vertebral de las decisiones:

- *Adapter vs. Facade* (puntos 2 y 5): Adapter traduce un contrato ajeno que no controlamos (el protocolo del banco); Facade simplifica un subsistema propio (las doce consultas que la app necesita). En el punto 2 hay traducción de vocabulario → Adapter. En el punto 5 hay demasiadas llamadas finas → Facade/BFF.
- *Observer vs. Unit of Work* (punto 4): resuelven fuerzas ortogonales. Observer quita el acoplamiento entre el pago y sus tres reacciones; Unit of Work garantiza que el pago y sus eventos se persistan atómicamente. Cambiar uno por el otro deja un agujero: solo Observer no impide el «alta a medias»; solo Unit of Work vuelve a acoplar el correo con el alta.
- *Strategy vs. State* (puntos 2 y 8): en el punto 2, lo que cambia es el algoritmo elegido por un dato → Strategy. En el paso 8 de la Misión 2, lo que cambia es el ciclo de vida del pago (`pendiente/acreditado/rechazado`) → State. Coexisten sin confundirse.
- *Circuit Breaker vs. Retry* (punto 6): el *retry* solo empeora una caída; el *breaker* corta y aísla. Se acompaña de Bulkhead porque el objetivo explícito es que el kardex siga vivo aunque el banco no.
- *Repository vs. Active Record* (punto 3): con varios consumidores de la misma consulta, el SQL no puede vivir en el registro ni en la plantilla.

**El punto 7 y la sobreingeniería.** El proveedor propone Event Sourcing, CQRS, malla de microservicios y Redux global para: *autenticar, consultar un registro que ya existe y generar un PDF*. No hay ningún problema que esas herramientas resuelvan aquí: no hay historia de eventos que reconstruir, no hay asimetría lectura/escritura que justifique CQRS, no hay dominio que trocear en servicios, no hay estado de cliente que orquestar. Lo suficiente es: Front Controller + middleware de autenticación + un Repository de solo lectura + un generador de PDF. El catálogo de patrones se rechaza donde no hay fuerza que lo pida; cada patrón añadido de más es costo operativo y cognitivo permanente y difícil de revertir.

**El marco: qué no se reescribe.** Si el equipo usa Spring, Laravel o Express, la mayor parte del esqueleto viene en la caja y **no se programa**: el front controller, el enrutador, la tubería de middlewares, el contenedor de inyección, el ORM y la clase base de repositorio, el despachador de eventos, la negociación de contenido y la validación. Lo que el equipo **sí escribe** es lo propio de estos conflictos: las estrategias de pago y los adaptadores de cada banco, el modelo de dominio y su máquina de estados, los eventos y sus *handlers*, la clave de idempotencia, la configuración del *circuit breaker* y la agregación del BFF. El framework aporta la fontanería; el dominio y sus integraciones son responsabilidad del equipo.

