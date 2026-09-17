# Revisión de los cinco proyectos

## Cinerex (cine, Django)

Este es un sistema para comprar boletos de cine. El login mete directo lo que escribe el usuario dentro de la consulta a la base de datos, así que con un poco de maña cualquiera puede entrar sin contraseña o sacar información que no le toca. Además existe una cookie llamada admin_bypass, y basta con crearla tú mismo en el navegador para que el sistema te deje pasar como si fueras del staff. La cartelera arma el HTML pegando texto a mano con los datos que vienen de la base y lo manda a pantalla marcado como seguro, entonces si el título de una película trae código metido, ese código corre en el navegador de quien lo vea. Cuando alguien compra un boleto, el sistema guarda el boleto, marca el asiento y regala una cortesía de dulces en tres pasos separados, y si algo falla a medias puede quedar el boleto pagado con el asiento libre, o al revés. También dejaron viva una ruta vieja, funcion_old, que regresa toda la información de los asientos sin pedir sesión ni nada. Y hay un archivo, cadena.py, pensado para filtrar las peticiones que nunca conectaron en la configuración, así que ahorita no hace absolutamente nada. La documentación de arquitectura que traen habla de un sistema portuario de contenedores y ni siquiera menciona el cine, así que tampoco sirve de guía.

| Patrón | Para qué serviría aquí |
| --- | --- |
| Repository | Juntar todas las consultas en un solo lugar y usar parámetros en vez de pegar texto, así se tapa la inyección |
| Service o caso de uso | Sacar la lógica de comprar boleto del view y meterla en una transacción real |
| Strategy | Manejar el precio por tipo de boleto y la forma de pago con clases separadas en vez de una fila larga de if |
| Middleware de autenticación | Usar el sistema de sesiones de Django de verdad, o terminar y conectar la cadena que empezaron en cadena.py |
| Adapter para el banco | Aislar la llamada al banco y el armado del XML en una clase aparte, para poder ponerle tiempo de espera |

## Hotel Luna (Spring)

Aquí el problema empieza desde la contraseña de la base de datos, escrita tal cual en el archivo de configuración, con el usuario root. El login compara la clave del empleado directo contra lo guardado en la tabla, sin ningún cifrado, y esa misma consulta se arma pegando el texto que llega del formulario, así que otra vez cualquiera puede meter algo raro y saltarse el login. Aparece la misma cookie admin_bypass que vimos en el cine, basta con crearla para entrar como gerente. Las pantallas de facturas usan una forma de Thymeleaf que no escapa el HTML, entonces datos guardados por un huésped podrían convertirse en código que corre en el navegador de otro usuario. Cuando alguien hace una reservación, el sistema cobra, guarda la reservación, marca la habitación ocupada y regala una cortesía de spa en pasos separados sin ninguna transacción, y ni siquiera relaciona la reservación con una habitación específica, nada más marca cualquier habitación de ese tipo como ocupada. Lo más raro es que además de los controladores normales de Spring, metieron un servlet propio que se registra para todas las rutas, mientras el documento de arquitectura del proyecto dice claro que ese servlet está prohibido. Y esa misma documentación, en otra parte, describe un sistema de inventario tipo NASA con racks y SKU, que tampoco tiene nada que ver con un hotel.

| Patrón | Para qué serviría aquí |
| --- | --- |
| Service Layer | Mover la reserva, el pago y el correo fuera del controlador, todo dentro de una transacción |
| Repository | Reemplazar el JdbcTemplate suelto en cada clase por consultas centralizadas y con parámetros |
| Strategy | Calcular el precio por tipo de habitación con clases o una tabla de tarifas, no con una cadena de if |
| Máquina de estados | Controlar los pasos válidos de una reservación, pagada, checkin, cancelada, para no saltarse ninguno |
| Gateway al banco | Sacar la llamada de pago del controlador y ponerla en una clase aparte con tiempo de espera y manejo de errores |

La verdad, entre el servlet propio peleando con Spring y la documentación que habla de un sistema totalmente distinto, conviene más sentarse a levantar el proyecto de nuevo con una sola forma de manejar las rutas, en lugar de seguir parchando lo que ya está.

## Pasofit (Flutter)

Esta aplicación de ejercicio guarda casi toda su lógica dentro de las pantallas mismas. Cada pantalla abre su propia conexión a la base local y arma el SQL pegando el texto directo, sin usar parámetros, algo que en una base local pesa menos pero de todas formas es una costumbre peligrosa. El login manda el usuario y la contraseña a un servicio interno y, si la respuesta trae la palabra ok o id en cualquier parte del texto, te deja entrar sin checar nada más. Ya adentro, la pantalla de inicio revisa si de verdad se autenticó, pero el código literalmente no hace nada con esa revisión, hasta trae un comentario que dice a veces entra igual, o sea que el chequeo existe nomás de adorno. El cronómetro arranca un timer que nunca se detiene cuando cierras la pantalla, y usa una lista de funciones sueltas para avisar el segundero, en vez del manejador de estado que ya trae instalado el proyecto, el cual por cierto está en el pubspec pero nunca se usa en ningún lado. Los logros se calculan repitiendo una consulta por cada ejercicio pendiente, y esos pendientes nunca se borran, entonces con el tiempo el cálculo se vuelve más lento y menos exacto. Lo curioso es que el documento de arquitectura de este proyecto dice, con todas sus letras, que está prohibido usar listas de funciones sueltas para avisos y que hay que usar el manejador de estado instalado, justo lo contrario de lo que se hizo.

