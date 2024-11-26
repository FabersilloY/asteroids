# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

def main():
    print("Starting asteroids!")
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    while True:

        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        print(dt)
        pygame.display.flip()
        
if __name__ == "__main__":
    main()