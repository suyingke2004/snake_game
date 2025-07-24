import pygame
from .constants import GRID_SIZE, SNAKE_COLOR, GRID_WIDTH, GRID_HEIGHT

class Snake:
    """
    定义蛇的类
    """
    def __init__(self):
        """
        初始化蛇.
        """
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)  # 初始向右

    def move(self):
        """
        根据当前方向移动蛇.
        """
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        
        new_head = (head_x + dir_x, head_y + dir_y)
        
        self.body.insert(0, new_head)
        # 移动时，在头部增加一个新块，并移除尾部最后一个块
        self.body.pop()

    def grow(self):
        """
        当蛇吃到食物时，身体增长.
        这个方法通过在下一次移动时不移除尾部来实现增长.
        为了做到这一点，我们只需在蛇的尾部复制最后一个元素即可.
        """
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        """
        改变蛇的移动方向，防止180度掉头.
        """
        if self.direction[0] != -new_direction[0] or \
           self.direction[1] != -new_direction[1]:
            self.direction = new_direction

    def draw(self, screen):
        """
        在屏幕上绘制蛇的每一段.
        """
        for segment in self.body:
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, SNAKE_COLOR, rect)

    def get_head(self):
        """
        获取蛇头的位置.
        """
        return self.body[0]