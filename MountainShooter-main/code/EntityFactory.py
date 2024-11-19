import random
from code.Background import Background
from code.Enemy import Enemy
from code.Enemy3 import Enemy3
from code.Player import Player
from code.Const import WIN_WIDTH, WIN_HEIGHT

class EntityFactory:
    @staticmethod
    def get_entity(entity_name):
        match entity_name:
            case 'Level1Bg':
                return [Background(f'Level1Bg{i}', (0, 0)) for i in range(7)]
            case 'Level2Bg':
                return [Background(f'Level2Bg{i}', (0, 0)) for i in range(5)]
            case 'Level3Bg':  # Novo caso para Bg3
                return [Background(f'Level3Bg{i}', (0, 0)) for i in range(5)]
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3':  # Novo caso para Enemy3
                return Enemy3('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))