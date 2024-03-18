import sys
import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

pygame.init()

#screen dymensions
WIDTH, HEIGHT = 400, 600
GRID_SIZE = 30
WHITE = (255, 255, 255)

#Define the different tetromino shapes (I, J, L, O, S, T, Z) using 2D arrays.

SHAPES = [
 [
        ['X', 'X', 'X', 'X']
        ],
[
        ['.', '.', 'X'],
        ['X', 'X', 'X']
        ],
[
        ['X', '.', '.'],
        ['X', 'X', 'X']
        ],
[
        ['X', 'X'],
        ['X', 'X']
        ],
[
        ['.', 'X', 'X'],
        ['X', 'X', '.']
        ],
[
        ['.', 'X', '.'],
        ['X', 'X', 'X']
        ],
[
        ['X', 'X', '.'],
        ['.', 'X', 'X']
        ]
]

# Initialize tetromino position
tetromino_x, tetromino_y = WIDTH // 2, 0
current_tetromino = random.choice(SHAPES) #This line selects a random tetromino shape from the list of predefined shapes (SHAPES).

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Game")

# Initialize the grid (2D array to track placed blocks)
grid = [[None] * (WIDTH // GRID_SIZE) for _ in range(HEIGHT // GRID_SIZE)]

# Game loop
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Handle user input (left, right, down arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tetromino_x -= GRID_SIZE
    if keys[pygame.K_RIGHT]:
        tetromino_x += GRID_SIZE
    if keys[pygame.K_DOWN]:
        tetromino_y += GRID_SIZE

    # Check collision with the bottom or other blocks
    if tetromino_y + len(current_tetromino) * GRID_SIZE >= HEIGHT:
        # Place the tetromino on the grid
        for row in range(len(current_tetromino)):
            for col in range(len(current_tetromino[0])):
                if current_tetromino[row][col] == 'X':
                    grid[(tetromino_y + row * GRID_SIZE) // GRID_SIZE][(tetromino_x + col * GRID_SIZE) // GRID_SIZE] = 'X'
        # Reset tetromino position
        tetromino_x, tetromino_y = WIDTH // 2, 0
        current_tetromino = random.choice(SHAPES)

    # Draw the placed blocks on the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                pygame.draw.rect(screen, WHITE, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()