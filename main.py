import pygame
from constants import *
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    _ = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        update_game(updatable, dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        draw_game(screen, drawable)

        
        dt = clock.tick(60) / 1000


def update_game(updatable, dt):
    for sprite in updatable:
        sprite.update(dt)


def draw_game(screen, drawable):
    screen.fill((0, 0, 0))
    
    for sprite in drawable:
        sprite.draw(screen)
    
    pygame.display.flip()


if __name__ == "__main__":
    main()
