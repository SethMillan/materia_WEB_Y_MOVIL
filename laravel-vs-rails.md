# Laravel vs Ruby on Rails

Comparación de las ventajas que trae cada framework "de fábrica" (sin instalar nada extra) en los puntos que se pidieron: ORM, autenticación, usuarios, permisos, sesiones, validación, migraciones, seguridad, panel administrativo, middleware, manejo de URLs y pruebas.

## Tabla comparativa

| Característica | Laravel (PHP) | Ruby on Rails |
|---|---|---|
| ORM | Eloquent ORM, basado en el patrón Active Record, sintaxis muy expresiva (`User::where('activo', true)->get()`) | Active Record (le da nombre al patrón), prácticamente igual de expresivo (`User.where(activo: true)`), es el "original" en el que Eloquent se inspiró |
| Autenticación | Laravel Breeze, Jetstream, Fortify o Sanctum, kits de inicio que ya traen login, registro, recuperación de contraseña listos | Devise (gema externa pero estándar de facto) o `has_secure_password` nativo de Rails para algo más simple |
| Usuarios | Modelo `User` generado por defecto con migración y tabla `users` ya lista desde el `php artisan make:auth` o los starter kits | Igual, `rails generate scaffold User` o con Devise se genera el modelo, migración y controlador de usuarios |
| Permisos / Roles | No trae roles de fábrica, se usa el paquete Spatie Laravel-Permission (el más usado del ecosistema) | Tampoco viene nativo, se usa la gema Pundit o CanCanCan para roles y políticas de autorización |
| Sesiones | Manejo de sesiones integrado (`session()`), soporta drivers de archivo, cookie, base de datos, Redis | Manejo de sesiones integrado también, por defecto usa cookies firmadas (`ActionDispatch::Session::CookieStore`) |
| Validación | Form Requests y reglas de validación muy completas y encadenables (`'email' => 'required|email|unique:users'`) | Validaciones dentro del propio modelo (`validates :email, presence: true, uniqueness: true`), más "declarativo" |
| Migraciones | Sistema de migraciones con `php artisan migrate`, define el esquema en PHP con un DSL propio (Schema Builder) | Sistema de migraciones con `rails db:migrate`, es el que popularizó este patrón, DSL en Ruby muy limpio |
| Seguridad | Protección CSRF automática, sanitización de queries (previene SQL injection por el ORM), hashing de contraseñas con bcrypt/argon2 | Protección CSRF automática, misma prevención de SQL injection vía Active Record, `has_secure_password` usa bcrypt también |
| Panel administrativo | No trae uno propio, se usan paquetes como Filament o Nova (de pago) | Rails Admin o Active Admin, gemas externas, no viene nativo tampoco |
| Middleware | Sistema de middleware explícito y muy usado (`auth`, `throttle`, middleware personalizado en `app/Http/Middleware`) | Existen los "filters" (`before_action`, `after_action`) en los controladores, más el concepto de Rack middleware a nivel más bajo |
| Manejo de URLs | Rutas definidas en `routes/web.php` y `routes/api.php`, sintaxis clara con Route::get, Route::resource | Rutas en `config/routes.rb`, con `resources :users` genera automáticamente las 7 rutas RESTful estándar |
| Pruebas | PHPUnit y Pest integrados, feature tests y unit tests con helpers propios de Laravel | Minitest integrado por defecto, o RSpec (el más usado en la comunidad), muy orientado a TDD/BDD |

## Notas rápidas

Ambos frameworks siguen la filosofía "convención sobre configuración", por eso se parecen tanto en la estructura (MVC, migraciones, rutas RESTful, ORM tipo Active Record). Rails fue el que estableció casi todas estas convenciones desde 2004 y Laravel las adoptó y las adaptó al mundo PHP después.

La diferencia más notoria está en el ecosistema: Rails trae más cosas "casi nativas" (Active Record y las validaciones dentro del modelo, Minitest de fábrica), mientras que Laravel se apoya más en paquetes del ecosistema (Spatie, Filament, Sanctum) pero con una documentación y comunidad más grandes hoy en día.
