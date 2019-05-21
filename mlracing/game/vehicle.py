import numpy as np

class Vehicle(object):
    def __init__(self, vid, timestep = 0.1, eyes = 4, **kwargs):
        self.id = vid
        self.timestep = timestep
        self.eyes = eyes
        self.position = np.zeros((2,)) # meters
        self.speed_line = 0. # meters per second
        self.speed_turn = 0. # degrees per second
        self.maxspeed = 10.
        self.maxturn = 10.

        self.heading = 0. # degrees
        self.lineofsight = np.zeros((self.eyes,)) # Distance to obstacles in meters

        self.acc_line = 1.0 # meters per second per second
        self.acc_turn = 5 # degrees per second per second

    def dirvec(self):
        return np.asarray([np.cos(self.heading*np.pi/180), np.sin(self.heading*np.pi/180)])

    def step(self, inp):
        """Advances the condition of the vehicle object by one step, depending on the input.

        Arguments:
            inp {numpy.ndarray} -- The control input to the vehicle.
        """
        self.speed_line = np.clip(self.speed_line + self.acc_line * self.timestep * inp[0], 0, self.maxspeed)
        self.speed_turn = np.clip(self.speed_turn + self.acc_turn * self.timestep * inp[1], 0, self.maxturn)
        self.heading = np.arctan(np.tan(np.pi/180*(self.heading + self.speed_turn * self.timestep))) * 180 / np.pi
        self.position = self.position + self.dirvec() * self.speed_line * self.timestep

