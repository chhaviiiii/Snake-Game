import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (154, 205, 50)
blue = (50, 153, 213)

# Display
width, height = 400, 400
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Load Images
snake_head_img = pygame.image.load('snake-head.png')
food_img = pygame.image.load('food.png')


# Scale images
snake_block = 20  # Increased snake size
food_size = 20  # New variable for food size
snake_head_img = pygame.transform.scale(snake_head_img, (snake_block, snake_block))
food_img = pygame.transform.scale(food_img, (food_size, food_size))

clock = pygame.time.Clock()

snake_speed = 5
font_style = pygame.font.SysFont(None, 50)


def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == len(snake_list) - 1:  # Head of the snake
            game_display.blit(snake_head_img, (x[0], x[1]))
        else:  # Body of the snake
            pygame.draw.circle(game_display, green, [x[0] + snake_block // 2, x[1] + snake_block // 2],
                               snake_block // 2)


def message(msg, color, y_displace=0):
    line_spacing = font_style.get_height()
    for line in msg.splitlines():
        mesg = font_style.render(line, True, color)
        text_rect = mesg.get_rect(center=(width / 2, height / 3 + y_displace))
        game_display.blit(mesg, text_rect)
        y_displace += line_spacing

def show_score(score, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width/2, 15)
    game_display.blit(score_surface, score_rect)


def game_loop():
    game_over = False
    score = 0

    while not game_over:
        game_close = False


        x1 = width / 2
        y1 = height / 2
        x1_change = 0
        y1_change = 0
        snake_list = []
        length_of_snake = 1

        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        while not game_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            game_display.fill(black)
            game_display.blit(food_img, (foodx, foody))
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(snake_block, snake_list)
            show_score(score,white, 'consolas', 20)  # Display the score
            pygame.display.update()

            if x1 < foodx + food_size and x1 + snake_block > foodx and \
                    y1 < foody + food_size and y1 + snake_block > foody:
                foodx = round(random.randrange(0, width - food_size) / 10.0) * 10.0
                foody = round(random.randrange(0, height - food_size) / 10.0) * 10.0
                length_of_snake += 1
                score += 1

            clock.tick(snake_speed)

        while game_close:
            game_display.fill(black)
            message("Score: " + str(score) + "\n" +
                                  "Press Q to Quit" + "\n"
                                                      "Press R to Restart", white)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_close = False

    pygame.quit()
    quit()


# Call game_loop to start the game
game_loop()
