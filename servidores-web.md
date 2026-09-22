# Servidores WEB
En esta clase el profe ha hablado de los servidorores web en los que podemos desplegar nnuestra aplicación, asi como de las posibles complicaciones que podemos tener al momento de tratar de subir todo asi sin chiste, tambien menciono las ventajas de los contenedores sobre las maquinas virtuales y los contenedores sobre aplicaciones nativas
Nos dejo investigar sobre los frameworks Laravel, Django y Rails que servidores web tanto en local como en produccion tienen, si es que tienen o si vamos a necesitar

1. Django
Local: runserver - Servidor de desarrollo WSGI
    El comando runserve en Django inicia un servidor web local y ligero diseado unicamente para pruebas y desarrollo, permitiendo probar código web en tu computadora de forma inmediata sin configurar un servidor por completo
Producción: Gunicorn/ uWSGI + Nginx
    Es un servidor HTTP WSGI de codigo abierto para sistemas UNIX, actua como puente entre un servidor web frontal y tu aplicacion web escrita en frameworks como django o flask

2. Rails
Local: Puma
    Puma es el servidor web HTTP multiproceso y multi-hilo predeterminado para aplicaciones de Ruby o Rails, a diferencia de NGINX que es un servidor web externo, puma corre directamente dentro del entorno de RUBY para ejecutar el código de tu aplciacion de rails de forma rapida y concurrente
Producción: Puma + Nginx
    NGINX Es un servidor web de código abierto y alto rendimiento diseñado para gestionar grandes volumenes de trafico de forma eficiente, a diferencia de servidores tradicionales como Apache, utiliza una arquitectura orientada a eventos que consume muy poca memoria RAM.
3. Laravel
Local: PHP Artisan (php artisan serve)
    El comando php artisan serve es una herramient integrada de Laravel que levanta un servidor web de desarrollo local de forma inmediata
Producción: PHP-FPM+ Nginx/Apache
    Para entornos de produccion esta combinacion es el estandar absoluto de la industria para Laravel, a diferencia de la manera local, solo es para desarrollo, pgp no puede recibir peticiones web directas en produccion de forma eficiente, necesita un intermediario, el PHP-FPM significa FastCGI Process Manager, es el gestor de procesos que escucha en segundo plano
