import pygame
import random
from .constants import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, FOOD_COLOR

class Food:
    """
    定义食物的类
    """
    def __init__(self, snake_body):
        """
        初始化食物，确保其位置不在蛇身上.
        """
        self.position = (0, 0)
        self.randomize_position(snake_body)

    def randomize_position(self, snake_body):
        """
        随机生成食物的新位置，并确保这个位置当前不是蛇身体的一部分.
        """
        while True:
            self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if self.position not in snake_body:
                break

    def draw(self, screen):
        """
        在屏幕上绘制食物.
        """
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, FOOD_COLOR, rect)