import pygame
import sys
from datetime import datetime
from code.DBProxy import DBProxy
from code.Const import C_YELLOW, C_WHITE, C_GRAY, WIN_WIDTH, WIN_HEIGHT

class Score:
    def __init__(self, window):
        self.window = window
        self.db_proxy = DBProxy()

    def save(self, game_mode, player_score):
        name = ''
        score = max(player_score)  # Usa a maior pontuação

        while True:
            self.window.fill((0, 0, 0))
            self.draw_text('Enter your name (4 characters):', C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 3))
            self.draw_text(name, C_YELLOW, (WIN_WIDTH / 2, WIN_HEIGHT / 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        date = datetime.now().strftime('%d/%m/%Y %H:%M')
                        self.db_proxy.save((name, score, date))
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 4:
                        name += event.unicode

    def show(self):
        scores = self.db_proxy.retrieve_top10()
        self.window.fill((0, 0, 0))
        self.draw_text('TOP 10 SCORES', C_YELLOW, (WIN_WIDTH / 2, 50))

        for i, (name, score, date) in enumerate(scores):
            text = f'{i + 1}. {name} - {score} - {date}'
            self.draw_text(text, C_WHITE, (WIN_WIDTH / 2, 100 + i * 30))

        self.draw_text('Press ESC to return', C_GRAY, (WIN_WIDTH / 2, WIN_HEIGHT - 20))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

    def draw_text(self, text, color, position):
        font = pygame.font.SysFont('Arial', 24)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=position)
        self.window.blit(text_surf, text_rect)