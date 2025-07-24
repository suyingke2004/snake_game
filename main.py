import pygame
import sys
from game.snake import Snake
from game.food import Food
from game.logic import check_collisions
from game.scores import load_high_scores, save_high_scores, add_score
from game.constants import (SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, 
                            FPS, TEXT_COLOR, FONT_PATH)

def draw_text(screen, text, size, x, y, color=TEXT_COLOR):
    """在屏幕上绘制文本"""
    try:
        font = pygame.font.Font(FONT_PATH, size)
    except FileNotFoundError:
        font = pygame.font.Font(None, size + 10) # 字体加载失败时的备用方案
        
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def show_game_over_screen(screen, score, high_scores):
    """显示游戏结束画面，包含分数、排行榜和操作按钮"""
    # 将当前分数添加到排行榜并保存
    updated_scores = add_score(score, high_scores)
    save_high_scores(updated_scores)

    screen.fill(BACKGROUND_COLOR)
    draw_text(screen, "GAME OVER", 48, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6)
    draw_text(screen, f"Your Score: {score}", 32, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)

    # 显示排行榜
    draw_text(screen, "High Scores", 28, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30)
    for i, hs in enumerate(updated_scores):
        draw_text(screen, f"{i+1}. {hs}", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + (i * 30))

    # 创建按钮
    play_again_rect = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT * 0.75 - 25, 200, 50)
    quit_rect = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT * 0.75 + 50, 200, 50)

    pygame.draw.rect(screen, (20, 80, 20), play_again_rect) # 暗绿色按钮
    pygame.draw.rect(screen, (80, 20, 20), quit_rect) # 暗红色按钮

    draw_text(screen, "Play Again", 24, play_again_rect.centerx, play_again_rect.centery)
    draw_text(screen, "Quit", 24, quit_rect.centerx, quit_rect.centery)
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    return 'restart'
                if quit_rect.collidepoint(event.pos):
                    return 'quit'
            if event.type == pygame.KEYUP: # 保留按键重新开始的功能
                return 'restart'

def game_loop(screen, clock):
    """游戏主循环"""
    snake = Snake()
    food = Food(snake.body)
    score = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # ... (方向键控制)
                elif event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        snake.move()

        if check_collisions(snake):
            running = False

        if snake.get_head() == food.position:
            snake.grow()
            food.randomize_position(snake.body)
            score += 10

        screen.fill(BACKGROUND_COLOR)
        snake.draw(screen)
        food.draw(screen)
        draw_text(screen, f"Score: {score}", 24, SCREEN_WIDTH / 2, 30)
        
        pygame.display.flip()
        clock.tick(FPS)
        
    return score

def main():
    """主函数，管理游戏状态"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("贪吃蛇")
    clock = pygame.time.Clock()

    high_scores = load_high_scores()
    score = 0
    
    while True:
        # 游戏开始前，可以先显示一个开始/菜单界面，这里我们直接进入游戏
        # 为了简单起见，我们用 game_over 后的界面作为循环的起点
        
        score = game_loop(screen, clock)
        
        action = show_game_over_screen(screen, score, high_scores)
        
        if action == 'quit':
            break
        elif action == 'restart':
            high_scores = load_high_scores() # 重新加载以更新排行榜
            continue

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
