import unittest
import sys
import os

# 将 game 目录添加到 sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.snake import Snake
from game.logic import check_collisions
from game.constants import GRID_WIDTH, GRID_HEIGHT

class TestGameLogic(unittest.TestCase):

    def test_wall_collision(self):
        """测试蛇撞到墙壁的情况"""
        snake = Snake()
        
        # 撞到左墙
        snake.body = [(-1, 10)]
        self.assertTrue(check_collisions(snake), "应检测到与左墙的碰撞")

        # 撞到右墙
        snake.body = [(GRID_WIDTH, 10)]
        self.assertTrue(check_collisions(snake), "应检测到与右墙的碰撞")

        # 撞到上墙
        snake.body = [(10, -1)]
        self.assertTrue(check_collisions(snake), "应检测到与上墙的碰撞")

        # 撞到下墙
        snake.body = [(10, GRID_HEIGHT)]
        self.assertTrue(check_collisions(snake), "应检测到与下墙的碰撞")

    def test_self_collision(self):
        """测试蛇撞到自己的情况"""
        snake = Snake()
        # 创建一个会撞到自己的蛇身体
        snake.body = [(10, 10), (11, 10), (12, 10), (10, 10)]
        self.assertTrue(check_collisions(snake), "应检测到与自身的碰撞")

    def test_no_collision(self):
        """测试没有发生碰撞的正常情况"""
        snake = Snake()
        # 一个正常的蛇
        snake.body = [(10, 10), (9, 10), (8, 10)]
        self.assertFalse(check_collisions(snake), "正常情况下不应检测到碰撞")

if __name__ == '__main__':
    unittest.main()
