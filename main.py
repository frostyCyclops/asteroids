import pygame
from constants import *
import sys


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player_input()
        update_game()
        draw_game(screen)


def player_input():
    pass


def update_game():
    pass


def draw_game(screen):
    screen.fill((0, 0, 0))
    pygame.display.flip()


if __name__ == "__main__":
    main()
