Seth Ricardo Millan Davalos
Ricardo Urbina
Carlos
Flavio Garcia

1. La ruta de las computadoras
Nota: Se ve asi porque uso una terminal con diseño personalizado pero arrojo correctamente la ruta
 plataforma-entregas  python -c "import sys; print(sys.prefix)"
C:\Users\milla\OneDrive - Instituto Tecnológico de Morelia\TECNOLOGICO DE MORELIA\9no SEMESTRE\Proyectos - Semestre\plataforma-entregas\.venv
 milla   plataforma-entregas   main ≡     
2. Una cotizacion que entrega datos
Se agrego la ruta y las reglas en otro archivo, en este caso podemos usar Strategy, al ser una practica sencilla y corta considere que seria aunmentar en gran medida la complejidad de la aplicacion y en las instrucciones no mencionaba implementarlo
    1. La validacion tiene que estar en el backend por que no se puede confiar que todos los clientes validen correctamente sus datos, aunque la app movil revise que km no este vacio, alguien podria ingresar con la api
    2. El patron es estrategy, tendriamos una mejor escalabilidad a futuro en caso de que la complejidad del sistema aumente
3. Dos clientes, un solo backend
Si la regla hubiera estado en el JS de la pagina, el cliente habria funcionado solamente en la pagina, al introducir datos incorrectos en la aplicacion movil por ejemplo, nos arrojaria un error, por eso es conveniente validar tambien los datos en backend
4. No tengo docker pero si quiero hacerlo despuecito
5. Casos para pensar señores, sin codigo
    1. No deberia cambiarlo directamnte porque la aplicacion movil existe para recibir un campo con nombre especifico, al cambiar nombre, las versiones actuales de la app podrian dejar de funconar, lo correcto seria agregar medios como posible respuesta para despues utilizar medios y eliminar medios_disponibles
    2. El mensaje podria enviarse cinco veces a cada repartidor, ese trabajo deberia manejarlo un sistema de tareas programadas, algo como un worker quiza
    3. Cuando el contenedor se reinicia es probable que se borren las fotos, al ser archivos efimeros los que viven en contenedores
    4. El entorno virtual sirve para el trabajo iario de desarrollo, permite aislar dependencias, paquetes y ejecutar django sin afectar el python global, docker en cambio es para empaquetar y ejecutar aplicaciones con su entorno de ejecucion, facilitando que funcione de manera consistente en diferentes maquinas
    5. Investigando un poco encontre que podria ser un problema de idempotencia, haciendo que tengamos un identificador unico para caa operacion de pago, el backend verifica si ya fue procesada la informacion y si lo fue, no la vuelve a realizar