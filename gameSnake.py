""" 蛇遊戲 (Snake Game)

這個程式實現了一個經典的蛇遊戲，玩家可以控制蛇移動吃食物，
蛇每吃一個食物就會變長，如果撞到牆壁或自己就會遊戲結束。
"""

import pygame   # pip install pygame
import random

# 初始化 Pygame
pygame.init()

# 顏色定義
COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (213, 50, 80),
    'green': (0, 255, 0),
    'blue': (50, 153, 213)
}

# 視窗設定
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 蛇的設定
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# 設定視窗大小
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# 設定時鐘
clock = pygame.time.Clock()

# 定義訊息顯示函數
def message(msg, color):
    """在畫面上顯示訊息
    
    Args:
        msg (str): 要顯示的訊息
        color (tuple): 訊息顏色
    """
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect()
    mesg_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    display.blit(mesg, mesg_rect)

# 定義遊戲迴圈
def game_loop():
    """遊戲主要迴圈"""
    game_over = False
    game_close = False

    # 蛇的初始位置和速度
    x1 = WINDOW_WIDTH / 2
    y1 = WINDOW_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    # 蛇的身體
    snake_list = []
    length_of_snake = 1

    # 食物的位置
    foodx = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    foody = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    # 分數
    score = 0

    while not game_over:

        while game_close == True:
            display.fill(COLORS['black'])
            message("Game Over! Press Q-Quit or C-Play Again", COLORS['red'])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # 使用方向鍵控制蛇的移動
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # 更新蛇的位置
        x1 += x1_change
        y1 += y1_change

        # 檢查是否撞到牆壁
        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            game_close = True

        # 檢查是否吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            foody = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            length_of_snake += 1
            score += 10

        # 更新蛇的身體
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # 檢查是否撞到自己
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # 繪製遊戲畫面
        display.fill(COLORS['black'])
        pygame.draw.rect(display, COLORS['red'], [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        
        for segment in snake_list:
            pygame.draw.rect(display, COLORS['green'], [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

        # 顯示分數
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, COLORS['white'])
        display.blit(score_text, [0, 0])

        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# 遊戲開始
if __name__ == '__main__':
    game_loop()