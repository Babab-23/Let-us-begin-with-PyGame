import pygame

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window title
pygame.display.set_caption("My First Game Screen")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Fill background with color
screen.fill(WHITE)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw a rectangle as an example
    pygame.draw.rect(screen, BLUE, (350, 250, 100, 100))
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
