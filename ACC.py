import time

import pygame
import random

params = {
    "running": True,
    "max-allowed-speed": 120
}

class Car:
    def __init__(self,root):
        self.root = root
        self.transform = (0, 500, 50, 50)  # pos x, pos y, scale x, scale y
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def evaluate_speed(self, dist):
        rd = dist - 2
        if rd <= 0: return 0
        elif rd <= 25: return params["max-allowed-speed"]-(self.transform[0]/16)
        elif rd > 25: return params["max-allowed-speed"]
        else: return "unexpected error occurred..."

    def finished(self):
        time.sleep(2)
        self.transform = (0, 500, 50, 50)

    def move(self):
        dist = (1870-self.transform[0])/50
        speed = self.evaluate_speed(dist)/100
        if speed == 0: self.finished()
        self.transform = (self.transform[0]+speed, self.transform[1], self.transform[2], self.transform[3])

    def draw(self):
        pygame.draw.rect(self.root, self.color, pygame.Rect(self.transform))

def simulation_loop():
    root = pygame.display.set_mode((1920, 1080))
    car_inst = Car(root)
    while params["running"]:
        root.fill((0,0,0))
        pygame.draw.rect(root, (255, 0, 0), pygame.Rect((1915, 0, 20, 1080)))
        car_inst.move()
        car_inst.draw()
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    simulation_loop()