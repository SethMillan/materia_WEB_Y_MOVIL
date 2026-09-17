# Qué patrones usamos


## Los tres patrones que identificamos

**Adapter.** Lo usamos para traducir lo que dice cada proveedor de IA al lenguaje que entiende nuestro programa. En vez de que el resto del código tenga que saber qué es un route_hint o cómo leer un atributo vehicle de un XML, hay una clase adaptadora para cada proveedor que se encarga de esa traducción y entrega siempre el mismo tipo de objeto hacia adelante, algo así como una sugerencia con el medio de transporte y el motivo. El resto del sistema nunca se entera de si la sugerencia vino de JSON o de XML.

**Strategy.** Cada medio de transporte, bicicleta, moto, camioneta y dron, tiene sus propias reglas para calcular si el pedido cabe, cuánto tarda y cuánto cuesta. En lugar de meter todas esas reglas juntas dentro de un montón de condicionales, cada medio quedó en su propia clase con su propio método para planear la entrega. Así se puede agregar un medio nuevo sin tocar los que ya existen.

**Factory Method.** Es el que decide qué medio de transporte concreto se crea, sin que el código que orquesta todo el proceso tenga que mencionar directamente una clase como dron o bicicleta. Hay una clase base que define el trámite de despachar el pedido y dejamos que sean las clases hijas las que decidan qué medio fabricar. Así, quien arma el pedido y consulta a la IA nunca necesita conocer los nombres concretos de los medios de transporte.

Estos tres patrones trabajan juntos en una sola secuencia: primero el Adapter traduce lo que dijo la IA, después el Factory Method fabrica el medio de transporte correspondiente, y por último el Strategy calcula el plan real de la entrega.

