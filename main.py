import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

# Load the sound effect
music_files = ['C:\\Users\\My PC\\PycharmProjects\\Snake\\Alan Walker - On My Way (Instrumental).mp3',]

# Choose a random music file to play
music_file = random.choice(music_files)

# Load the sound effect
pygame.mixer.music.load(music_file)

# Play the music
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(2.0)


# Define colors
BLACK = (0, 0, 0)
WHITE = (240, 248, 255)
ORCHID = (61, 145, 64)
DARKOLIVEGREEN = (85,107,47)
RED = (238,44,44)

# Define the snake and food
snake_block_size = 20
snake_speed = 14
font_style = pygame.font.SysFont(None, 55)
large_font = pygame.font.SysFont(None, 80)

def draw_snake(snake_block_size, snake_list): #Snake appearance
    for x in snake_list:
        pygame.draw.rect(game_window, BLACK, [x[0], x[1], snake_block_size, snake_block_size])

def message(msg, color, score, highest_score=None):
    msg = font_style.render(msg, True, color)
    game_window.blit(msg, [WINDOW_WIDTH/2 - msg.get_width()/2, WINDOW_HEIGHT/2.6 - msg.get_height()/2]) #PRESS C TO TRY AGAIN
    msg2 = large_font.render("YOU LOST!", True, RED)
    game_window.blit(msg2, [WINDOW_WIDTH / 2 - msg2.get_width() / 1.7, WINDOW_HEIGHT / 4]) #YOU LOST!
    highest_score_font = pygame.font.SysFont(None, 35)
    highest_score_text = highest_score_font.render("Highest Score: " + str(highest_score), True, WHITE)
    game_window.blit(highest_score_text, [10, 10])
    score_font = pygame.font.SysFont(None, 70)
    score_text = score_font.render("Your Score: " + str(score), True, WHITE)
    game_window.blit(score_text, [WINDOW_WIDTH - score_text.get_width() - 255, 400 + highest_score_text.get_height()])

def game_loop():
    game_over = False
    game_close = False
    score = 0
    highest_score = 0

    # Load the highest score from a file
    with open('highest_score.txt', 'r') as f:
        score_str = f.read()
        if score_str:
            highest_score = int(score_str)

    # Starting position of the snake
    x1 = WINDOW_WIDTH / 2
    y1 = WINDOW_HEIGHT / 2

    # Change in position of the snake
    x1_change = 0
    y1_change = 0

    # Define the snake and food
    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 20.0) * 20.0

    def display_highest_score():
        highest_score_font = pygame.font.SysFont(None, 35)
        highest_score_text = highest_score_font.render("Highest Score: " + str(highest_score), True, WHITE)
        game_window.blit(highest_score_text, [10, 10])

    def display_current_score():
        score_font = pygame.font.SysFont(None, 35)
        score_text = score_font.render("Current Score: " + str(score), True, WHITE)
        game_window.blit(score_text, [10, 40])


    # Start the game loop
    while not game_over:

        while game_close == True:
            game_window.fill(ORCHID)
            message("Press Q to Quit or Press C to Play Again", WHITE, score, highest_score)
            pygame.display.update()
            pygame.font.SysFont(None, 70)
            pygame.display.update()
            pygame.mixer.music.fadeout(1000)

            # Choose a random music file to play
            music_file = random.choice(music_files)

            # Load the sound effect
            pygame.mixer.music.load(music_file)

            # Play the music
            pygame.mixer.music.play(loops=-1)
            pygame.mixer.music.set_volume(0.3)

            if foodx is None and foody is None:
                # Generate a random position for the food
                foodx = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 20.0) * 20.0
                foody = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 20.0) * 20.0

                # Check if the food is overlapping with the snake's body
                while [foodx, foody] in snake_list:
                    foodx = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 20.0) * 20.0
                    foody = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 20.0) * 20.0

            # Display the highest score
            display_highest_score()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        pygame.mixer.music.play(loops=-1)  # Start the music again
                        game_loop()

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check if snake goes out of bounds
        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            pygame.mixer.music.fadeout(1000)
            game_close = True

        # Check if the game is over
        if game_close:
            pygame.mixer.music.fadeout(1000)  # Fade out the music over 2 seconds
            game_window.fill(DARKOLIVEGREEN)
            message("Press Q to Quit or Press C to Play Again", WHITE, score, highest_score)


            # Check if the current score is higher than the highest score
            if score > highest_score:
                highest_score = score
                with open('highest_score.txt', 'w') as f:
                    f.write(str(highest_score))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Draw the food and snake on the screen
        game_window.fill(ORCHID)
        pygame.draw.rect(game_window, RED, [foodx, foody, snake_block_size, snake_block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block_size, snake_list)

        # Display the highest score
        display_highest_score()

        # Display the current score
        display_current_score()

        pygame.display.update()

        # Check if the snake has hit the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 20.0) * 20.0
            Length_of_snake += 1
            score += 10

        # Update the game clock
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Deactivate pygame library
    pygame.quit()

game_loop()