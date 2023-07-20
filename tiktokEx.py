import pygame
import time
import random

pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
grid_size = 20

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up the snake initial position and velocity
snake_block = 20
snake_speed = 10

# Initialize the display
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Define functions

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])

def draw_score(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score), True, blue)
    game_display.blit(text, (10, 10))

def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    rendered_msg = font_style.render(msg, True, color)
    game_display.blit(rendered_msg, [screen_width / 6, screen_height / 3])

def game_loop():
    # Initialize the game
    game_over = False
    game_close = False

    snake_list = []
    snake_length = 1

    snake_x = screen_width / 2
    snake_y = screen_height / 2

    x_change = 0
    y_change = 0

    food_x = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0

    clock = pygame.time.Clock()

    # Game loop
    while not game_over:

        while game_close:
            game_display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            draw_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_close = True

        snake_x += x_change
        snake_y += y_change

        game_display.fill(white)
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        draw_score(snake_length - 1)

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
game_loop()
