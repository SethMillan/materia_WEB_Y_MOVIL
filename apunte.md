2.1 El caso de estudio: FeriaPPT
A lo largo de la unidad se emplea una sola aplicacion de dominio, FeriaPPT a fin de no cambiar el empleo den cada patron. El dominio es el juego de piedra, papel o tijera:
- El jugador y el rival eligen, cada uno, una de tres tiradas.
- Las reglas de victoria son fijas: el papel cubre la piedra, la piedra rompe la tijera, la tijera corta el papel, si coincide hay empate.
- El sistema administra ichas, el estado de a ronda, un ranking y la compra de vidas extra.

Ese dominio es independientemente de la plataforma. La variante web se ejecuta en el navegador y se comunica con un servidor HTTP (persistencia, ranking, pagos). La variante móvil se ejecuta en un dispositivo con ciclo propio de vida propio y, con frecuencia, conectividad intermitente; las tiradas deben poder persistirse en local y sincronizarse despues.
Las reglas del duelo no cambiam. Cambian las restricciones de la plataforma (HTTP sin estado, latencia, ciclo de vida del sistema operativo, bateria). Los patrones de cada parte de la unidad se analizan sobre esas restricciones, no como ornamento del diagrama.t