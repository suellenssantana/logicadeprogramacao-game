from .Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        if self.name == "Enemy3":
            self._move_enemy3()  # Chama a lógica específica para Enemy3
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]  # Movimento padrão para outros inimigos

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(f'{self.name}Shot', (self.rect.centerx, self.rect.centery))

    def _move_enemy3(self):
        # Movimento horizontal (da direita para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical (subir e descer)
        if not hasattr(self, "vertical_direction"):
            self.vertical_direction = -1  # Direção inicial: subir
            self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade inicial

        # Alterar a direção ao bater nas bordas superior ou inferior
        if self.rect.top <= 0:  # Bateu na borda superior
            self.vertical_direction = 1  # Muda direção para descer
            self.vertical_speed = ENTITY_SPEED[self.name] * 2  # Velocidade dobrada para descer
        elif self.rect.bottom >= self.screen_height:  # Bateu na borda inferior
            self.vertical_direction = -1  # Muda direção para subir
            self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade normal para subir

        # Aplicar o movimento vertical
        self.rect.centery += self.vertical_speed * self.vertical_direction