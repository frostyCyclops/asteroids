import pygame
from constants import *
import sys
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        update_game(player, dt)
        draw_game(screen, player)

        
        dt = clock.tick(60) / 1000


def update_game(player, dt):
    player.update(dt)


def draw_game(screen, player):
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()


if __name__ == "__main__":
    main()
