import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Create pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add classes to Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")

        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            if(asteroid.is_colliding(player)):
                sys.exit("Game Over!")

        for i in drawable:
            i.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