| Patrón | Para qué serviría aquí |
| --- | --- |
| BLoC o Cubit | Usar de verdad el manejador de estado ya instalado en vez de la lista de funciones sueltas |
| Repository | Meter todo el acceso a la base local en una sola clase, separada de las pantallas, con consultas parametrizadas |
| Observer bien hecho | Reemplazar los buses de aviso por streams o notifiers que sí se dan de baja cuando la pantalla se cierra |
| Guard de navegación | Revisar el permiso de entrada antes de construir la pantalla, no nada más leerlo y dejar pasar de todas formas |
| State machine simple | Controlar el ciclo de una rutina, iniciada, guardada, con logro, para no repetir cálculos ni duplicar registros |

El chequeo de acceso que no bloquea nada y el manejador de estado instalado que nunca se usa dan la impresión de que el proyecto se fue armando a prueba y error sin ninguna metodología fija. Antes de seguir agregando pantallas valdría la pena decidir de una vez cómo se maneja el estado y el acceso a datos.

## Sabores (Laravel)

Este es un sistema de pedidos de comida y mezcla dos formas distintas de resolver lo mismo. Por un lado están las rutas normales de Laravel en web.php, y por otro hay una clase FrontController que vuelve a decidir a mano qué controlador llamar según el texto de la ruta, cosa que Laravel ya hace solo. El login pega el correo y la clave directo en la consulta, y vuelve a aparecer la cookie admin_bypass, basta con crearla para entrar como administrador. Al guardar un pedido, el número de tarjeta se manda tal cual dentro de un texto XML hacia la pasarela de pago, sin ningún cuidado especial para ese dato. Después de guardar el pedido, el folio se saca pidiendo el máximo id de la tabla en una consulta aparte, así que si dos personas pagan al mismo tiempo los folios se pueden cruzar. La vista de reportes, en vez de usar el mismo motor de base de datos que el resto del proyecto, abre su propia conexión con mysqli, con el usuario y la contraseña escritos ahí mismo, y hace una consulta por cada pedido nada más para buscar el nombre del cliente. La vista de reseñas hace lo mismo con otra conexión aparte, y encima imprime el texto de la reseña sin ningún escape, así que un comentario con código adentro correría para todos los que lo vean. El documento que traen de arquitectura dice que este repositorio es un censo de ganado del gobierno estatal y que los pedidos en realidad son traslados de reses, lo cual no tiene ninguna relación con lo que hace el código.

| Patrón | Para qué serviría aquí |
| --- | --- |
| Repository | Sacar las consultas sueltas y las conexiones manuales de mysqli, y centralizar el acceso con Eloquent |
| Front controller único | Quitar la clase FrontController hecha a mano y dejar que solo las rutas de Laravel decidan qué controlador entra |
| Service Layer | Mover el cálculo del pedido y el cobro fuera del controlador, en una clase que maneje la transacción completa |
| Strategy de pago | Separar cada forma de pago en su propia clase en vez de la cadena larga de if para efectivo, tarjeta, vale y puntos |
| Adapter para la pasarela | Aislar el armado del XML y el envío a la pasarela en una clase propia, para no mandar el número de tarjeta suelto |

Entre las dos formas de manejar rutas, las conexiones manuales a la base regadas en las vistas y el documento que dice que esto es un sistema de ganado, la verdad conviene más levantar el proyecto de nuevo siguiendo la estructura normal de Laravel que seguir arreglando parche por parche.

## Tallerpro (Express)

Este proyecto de taller mecánico sí trae una cadena de responsabilidad que funciona de verdad, el archivo Handler.js encadena un paso de autenticación, uno de bitácora y al final el cobro de la orden, y se usa así en la ruta para abrir una orden nueva. El problema es que ese cuidado no se aplicó en el resto de las rutas. Por ejemplo, la ruta para marcar una orden como entregada y la de ver el inventario no piden ninguna sesión ni cookie, cualquiera que conozca la dirección puede usarlas sin haber iniciado nada. El login pega el correo y la clave directo en la consulta SQL, y la sesión se protege con un secreto que literalmente es la palabra password. La cookie admin_bypass reaparece aquí también. Cuando se cobra una orden, se guarda la orden, se actualiza el inventario de refacciones y se marca ocupado al mecánico en consultas separadas sin transacción, así que una falla a medias puede dejar a un mecánico marcado como ocupado para siempre, o una orden pagada sin descontar refacciones. El documento de este proyecto dice que en realidad es el sistema de una clínica dental y que está prohibido usar clases para la cadena de responsabilidad, justo lo que sí se hizo bien en este proyecto.

| Patrón | Para qué serviría aquí |
| --- | --- |
| Middleware de autenticación | Aplicar el mismo chequeo de sesión a todas las rutas, no nada más a la de abrir una orden nueva |
| Repository | Juntar las consultas SQL en un solo lugar con parámetros, en vez de pegar el texto directo en cada ruta |
| Service Layer | Meter el cobro, la actualización de inventario y la del mecánico dentro de una sola transacción |
| Strategy de pago | Separar caja, tarjeta y crédito del cliente en clases distintas en vez de la cadena de if actual |
| Unit of Work | Asegurar que las tres actualizaciones de una orden se confirmen juntas o ninguna se quede a medias |
