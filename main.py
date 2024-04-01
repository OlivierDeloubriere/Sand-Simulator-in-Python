import pygame
import world

GRID_WIDTH = 4
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
INITIAL_GRAIN_COLOR = (220, 245, 128)
BACKGROUND_COLOR = (20,20,45)
BUCKET_SIZE = 10
GRAIN_COLOR_PALETTE = [INITIAL_GRAIN_COLOR, (200, 225, 140), (220, 245, 180)]

def updateWindow(grid, screen):
    screen.fill(BACKGROUND_COLOR)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != (0,0,0):
                pygame.draw.rect(screen, grid[i][j], pygame.Rect(GRID_WIDTH * i, GRID_WIDTH * j, GRID_WIDTH, GRID_WIDTH))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    gameClock = pygame.time.Clock()
    gameIsRunning = True
    colorIndex = 0
    changeColorCounter = 0
    gameWorld = world.World(WINDOW_HEIGHT // GRID_WIDTH, WINDOW_WIDTH // GRID_WIDTH)
    while gameIsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
                break

        mouseButtonPressed = pygame.mouse.get_pressed()
        if any(mouseButtonPressed):
            mouseX, mouseY = pygame.mouse.get_pos()
            gameWorld.addGrain(mouseX // GRID_WIDTH, mouseY // GRID_WIDTH, BUCKET_SIZE, GRAIN_COLOR_PALETTE[colorIndex])
            changeColorCounter += 1

        if changeColorCounter == 20:
            changeColorCounter = 0
            colorIndex += 1
            if colorIndex == len(GRAIN_COLOR_PALETTE):
                colorIndex = 0

        gameWorld.update()

        updateWindow(gameWorld.grid, screen)
        
        pygame.display.flip()
        gameClock.tick(120) # Limit game to 60 fps

    pygame.quit()

    