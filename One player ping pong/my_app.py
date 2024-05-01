import pygame 
import random

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ping pong")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_width = 40
player_height = 150
player_speed = 7
ball_size = 40
ball_speed_x = 9
ball_speed_y = 9

player = pygame.Rect(34, SCREEN_HEIGHT // 2 - player_height // 2, player_width, player_height)

# Randomize the starting position of the ball within the visible screen width
ball = pygame.Rect(random.randint(0, SCREEN_WIDTH - ball_size), SCREEN_HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
ball_direction_x = random.choice([-1, 1])
ball_direction_y = random.choice([-1, 1])

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Default font with size 36


game_running = True
pygame.time.delay(1000)
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    movement = pygame.key.get_pressed()
    if movement[pygame.K_UP]:
        player.y -= player_speed
    if movement[pygame.K_DOWN]:
        player.y += player_speed

    ball.x += ball_speed_x * ball_direction_x
    ball.y += ball_speed_y * ball_direction_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_direction_y *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_direction_x *= -1
    if ball.left <= 0:
        lose_text = "YOU LOSE! :("
        surface_of_lose_text = font.render(lose_text, True, RED)
        rect_of_lose_text = surface_of_lose_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(surface_of_lose_text, rect_of_lose_text)
        pygame.display.flip()
        pygame.time.delay(5000)
        game_running = False

    if ball.colliderect(player):
        ball_direction_x *= -1

    screen.fill(BLUE)

    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.circle(screen, RED, ball.center, ball_size // 2)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

