import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (30, 30, 30)  # Dark gray
SQUARE_COLOR = (0, 200, 0)       # Green
SQUARE_SIZE = 50
FPS = 60

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sample - Moving Square")

# Set up the square
square_x, square_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
square_speed = 50

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key presses
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed

    # Keep square within screen boundaries
    if square_x < 0:
        square_x = 0
    if square_x > SCREEN_WIDTH - SQUARE_SIZE:
        square_x = SCREEN_WIDTH - SQUARE_SIZE
    if square_y < 0:
        square_y = 0
    if square_y > SCREEN_HEIGHT - SQUARE_SIZE:
        square_y = SCREEN_HEIGHT - SQUARE_SIZE

    # Fill the screen with background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the square
    pygame.draw.rect(screen, SQUARE_COLOR, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)



