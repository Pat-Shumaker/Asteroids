import pygame
from constants import *
from logger import log_state
from player import *

def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        dt = clock.tick(60) / 1000
        log_state()        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
