import pygame as pg
import globals


class Snake:
    def __init__(self):
        """sets the initial position and speed of the snake.
        Args:
            self (Snake):  an instance of the class.
        Returns:
            None.
        """
        self.blocks = [(globals.x_center, globals.y_center)]
        self.x_speed = 0
        self.y_speed = 0

    def draw_snake(self):
        """reflects the snake instance on the screen.
        Args:
            self (Snake):  an instance of the class.
        Returns:
            None.
        """
        for snake_x, snake_y in self.blocks:
            pg.draw.rect(
                globals.DISPLAY_SURFACE, globals.RED,
                (snake_x, snake_y, globals.SNAKE_BLOCK, globals.SNAKE_BLOCK))