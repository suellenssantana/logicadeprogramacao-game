import pygame

# Cores
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_GRAY = (128, 128, 128)

# Eventos
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# Configurações gerais
SPAWN_TIME = 4000
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = {
    'Level1': 20000,
    'Level2': 20000,
    'Level3': 40000,  # Level 3 tem o dobro da duração dos outros níveis
}

# Dimensões da tela
WIN_WIDTH = 576
WIN_HEIGHT = 324

# Opções do menu
MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT'
)

# Posições do placar
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50)}

# Teclas de controle
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# Velocidades das entidades
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level3Bg0': 0,  # Velocidade dos elementos de fundo do Level 3
    'Level3Bg1': 1,
    'Level3Bg2': 2,
    'Player1': 3,
    'Player1Shot': 5,
    'Enemy1': 1,
    'Enemy1Shot': 4,
    'Enemy2': 2,
    'Enemy2Shot': 5,
    'Enemy3': 2,  # Velocidade horizontal de Enemy3
    'Enemy3Vertical': 3,  # Velocidade vertical normal de Enemy3
    'Enemy3Shot': 6,  # Velocidade do tiro de Enemy3
}

# Delay para tiros das entidades
ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
    'Enemy3': 80,  # Enemy3 atira mais rápido que os outros inimigos
}