import tkinter as tk  # Biblioteca para crear interfaces gráficas de usuario (GUIs).
import random  # Biblioteca para generar valores aleatorios.


class SnakeGame:
    """
    Clase principal que define el juego de la serpiente.
    Contiene toda la lógica para el movimiento de la serpiente, generación de comida, colisiones,
    control de vidas, y reinicio del juego.
    """

    def __init__(self, master):
        """
        Constructor de la clase SnakeGame.

        Args:
            master (tk.Tk): Ventana principal del juego.
        """
        # Ventana principal
        self.master = master
        self.master.title("Snake Game")  # Título de la ventana.

        # Área de juego (canvas)
        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")  # Área donde se dibuja el juego.
        self.canvas.pack()  # Muestra el canvas en la ventana.

        # Variables del juego
        self.snake = [(20, 20)]  # Lista de tuplas que representa las posiciones de la serpiente.
        self.snake_direction = "Right"  # Dirección inicial de la serpiente.
        self.food_position = self.create_food()  # Genera la posición inicial de la comida.
        self.game_over = False  # Indica si el juego ha terminado.
        self.lives = 3  # Cantidad inicial de vidas del jugador.

        # Enlaza las teclas del teclado con la función de cambio de dirección.
        self.master.bind("<Key>", self.change_direction)

        # Crear botón para iniciar el juego
        self.start_button = tk.Button(self.master, text="Iniciar Juego", command=self.start_game, font=("Arial", 14))
        self.start_button.place(x=140, y=160)  # Posición del botón de inicio.

    def create_food(self):
        """
        Genera una nueva posición aleatoria para la comida dentro de los límites del área de juego.

        Returns:
            tuple: Coordenadas (x, y) de la comida.
        """
        x = random.randint(0, 19) * 20  # Coordenada X múltiplo de 20.
        y = random.randint(0, 19) * 20  # Coordenada Y múltiplo de 20.
        return x, y

    def move_snake(self):
        """
        Controla el movimiento continuo de la serpiente. Calcula la nueva posición
        de la cabeza, verifica colisiones, y redibuja los objetos en el canvas.
        """
        if self.game_over:
            return  # Si el juego ha terminado, detiene el movimiento.

        # Calcula la nueva posición de la cabeza de la serpiente.
        head_x, head_y = self.snake[0]
        if self.snake_direction == "Right":
            new_head = (head_x + 20, head_y)
        elif self.snake_direction == "Left":
            new_head = (head_x - 20, head_y)
        elif self.snake_direction == "Up":
            new_head = (head_x, head_y - 20)
        elif self.snake_direction == "Down":
            new_head = (head_x, head_y + 20)

        self.snake.insert(0, new_head)  # Añade la nueva posición al inicio de la lista.

        # Verifica si la serpiente ha comido comida.
        if new_head == self.food_position:
            self.food_position = self.create_food()  # Genera nueva comida.
        else:
            self.snake.pop()  # Si no comió, elimina el último segmento.

        self.check_collisions()  # Verifica si la serpiente colisionó.
        self.draw_objects()  # Redibuja los objetos en el canvas.
        self.master.after(100, self.move_snake)  # Programa el próximo movimiento en 100 ms.

    def change_direction(self, event):
        """
        Cambia la dirección de movimiento de la serpiente según la tecla presionada.

        Args:
            event (tk.Event): Evento del teclado que contiene la tecla presionada.
        """
        new_direction = event.keysym  # Dirección basada en la tecla presionada.
        all_directions = ("Up", "Down", "Left", "Right")  # Direcciones válidas.
        opposites = ({"Up", "Down"}, {"Left", "Right"})  # Direcciones opuestas.
        if (new_direction in all_directions and
                {new_direction, self.snake_direction} not in opposites):
            self.snake_direction = new_direction

    def check_collisions(self):
        """
        Verifica si la serpiente ha colisionado con los bordes del área de juego o consigo misma.
        Reduce vidas si ocurre una colisión y termina el juego si no quedan vidas.
        """
        head_x, head_y = self.snake[0]
        # Colisiones con bordes.
        if (head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or
                len(self.snake) != len(set(self.snake))):  # Colisión consigo misma.
            self.lives -= 1  # Reduce una vida.
            if self.lives > 0:
                self.reset_game()  # Reinicia el juego si quedan vidas.
            else:
                self.game_over = True  # Indica que el juego terminó.
                self.show_game_over()  # Muestra el mensaje de Game Over.

    def draw_objects(self):
        """
        Dibuja los objetos del juego (serpiente, comida, vidas) en el canvas.
        """
        self.canvas.delete(tk.ALL)  # Limpia el canvas.

        # Dibuja la serpiente.
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green")

        # Dibuja la comida.
        food_x, food_y = self.food_position
        self.canvas.create_oval(food_x, food_y, food_x + 20, food_y + 20, fill="red")

        # Dibuja las vidas como corazones.
        hearts = "❤️" * self.lives
        self.canvas.create_text(50, 10, text=f"Lives: {hearts}", fill="white", font=("Arial", 14), anchor="nw")

    def reset_game(self):
        """
        Reinicia el estado del juego sin modificar el número de vidas.
        """
        self.snake = [(20, 20)]  # Reinicia la posición de la serpiente.
        self.snake_direction = "Right"  # Restablece la dirección inicial.
        self.food_position = self.create_food()  # Genera nueva comida.
        self.game_over = False  # Indica que el juego no ha terminado.

    def show_game_over(self):
        """
        Muestra un mensaje de "GAME OVER" en el centro del canvas y un mensaje de "Perdiste" antes del botón
        para reiniciar el juego.
        """
        # Mensaje de GAME OVER
        self.canvas.create_text(200, 150, text="GAME OVER", fill="red", font=("Arial", 36, "bold"))

        # Mensaje de 'Perdiste'
        self.canvas.create_text(200, 200, text="Perdiste todas las vidas", fill="white", font=("Arial", 16, "bold"))

        # Botón para reiniciar el juego
        self.restart_button = tk.Button(self.master, text="Reiniciar", command=self.restart_game, font=("Arial", 14))
        self.restart_button.place(x=160, y=250)  # Posición del botón de reinicio.

    def restart_game(self):
        """
        Reinicia completamente el juego, incluyendo las vidas, y elimina el botón de reinicio.
        """
        self.lives = 3  # Restablece las vidas.
        self.reset_game()  # Reinicia el estado del juego.
        self.restart_button.destroy()  # Elimina el botón de reinicio.
        self.move_snake()  # Reanuda el movimiento de la serpiente.

    def start_game(self):
        """
        Inicia el juego al eliminar el botón de inicio y comenzar el movimiento de la serpiente.
        """
        self.start_button.destroy()  # Elimina el botón de inicio.
        self.move_snake()  # Comienza el movimiento de la serpiente.


def main():
    """
    Función principal que inicializa la ventana y el juego.
    """
    root = tk.Tk()  # Crea la ventana principal.
    game = SnakeGame(root)  # Instancia el juego.
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica.


# Ejecuta la función principal si se ejecuta directamente el script.
if __name__ == "__main__":
    main()
