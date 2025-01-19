import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Apples")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Basket
basket_width = 100
basket_height = 20
basket_x = (WIDTH - basket_width) // 2
basket_y = HEIGHT - 50
basket_speed = 10

# Apples
apple_radius = 20
apple_x = random.randint(apple_radius, WIDTH - apple_radius)
apple_y = -apple_radius
apple_speed = 5

# Score
score = 0
font = pygame.font.SysFont("Arial", 30)

# Game Over
game_over_font = pygame.font.SysFont("Arial", 50)

def draw_basket(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, basket_width, basket_height))

def draw_apple(x, y):
    pygame.draw.circle(screen, RED, (x, y), apple_radius)

def show_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def game_over_message():
    game_over_text = game_over_font.render("Game Over!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(3000)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move the apple
    apple_y += apple_speed

    # Check if apple is caught
    if (basket_y < apple_y + apple_radius < basket_y + basket_height and
            basket_x < apple_x < basket_x + basket_width):
        score += 1
        apple_x = random.randint(apple_radius, WIDTH - apple_radius)
        apple_y = -apple_radius
        apple_speed += 0.2  # Increase speed as the score goes up

    # Check if apple hits the ground
    if apple_y > HEIGHT:
        game_over_message()
        running = False

    # Draw everything
    draw_basket(basket_x, basket_y)
    draw_apple(apple_x, apple_y)
    show_score(score)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
