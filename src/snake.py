from random import randint
import pygame as pg
import sys
from pygame.locals import *

pg.init()

import globals
import sounds


class Food:
    def __init__(self, walls):
        self.x_coord = randint(0, globals.WIDTH - globals.FOOD_SIDE) // 15 * 15
        self.y_coord = randint(0, globals.HEIGHT - globals.FOOD_SIDE) // 15 * 15
        while (self.x_coord, self.y_coord, 15, 15) in walls:
            self.x_coord = randint(0,
                                   globals.WIDTH - globals.FOOD_SIDE) // 15 * 15
            self.y_coord = randint(0,
                                   globals.HEIGHT - globals.FOOD_SIDE) // 15 * 15

    def draw_food(self):
        pg.draw.rect(
            DISPLAY_SURFACE, globals.GREEN,
            (self.x_coord, self.y_coord, globals.FOOD_SIDE, globals.FOOD_SIDE))


class Score:
    def __init__(self):
        self.points = 0
        self.record = 0

    def draw_score(self):
        score_text = globals.font_style.render(f'Score: {self.points}',
                                               True, globals.BLUE)
        record_text = globals.font_style.render(f'Your record: {self.record}',
                                               True, globals.BLUE)
        my_file = open("records.txt", 'r')
        cur_record = int(my_file.readline())
        my_file.close()
        if self.points > cur_record:
            my_file = open("records.txt", 'w')
            my_file.write(str(self.points))
            my_file.close()
        score_tablet = score_text.get_rect()
        record_tablet = record_text.get_rect()
        score_tablet.topleft = (5, 5)
        record_tablet.topleft = (5, 30)
        DISPLAY_SURFACE.blit(score_text, score_tablet)
        DISPLAY_SURFACE.blit(record_text, record_tablet)


class Snake:
    def __init__(self):
        self.blocks = [(globals.x_center, globals.y_center)]

    def draw_snake(self):
        for snake_x, snake_y in self.blocks:
            pg.draw.rect(
                DISPLAY_SURFACE, globals.RED,
                (snake_x, snake_y, globals.SNAKE_BLOCK, globals.SNAKE_BLOCK))


class Walls:
    def __init__(self):
        self.all_walls = []

    def generate_walls(self):
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
        DISPLAY_SURFACE.fill(globals.BLUE_BACKGROUND)
        for wall in self.all_walls:
            pg.draw.rect(DISPLAY_SURFACE, globals.BLACK, wall)
        for x in range(0, globals.WIDTH, 15):
            pg.draw.line(
                DISPLAY_SURFACE, globals.WHITE, (x, 0), (x, globals.HEIGHT))
        for y in range(0, globals.HEIGHT, 15):
            pg.draw.line(
                DISPLAY_SURFACE, globals.WHITE, (0, y), (globals.WIDTH, y))


def game_over():
    DISPLAY_SURFACE.blit(globals.game_over_text, globals.game_over_tablet)
    DISPLAY_SURFACE.blit(globals.play_or_quit_text, globals.play_or_quit_tablet)
    sounds.background_sound.stop()
    sounds.eating_food_sound.stop()
    sounds.game_over_sound.play()
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    pg.quit()
                    quit()
                elif event.key == K_p:
                    main_game()


def choose_speed():
    while True:
        DISPLAY_SURFACE.fill(globals.BLUE_BACKGROUND)
        DISPLAY_SURFACE.blit(globals.choose_speed_text_1,
                             globals.choose_speed_tablet_1)
        DISPLAY_SURFACE.blit(globals.choose_speed_text_2,
                             globals.choose_speed_tablet_2)
        DISPLAY_SURFACE.blit(globals.choose_speed_text_3,
                             globals.choose_speed_tablet_3)
        DISPLAY_SURFACE.blit(globals.choose_speed_text_4,
                             globals.choose_speed_tablet_4)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    return globals.SPEED - 5
                if event.key == pg.K_2:
                    return globals.SPEED
                if event.key == pg.K_3:
                    return globals.SPEED + 5
            if event.type == pg.QUIT:
                pg.quit()
                quit()


def main_game():
    # set background sound and choose speed
    sounds.game_over_sound.stop()
    sounds.background_sound.play(loops=-1)
    SPEED = choose_speed()

    # generate food and walls
    walls = Walls()
    walls.generate_walls()
    food_1 = Food(walls.all_walls)
    food_2 = Food(walls.all_walls)
    food_3 = Food(walls.all_walls)
    score = Score()
    my_file = open("records.txt", 'r')
    score.record = int(my_file.readline())
    my_file.close()

    # initialize snake
    snake = Snake()
    x_speed = y_speed = 0

    def can_move(x, y):
        for (x_start, y_start, width, height) in walls.all_walls:
            if x_start <= x <= x_start + width - 15\
                    and y_start <= y <= y_start + height - 15:
                return False

        return bool(x >= 0 and x + globals.SNAKE_BLOCK <= globals.WIDTH
                    and y >= 0 and y + globals.SNAKE_BLOCK <= globals.HEIGHT
                    and (x, y) not in snake.blocks)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key in globals.KEY_ACTIONS:
                    x_new, y_new = globals.KEY_ACTIONS[event.key]
                    if x_speed == 0 and y_speed == 0 or\
                            x_new + x_speed != 0 and y_new + y_speed != 0:
                        x_speed, y_speed = x_new, y_new

        if x_speed != 0 or y_speed != 0:
            new_head_x, new_head_y = snake.blocks[-1]
            new_head_x += x_speed
            new_head_y += y_speed

            if can_move(new_head_x, new_head_y):
                snake.blocks.append((new_head_x, new_head_y))
            else:
                game_over()

            if new_head_x == food_1.x_coord and new_head_y == food_1.y_coord:
                food_1 = Food(walls.all_walls)
                sounds.eating_food_sound.stop()
                sounds.eating_food_sound.play()
                score.points += 1
                score.record = max(score.record, score.points)
                x_speed *= -1
                y_speed *= -1
                snake.blocks = snake.blocks[::-1]
            elif new_head_x == food_2.x_coord and new_head_y == food_2.y_coord:
                food_2 = Food(walls.all_walls)
                sounds.eating_food_sound.stop()
                sounds.eating_food_sound.play()
                score.points += 1
                score.record = max(score.record, score.points)
                x_speed *= -1
                y_speed *= -1
                snake.blocks = snake.blocks[::-1]
            elif new_head_x == food_3.x_coord and new_head_y == food_3.y_coord:
                food_3 = Food(walls.all_walls)
                sounds.eating_food_sound.stop()
                sounds.eating_food_sound.play()
                score.points += 1
                score.record = max(score.record, score.points)
                x_speed *= -1
                y_speed *= -1
                snake.blocks = snake.blocks[::-1]
            else:
                snake.blocks.pop(0)

        walls.draw_background()
        food_1.draw_food()
        food_2.draw_food()
        food_3.draw_food()
        snake.draw_snake()
        score.draw_score()

        pg.display.update()
        FPS_CLOCK.tick(SPEED)


# initialize display and clock
DISPLAY_SURFACE = pg.display.set_mode((globals.WIDTH, globals.HEIGHT))
pg.display.set_caption("Snake")
FPS_CLOCK = pg.time.Clock()
main_game()