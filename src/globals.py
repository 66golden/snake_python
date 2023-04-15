import pygame as pg
import os

file_path = "./records.txt"
if not os.access(file_path, os.F_OK):
    my_file = open("records.txt", 'w')
    my_file.write(str(0))
    my_file.close()

# define colors
WHITE = (220, 220, 220)
GREEN = (0, 158, 0)
RED = (185, 0, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
BLUE_BACKGROUND = (0, 180, 210)

# define display size and block size and speed
WIDTH, HEIGHT = 705, 795
SNAKE_BLOCK = 15
FOOD_SIDE = 15
SPEED = 15

# coordinates
x_center = 345
y_center = 390

# define texts
GAME_OVER_FONT_SIZE = 40
GAME_FONT_SIZE = 24

game_over_font = pg.font.Font('freesansbold.ttf', GAME_OVER_FONT_SIZE)
game_over_text = game_over_font.render('GAME OVER', True, RED)
game_over_tablet = game_over_text.get_rect()
game_over_tablet.center = (WIDTH // 2, HEIGHT // 2)

play_or_quit_text = game_over_font.render('Q - QUIT, P - PLAY', True, RED)
play_or_quit_tablet = play_or_quit_text.get_rect()
play_or_quit_tablet.center = (WIDTH // 2, HEIGHT // 2 + GAME_OVER_FONT_SIZE + 5)

choose_speed_font = pg.font.Font('freesansbold.ttf', GAME_FONT_SIZE)
choose_speed_text_1 = choose_speed_font.render("Select the difficulty of the game.", True, YELLOW)
choose_speed_text_2 = choose_speed_font.render("Press 1, for difficulty easy.", True, YELLOW)
choose_speed_text_3 = choose_speed_font.render("Press 2, for difficulty medium.", True, YELLOW)
choose_speed_text_4 = choose_speed_font.render("Press 3, for difficulty hard.", True, YELLOW)
choose_speed_tablet_1 = choose_speed_text_1.get_rect()
choose_speed_tablet_2 = choose_speed_text_2.get_rect()
choose_speed_tablet_3 = choose_speed_text_3.get_rect()
choose_speed_tablet_4 = choose_speed_text_4.get_rect()
choose_speed_tablet_1.center = (WIDTH // 2, HEIGHT // 3)
choose_speed_tablet_2.center = (WIDTH // 2, HEIGHT // 3 + GAME_FONT_SIZE + 5)
choose_speed_tablet_3.center = (WIDTH // 2, HEIGHT // 3 + 2 * (GAME_FONT_SIZE + 5))
choose_speed_tablet_4.center = (WIDTH // 2, HEIGHT // 3 + 3 * (GAME_FONT_SIZE + 5))

font_style = pg.font.Font('freesansbold.ttf', GAME_FONT_SIZE)

# define key actions
KEY_ACTIONS = {
    pg.K_LEFT: (-SPEED, 0),
    pg.K_RIGHT: (SPEED, 0),
    pg.K_UP: (0, -SPEED),
    pg.K_DOWN: (0, SPEED),
}