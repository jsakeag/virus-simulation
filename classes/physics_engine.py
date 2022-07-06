import numpy as np


class PhysicsEngine:
    def __init__(self):
        self.body_pos_array = np.array([]).reshape((0, 3))
        self.body_list = None

    def define_bodies(self, body_list):
        self.body_list = [np.array([i, body])
                          for i, body in enumerate(body_list)]
