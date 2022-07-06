import pygame
import time
from classes.physics_engine import PhysicsEngine
from classes.body import Body

BODY_COUNT = 15
TIME_DELAY = 0.005


class Simulation:
    physics_engine = PhysicsEngine()

    def __init__(self):
        self.run, self.space, self.bodies = None, None, None

    def initialise_environment(self, body_list, initial_infected):
        self.bodies = body_list
        self.space_plane_size = (1000, 800)  # width, height of canvas
        self.run = True
        self.runtime = 0
        self.initial_infected = initial_infected

        # setting up pygame
        pygame.init()
        pygame.display.set_caption("Covid simulation")
        self.space = pygame.display.set_mode(self.space_plane_size)

        # setting up physics engine
        self.physics_engine.define_bodies(body_list)

    def show_environment(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.space.fill((0, 0, 0))

            for body in self.bodies:
                body.draw(self.space)

            for body in self.bodies:
                body.move()
                # print(body.velocity)
                # print(body.position)

            for body in self.bodies:
                if(body.position[0][0] > self.space_plane_size[0] or body.position[0][0] < 0):
                    body.bounce_velocity_x()
                if(body.position[0][1] > self.space_plane_size[1] or body.position[0][1] < 0):
                    body.bounce_velocity_y()

            for body in self.bodies:
                for other_body in self.bodies:
                    if(body != other_body):
                        if(body.detect_collision(other_body)):
                            print(str(Body.num_infected) +
                                  " infected at " + str(round(self.runtime, 2)) + "s")

            if(Body.num_infected == BODY_COUNT):
                self.run = False
                print("//////////////////////////////////////////////////////////////////////" +
                      "\nAll infected! \nTotal Bodies: " + str(BODY_COUNT) +
                      "\nTotal runtime: " + str(round(self.runtime, 2)) +
                      "\nAverage infection time: " + str(round(self.runtime/BODY_COUNT, 2)) +
                      "\nAverage infection time after initial: " + str(round(self.runtime/(BODY_COUNT-self.initial_infected), 2)) +
                      "\n//////////////////////////////////////////////////////////////////////")

            self.runtime += TIME_DELAY
            time.sleep(TIME_DELAY)

            pygame.display.update()
