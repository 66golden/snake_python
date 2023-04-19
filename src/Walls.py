from random import randint
import pygame as pg
import globals


class Walls:
    def __init__(self):
        """initialises the walls.
        Args:
            self (Walls):  an instance of the class.
        Returns:
            None.
        """
        self.all_walls = []

    def generate_walls(self):
        """generates walls on the playing field.
        Args:
            self (Walls):  an instance of the class.
        Returns:
            None.
        """
        amount_of_walls = randint(4, 10)
        for i in range(amount_of_walls):
            is_vertical = bool(randint(0, 1))
            if is_vertical:
                x = randint(0, globals.WIDTH) // 15 * 15
                while x == globals.x_center:
                    x = randint(0, globals.WIDTH) // 15 * 15
                y_start = randint(0, globals.HEIGHT) // 15 * 15
                y_end = randint(y_start + 15, globals.HEIGHT) // 15 * 15
                while y_start != y_end:
                    wall = (x, y_start, 15, 15)
                    self.all_walls.append(wall)
                    y_start += 15
            else:
                x_start = randint(0, globals.WIDTH) // 15 * 15
                x_end = randint(x_start + 15, globals.WIDTH) // 15 * 15
                y = randint(0, globals.HEIGHT) // 15 * 15
                while y == globals.y_center:
                    y = randint(0, globals.HEIGHT) // 15 * 15
                while x_start != x_end:
                    wall = (x_start, y, 15, 15)
                    self.all_walls.append(wall)
                    x_start += 15

    def draw_background(self):
        """draws the game background and walls on the playing field.
        Args:
            self (Walls):  an instance of the class.
        Returns:
            None.
        """
        globals.DISPLAY_SURFACE.fill(globals.BLUE_BACKGROUND)
        for wall in self.all_walls:
            pg.draw.rect(globals.DISPLAY_SURFACE, globals.BLACK, wall)
        for x in range(0, globals.WIDTH, 15):
            pg.draw.line(
                globals.DISPLAY_SURFACE, globals.WHITE, (x, 0), (x, globals.HEIGHT))
        for y in range(0, globals.HEIGHT, 15):
            pg.draw.line(
                globals.DISPLAY_SURFACE, globals.WHITE, (0, y), (globals.WIDTH, y))