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

        player_input()
        update_game()
        draw_game(screen)

        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

def player_input():
    pass


def update_game():
    pass


def draw_game(screen):
    screen.fill((0, 0, 0))


if __name__ == "__main__":
    main()
