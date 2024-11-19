import random
import sys
import pygame
from code.Const import (
    C_WHITE, WIN_HEIGHT, EVENT_ENEMY, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL, C_GREEN, C_CYAN, C_GRAY, WIN_WIDTH
)
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player

class Level:
    def __init__(self, window, name, game_mode, player_score):
        self.window = window
        self.name = name
        # Ajusta a duração do timeout para o Level 3
        self.timeout = TIMEOUT_LEVEL[name] * 2 if name == 'Level3' else TIMEOUT_LEVEL[name]
        self.game_mode = game_mode
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity(f'{name}Bg'))

        # Inicializa jogadores
        player1 = EntityFactory.get_entity('Player1')
        player1.score = player_score[0]
        self.entity_list.append(player1)

        if game_mode in ['NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COMPETITIVE']:
            player2 = EntityFactory.get_entity('Player2')
            player2.score = player_score[1]
            self.entity_list.append(player2)

        # Define timers para geração de inimigos e controle de tempo
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score):
        # Carrega a música do nível
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            self.window.fill((0, 0, 0))
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    if self.name == 'Level3':
                        # Gera apenas Enemy3 no Level 3
                        self.entity_list.append(EntityFactory.get_entity('Enemy3'))
                    else:
                        # Gera Enemy1 ou Enemy2 em outros níveis
                        choice = random.choice(['Enemy1', 'Enemy2'])
                        self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        # Salva o score ao final do nível
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                if ent.name == 'Player1':
                                    player_score[0] = ent.score
                                elif ent.name == 'Player2':
                                    player_score[1] = ent.score
                        return True

            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)
                if isinstance(ent, (Player)):
                    shoot = ent.shoot()
                    if shoot:
                        self.entity_list.append(shoot)

            # Verifica colisões e estado das entidades
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # Verifica se ainda há jogadores
            found_player = any(isinstance(ent, Player) for ent in self.entity_list)
            if not found_player:
                return False

            # Exibe o tempo restante e informações adicionais
            self.draw_text(f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.draw_text('Suellen Santos de Santana, RU 4675033', C_GRAY, (WIN_WIDTH / 2, WIN_HEIGHT - 20))
            pygame.display.flip()

    def draw_text(self, text, color, position):
        font = pygame.font.SysFont('Arial', 18)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=position)
        self.window.blit(text_surf, text_rect)