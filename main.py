#!/usr/bin/env python3

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        screen.fill("#000000")
        pygame.display.flip()


if __name__ == "__main__":
    main()
