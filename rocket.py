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
        self.last_update = time.time()
    
    def update(self):        
        time_elapsed = time.time() - self.last_update
        self.velocity = self.acceleration / time_elapsed
        self.altitude = self.altitude + ((self.velocity*math.sin(math.radians(self.angle))) * time_elapsed)
        if self.altitude < 0:  # Prevent altitudes lower than 0
            self.altirude = 0
        self.last_update = time.time()  # Update last to record the time the update was finished