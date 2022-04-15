# Conway's Game of Life implementation in PyGame

import pygame
import random

def main():
    '''
    Main function. Initializes the game and runs it.
    '''
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()
    running = True
    grid = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            grid[i][j] = random.randint(0, 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for i in range(100):
            for j in range(100):
                if grid[i][j] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (i * 10, j * 10, 10, 10))
        pygame.display.flip()
        for i in range(100):
            for j in range(100):
                if grid[i][j] == 1:
                    if count_neighbors(grid, i, j) < 2 or count_neighbors(grid, i, j) > 3:
                        grid[i][j] = 0
                elif count_neighbors(grid, i, j) == 3:
                    grid[i][j] = 1
        clock.tick(10)
    pygame.quit()

def count_neighbors(grid, x, y):
    '''
    Counts the number of neighbors of a cell.
    '''
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (
                i >= 0
                and i < 100
                and j >= 0
                and j < 100
                and (i != x or j != y)
            ):
                count += grid[i][j]
    return count

if __name__ == "__main__":
    main()