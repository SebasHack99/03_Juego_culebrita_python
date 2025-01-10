Juego de la Serpiente (Snake Game) en Python
Este es un juego clásico de la serpiente (Snake Game), implementado en Python utilizando la biblioteca tkinter para la interfaz gráfica de usuario. El jugador controla la serpiente que debe comer la comida (representada por un círculo rojo) y evitar las colisiones con los bordes de la pantalla o con su propio cuerpo. El objetivo es lograr la mayor longitud posible sin perder todas las vidas.

Tecnologías Usadas
Python: Lenguaje de programación principal.
tkinter: Biblioteca estándar de Python para crear interfaces gráficas de usuario (GUIs).
random: Biblioteca estándar de Python para generar posiciones aleatorias para la comida.
Características del Juego
La serpiente se mueve en una cuadrícula.
El jugador tiene 3 vidas. Si la serpiente se choca con los bordes o consigo misma, pierde una vida.
Cada vez que la serpiente come la comida, su longitud aumenta.
Al perder todas las vidas, se muestra un mensaje de "Game Over" y un botón para reiniciar el juego.
Instrucciones
Mover la serpiente: Usa las teclas de flecha (↑, ↓, ←, →) para controlar la dirección de la serpiente.
Objetivo: Comer la mayor cantidad de comida posible sin chocar contra los bordes ni contra el cuerpo de la serpiente.
Reiniciar el juego: Si pierdes todas las vidas, haz clic en el botón "Reiniciar" para comenzar nuevamente.
Cómo ejecutar el juego
Para jugar, asegúrate de tener Python instalado en tu máquina. Luego, simplemente ejecuta el siguiente comando en tu terminal:

bash
Copiar código
python snake_game.py
Esto abrirá una ventana con el juego y podrás comenzar a jugar.

Descripción del Código
El código está basado en una clase SnakeGame, que encapsula toda la lógica del juego. Incluye funciones para el movimiento de la serpiente, la generación de comida, la detección de colisiones, la gestión de vidas, y el reinicio del juego. La interfaz gráfica se crea con la biblioteca tkinter, que proporciona una ventana con un canvas para dibujar la serpiente, la comida y el puntaje.

Métodos Principales:
move_snake(): Mueve la serpiente en la dirección deseada y verifica si ha comido la comida o si ha colisionado.
change_direction(event): Cambia la dirección de la serpiente según la tecla presionada.
check_collisions(): Verifica si la serpiente ha colisionado con los bordes o consigo misma.
draw_objects(): Redibuja la serpiente, la comida y las vidas en el canvas.
reset_game(): Reinicia el estado del juego sin modificar las vidas.
show_game_over(): Muestra el mensaje de "Game Over" y el botón para reiniciar el juego.
Dependencias
El proyecto utiliza la biblioteca estándar de Python, por lo que no es necesario instalar paquetes adicionales.

Licencia
Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo de acuerdo con los términos de esta licencia.

Este README.md proporciona una descripción clara del juego, las tecnologías utilizadas, y las instrucciones para ejecutar el juego. ¡Espero que te sea útil para tu repositorio!
