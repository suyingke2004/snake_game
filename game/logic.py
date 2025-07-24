from .constants import GRID_WIDTH, GRID_HEIGHT

def check_collisions(snake):
    """
    检查蛇是否发生了碰撞.

    Args:
        snake (Snake): 蛇对象.

    Returns:
        bool: 如果发生碰撞则返回 True, 否则返回 False.
    """
    head = snake.get_head()
    head_x, head_y = head

    # 1. 检查是否撞到墙壁
    if not (0 <= head_x < GRID_WIDTH and 0 <= head_y < GRID_HEIGHT):
        return True  # 撞墙

    # 2. 检查是否撞到自身
    # 检查蛇头位置是否存在于蛇身体的其余部分
    if head in snake.body[1:]:
        return True  # 撞到自己

    return False
