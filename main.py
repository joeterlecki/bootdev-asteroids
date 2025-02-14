#!/usr/bin/env python3

import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    tick = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.colliding(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("#000000")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = tick.tick(60) / 1000


if __name__ == "__main__":
    main()
