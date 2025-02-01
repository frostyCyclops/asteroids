from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        random_angle = random.uniform(30, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_split = Asteroid(self.position.x, self.position.y, new_radius)
        first_split.velocity = self.velocity.rotate(random_angle) * 1.2

        second_split = Asteroid(self.position.x, self.position.y, new_radius)
        second_split.velocity = self.velocity.rotate(-random_angle) * 1.2
    
    def update(self, dt):
        self.position += self.velocity * dt
