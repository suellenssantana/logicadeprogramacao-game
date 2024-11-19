import pygame
from code.Const import ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[PLAYER_KEY_UP[self.name]]:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_DOWN[self.name]]:
            self.rect.centery += ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_LEFT[self.name]]:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_RIGHT[self.name]]:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0 and pygame.key.get_pressed()[PLAYER_KEY_SHOOT[self.name]]:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return PlayerShot(f'{self.name}Shot', (self.rect.centerx, self.rect.centery))