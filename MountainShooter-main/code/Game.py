import pygame
import sys
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

class Game:
    def __init__(self):
        # Inicialização do Pygame e da janela do jogo
        pygame.init()
        self.window = pygame.display.set_mode((576, 324))
        pygame.display.set_caption("Mountain Shooter")

    def run(self):
        print("Jogo iniciado!")
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            score = Score(self.window)

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # Inicia o score do jogador
                # Level 1
                level1 = Level(self.window, 'Level1', menu_return, player_score)
                if level1.run(player_score):
                    # Level 2
                    level2 = Level(self.window, 'Level2', menu_return, player_score)
                    if level2.run(player_score):
                        # Level 3
                        level3 = Level(self.window, 'Level3', menu_return, player_score)
                        if level3.run(player_score):
                            # Salvar e mostrar o score após Level 3
                            score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:  # Mostra as pontuações
                score.show()
            elif menu_return == MENU_OPTION[4]:  # Sai do jogo
                pygame.quit()
                sys.exit()