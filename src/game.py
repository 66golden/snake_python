import pygame as pg

pg.init()

import globals
import sounds
import Food
import Score
import Snake
import Walls


def game_over():
    """opens an action selection window for the player, where
       he can choose to either start the game again or quit the game.
    Args:
        None.
    Returns:
        None.
    """
    globals.DISPLAY_SURFACE.blit(globals.game_over_text, globals.game_over_tablet)
    globals.DISPLAY_SURFACE.blit(globals.play_or_quit_text, globals.play_or_quit_tablet)
    sounds.background_sound.stop()
    sounds.eating_food_sound.stop()
    sounds.game_over_sound.play()
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    quit()
                elif event.key == pg.K_p:
                    main_game()


def choose_speed():
    """opens the difficulty selection window for the player, where
       he can choose one of three versions: easy, medium or hard.
    Args:
        None.
    Returns:
        int: the speed of the snake depending on the player's choice.
    """
    while True:
        globals.DISPLAY_SURFACE.fill(globals.BLUE_BACKGROUND)
        globals.DISPLAY_SURFACE.blit(globals.choose_speed_text_1,
                             globals.choose_speed_tablet_1)
        globals.DISPLAY_SURFACE.blit(globals.choose_speed_text_2,
                             globals.choose_speed_tablet_2)
        globals.DISPLAY_SURFACE.blit(globals.choose_speed_text_3,
                             globals.choose_speed_tablet_3)
        globals.DISPLAY_SURFACE.blit(globals.choose_speed_text_4,
                             globals.choose_speed_tablet_4)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1 or event.key == pg.K_KP_1:
                    return globals.SPEED - 5
                if event.key == pg.K_2 or event.key == pg.K_KP_2:
                    return globals.SPEED
                if event.key == pg.K_3 or event.key == pg.K_KP_3:
                    return globals.SPEED + 5
            if event.type == pg.QUIT:
                pg.quit()
                quit()


def can_move(x, y, walls, snake):
    """checks if the snake can go to the x, y coordinates.
    Args:
        x (int): x coordinate.
        y (int): y coordinate.
        walls (Walls.Walls): walls on the field of play.
        snake (Snake.Snake): snake on the field of play.
    Returns:
        bool: True, if the snake can go to the x, y coordinates, False otherwise.
    """
    for (x_start, y_start, width, height) in walls.all_walls:
        if x_start <= x <= x_start + width - 15\
                and y_start <= y <= y_start + height - 15:
            return False

    return bool(x >= 0 and x + globals.SNAKE_BLOCK <= globals.WIDTH
                and y >= 0 and y + globals.SNAKE_BLOCK <= globals.HEIGHT
                and (x, y) not in snake.blocks)


def direction_set(snake):
    """sets the direction of the snake's movement.
    Args:
        snake (Snake.Snake): snake on the field of play.
    Returns:
        None.
    """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key in globals.KEY_ACTIONS:
                x_new, y_new = globals.KEY_ACTIONS[event.key]
                if snake.x_speed == 0 and snake.y_speed == 0 or \
                        x_new + snake.x_speed != 0 and y_new + snake.y_speed != 0:
                    snake.x_speed, snake.y_speed = x_new, y_new


def eat_food(snake, score, walls, food, head_x, head_y):
    """function that checks if the snake with head at
       head_x and head_y has or has not eaten food.
    Args:
        snake (Snake.Snake): snake on the field of play.
        score (Score.Score): score of the play.
        walls (Walls.Walls): walls on the field of play.
        food (list): food on the field of play.
        head_x (int): x coordinate of the snake's head.
        head_y (int): y coordinate of the snake's head.
    Returns:
        bool: True, if a snake has eaten food, False otherwise.
    """
    for food_number in range(len(food)):
        if head_x == food[food_number].x_coord and head_y == food[food_number].y_coord:
            food[food_number] = Food.Food(walls.all_walls)
            sounds.eating_food_sound.stop()
            sounds.eating_food_sound.play()
            score.points += 1
            score.record = max(score.record, score.points)
            snake.x_speed *= -1
            snake.y_speed *= -1
            snake.blocks = snake.blocks[::-1]
            return True
    return False


def main_game():
    """the main game function that runs throughout the game.
    Args:
        None.
    Returns:
        None.
    """
    # set background sound and choose speed
    sounds.game_over_sound.stop()
    sounds.background_sound.play(loops=-1)
    SPEED = choose_speed()

    # generate food, walls and initialize snake
    walls = Walls.Walls()
    walls.generate_walls()
    food = [Food.Food(walls.all_walls), Food.Food(walls.all_walls), Food.Food(walls.all_walls)]
    score = Score.Score()
    score.record = score.read_record()
    snake = Snake.Snake()

    while True:
        direction_set(snake)
        if snake.x_speed != 0 or snake.y_speed != 0:
            head_x, head_y = snake.blocks[-1]
            head_x += snake.x_speed
            head_y += snake.y_speed
            if can_move(head_x, head_y, walls, snake):
                snake.blocks.append((head_x, head_y))
            else:
                game_over()
            if not eat_food(snake, score, walls, food, head_x, head_y):
                snake.blocks.pop(0)

        walls.draw_background()
        for food_number in range(len(food)):
            food[food_number].draw_food()
        snake.draw_snake()
        score.draw_score()
        pg.display.update()
        globals.FPS_CLOCK.tick(SPEED)

main_game()