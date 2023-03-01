import math
import time

class Rocket:
    def __init__(self,fuel=100, health=100, acceleration=0, velocity=0, angle=90, altitude = 0):
        self.fuel = fuel
        self.health = health
        self.acceleration = acceleration
        self.velocity = velocity
        self.angle = angle  # Referenced from the positive side of X in a 2D representation.
        self.altitude = altitude        
        self.engine_on = False
        self.acceleration = 0
    
    def update(self):       
        self.velocity += self.acceleration
        self.altitude += self.velocity
        if self.altitude < 0:  # Prevent altitudes lower than 0
            self.altitude = 0
        