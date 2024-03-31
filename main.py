import pygame
import world

GRID_WIDTH = 2
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
GRAIN_COLOR = (220, 245, 128)
BACKGROUND_COLOR = (20,20,45)
BUCKET_SIZE = 20

def updateWindow(grid, screen):
    screen.fill(BACKGROUND_COLOR)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, GRAIN_COLOR, pygame.Rect(GRID_WIDTH * i, GRID_WIDTH * j, GRID_WIDTH, GRID_WIDTH))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    gameClock = pygame.time.Clock()
    gameIsRunning = True
    
    gameWorld = world.World(WINDOW_HEIGHT // GRID_WIDTH, WINDOW_WIDTH // GRID_WIDTH)
    while gameIsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
                break

        mouseButtonPressed = pygame.mouse.get_pressed()
        if any(mouseButtonPressed):
            mouseX, mouseY = pygame.mouse.get_pos()
            gameWorld.addGrain(mouseX // GRID_WIDTH, mouseY // GRID_WIDTH, BUCKET_SIZE)

        gameWorld.update()

        updateWindow(gameWorld.grid, screen)
        
        pygame.display.flip()
        gameClock.tick(120) # Limit game to 60 fps

    pygame.quit()

    