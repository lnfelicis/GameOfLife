import pygame
import numpy as np


width = 1920
height = 1080
background_color = (0, 0, 0)
pixel_color = (255, 255, 255)
fps = 240
pixel_size = 15
line_color = (0, 0, 0)

array = np.random.randint(2, size=(width//pixel_size, height//pixel_size))

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
iteration = 0
max_iteration = 750

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    newArray = np.zeros_like(array)
    for i in range(1, len(array) - 1):
        for j in range(1, len(array[0]) - 1):
            sum = np.sum(array[i-1: i+2, j-1: j+2]) - array[i, j]
            if array[i, j] == 1 and (sum < 2 or sum > 3):
                    newArray[i, j] = 0
            elif array[i, j] == 0 and sum == 3:
                    newArray[i, j] = 1
            else:
                 newArray[i, j] = array[i, j]
    
    array = newArray.copy()

    screen.fill(background_color)

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i,j] == 1:
                pygame.draw.rect(screen, pixel_color, pygame.Rect(i*pixel_size, j*pixel_size, pixel_size, pixel_size))
    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(fps)

    iteration += 1
    if iteration >= max_iteration:
        array = np.random.randint(2, size=(width//pixel_size, height//pixel_size))
        iteration = 0


pygame.quit()
