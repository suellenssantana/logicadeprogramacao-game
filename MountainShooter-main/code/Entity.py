from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, name, position):
        self.name = name
        self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)
        self.health = 100
        self.damage = 10

    @abstractmethod
    def move(self):
        pass