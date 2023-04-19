from random import randint
import pygame as pg
import globals


class Food:
    def __init__(self, walls):
        """set the coordinates of the food.
        Args:
            self (Food):  an instance of the class.
            walls (list): array of wall blocks.
        Returns:
            None.
        """
        self.x_coord = randint(0, globals.WIDTH - globals.FOOD_SIDE) // 15 * 15
        self.y_coord = randint(0, globals.HEIGHT - globals.FOOD_SIDE) // 15 * 15
        while (self.x_coord, self.y_coord, 15, 15) in walls:
            self.x_coord = randint(0,
                                   globals.WIDTH - globals.FOOD_SIDE) // 15 * 15
            self.y_coord = randint(0,
                                   globals.HEIGHT - globals.FOOD_SIDE) // 15 * 15

    def draw_food(self):
        """reflects the food instance on the screen.
        Args:
            self (Food):  an instance of the class.
        Returns:
            None.
        """
        pg.draw.rect(
            globals.DISPLAY_SURFACE, globals.GREEN,
            (self.x_coord, self.y_coord, globals.FOOD_SIDE, globals.FOOD_SIDE))