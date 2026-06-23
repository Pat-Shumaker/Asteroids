import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000
        log_state()        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
