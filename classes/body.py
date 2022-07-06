from typing_extensions import runtime
import pygame
import numpy as np

# CONSTANTS

TIME_DELAY = 0.005


class Body:
    num_infected = 0

    def __init__(self, position_array, mass, color, radius):
        self.velocity = np.array([[0, 0, 0]])
        self.position = position_array
        self.radius = radius
        self.thickness = self.radius * 2
        self.color = color
        self.infected = False

    def draw(self, surface):
        pygame.draw.circle(
            surface, self.color, (self.position[0][0], self.position[0][1]), self.radius, self.thickness)

    def detect_collision(self, other_body):
        dist = np.linalg.norm(self.position-other_body.position)
        if(dist < self.thickness):
            return other_body.infect()
        return False

    def add_velocity(self, velocity_array):
        self.velocity = self.velocity + velocity_array

    def bounce_velocity_x(self):
        self.velocity = np.array(
            [[-self.velocity[0][0], self.velocity[0][1], self.velocity[0][2]]])

    def bounce_velocity_y(self):
        self.velocity = np.array(
            [[self.velocity[0][0], -self.velocity[0][1], self.velocity[0][2]]])

    def move(self):
        self.position = self.position + self.velocity * TIME_DELAY

    def infect(self):
        if(not self.infected):
            self.infected = True
            self.color = (255, 100, 100)
            Body.num_infected += 1
            return True
        return False
