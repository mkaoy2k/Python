""" 蛇遊戲 (Snake Game)

這個程式實現了一個經典的蛇遊戲，使用 Pygame 模組來繪製遊戲畫面。
玩家可以使用方向鍵控制蛇的移動，目標是吃到食物讓蛇變長，
同時避免撞到牆壁或自己。
"""

import pygame
import random
from pygame.locals import *

# 初始化 Pygame
pygame.init()

# 顏色定義
COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

# 視窗設定
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 蛇的設定
SNAKE_BLOCK = 20
SNAKE_SPEED = 15

# 設定視窗
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

# 定義蛇類別
class Snake:
    """蛇類別，負責蛇的移動和繪製"""
    def __init__(self):
        """初始化蛇的位置和速度"""
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.speed = SNAKE_BLOCK
        self.body = []
        self.length = 1
        self.x_change = 0
        self.y_change = 0

    def move(self):
        """移動蛇的位置"""
        self.x += self.x_change
        self.y += self.y_change
        
        # 更新蛇的身體
        snake_head = []
        snake_head.append(self.x)
        snake_head.append(self.y)
        self.body.append(snake_head)
        
        if len(self.body) > self.length:
            del self.body[0]

    def draw(self):
        """繪製蛇"""
        for segment in self.body:
            pygame.draw.rect(display, COLORS['green'], 
                           [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def check_collision(self):
        """檢查是否撞到牆壁或自己"""
        if (self.x >= WINDOW_WIDTH or self.x < 0 or 
            self.y >= WINDOW_HEIGHT or self.y < 0):
            return True
            
        for segment in self.body[:-1]:
            if segment == [self.x, self.y]:
                return True
        
        return False

# 定義食物類別
class Food:
    """食物類別，負責食物的生成和繪製"""
    def __init__(self):
        """初始化食物的位置"""
        self.x = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
        self.y = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    def draw(self):
        """繪製食物"""
        pygame.draw.rect(display, COLORS['red'], 
                       [self.x, self.y, SNAKE_BLOCK, SNAKE_BLOCK])

    def respawn(self):
        """重新生成食物的位置"""
        self.x = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
        self.y = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

# 定義遊戲類別
class Game:
    """遊戲類別，負責遊戲的主要邏輯"""
    def __init__(self):
        """初始化遊戲"""
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False

    def check_food_collision(self):
        """檢查是否吃到食物"""
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.food.respawn()
            self.snake.length += 1
            self.score += 10

    def update(self):
        """更新遊戲狀態"""
        self.snake.move()
        self.check_food_collision()
        
        if self.snake.check_collision():
            self.game_over = True

    def draw(self):
        """繪製遊戲畫面"""
        display.fill(COLORS['black'])
        self.snake.draw()
        self.food.draw()
        
        # 顯示分數
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {self.score}", True, COLORS['white'])
        display.blit(score_text, [0, 0])

    def run(self):
        """遊戲主迴圈"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake.x_change == 0:
                        self.snake.x_change = -self.snake.speed
                        self.snake.y_change = 0
                    elif event.key == pygame.K_RIGHT and self.snake.x_change == 0:
                        self.snake.x_change = self.snake.speed
                        self.snake.y_change = 0
                    elif event.key == pygame.K_UP and self.snake.y_change == 0:
                        self.snake.y_change = -self.snake.speed
                        self.snake.x_change = 0
                    elif event.key == pygame.K_DOWN and self.snake.y_change == 0:
                        self.snake.y_change = self.snake.speed
                        self.snake.x_change = 0

            if not self.game_over:
                self.update()
                self.draw()
                pygame.display.update()
                clock.tick(SNAKE_SPEED)
            else:
                message("Game Over! Press Q to quit or R to restart", COLORS['red'])
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        if event.key == pygame.K_r:
                            self.__init__()

# 遊戲開始
if __name__ == '__main__':
    game = Game()
    game.run()