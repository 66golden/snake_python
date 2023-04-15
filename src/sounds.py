import pygame as pg

# define sounds
background_sound = pg.mixer.Sound('sounds/background.mp3')
background_sound.set_volume(0.2)
game_over_sound = pg.mixer.Sound('sounds/game_over.mp3')
game_over_sound.set_volume(0.2)
eating_food_sound = pg.mixer.Sound('sounds/eating_food.mp3')
eating_food_sound.set_volume(0.3)
