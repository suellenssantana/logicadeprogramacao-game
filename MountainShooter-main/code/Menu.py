import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_YELLOW, C_WHITE, C_ORANGE, C_GRAY

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, (0, 0))
            for i, option in enumerate(MENU_OPTION):
                color = C_YELLOW if i == menu_option else C_WHITE
                self.draw_text(option, color, (WIN_WIDTH / 2, 200 + 30 * i))

            # Exibir o nome e RU no canto inferior esquerdo
            self.draw_text('Suellen Santos de Santana, RU 4675033', C_GRAY, (150, WIN_HEIGHT - 30))  # Ajuste posição conforme necessário
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def draw_text(self, text, color, position):
        font = pygame.font.SysFont('Arial', 24)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=position)
        self.window.blit(text_surf, text_rect)