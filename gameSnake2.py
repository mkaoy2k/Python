""" 蛇遊戲 (Snake Game)

這個程式實現了一個經典的蛇遊戲，使用 Python 的 turtle 模組來繪製遊戲畫面。
玩家可以使用方向鍵控制蛇的移動，目標是吃到食物讓蛇變長，
同時避免撞到牆壁或自己。
"""

import turtle
import time
import random

# 設定遊戲視窗
tn = turtle.Screen()
tn.title("Snake Game")
tn.bgcolor("black")
tn.setup(width=600, height=600)
tn.tracer(0)  # 關閉自動更新，提高繪製速度

# 設定顏色
COLORS = {
    'white': "white",
    'black': "black",
    'red': "red",
    'green': "green",
    'blue': "blue"
}

# 蛇的設定
SNAKE_SPEED = 0.1

# 設定蛇頭
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(COLORS['green'])
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 設定食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(COLORS['red'])
food.penup()
food.goto(0, 100)

# 蛇的身體段落
segments = []

# 繪製分數的筆
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color(COLORS['white'])
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("分數: 0  最高分數: 0", align="center", font=("Courier", 24, "normal"))

# 初始化分數
score = 0
high_score = 0

def go_up():
    """向上移動"""
    if head.direction != "down":
        head.direction = "up"

def go_down():
    """向下移動"""
    if head.direction != "up":
        head.direction = "down"

def go_left():
    """向左移動"""
    if head.direction != "right":
        head.direction = "left"

def go_right():
    """向右移動"""
    if head.direction != "left":
        head.direction = "right"

def move():
    """移動蛇"""
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def check_collision():
    """檢查是否撞到牆壁或自己"""
    # 檢查是否撞到牆壁
    if (head.xcor() > 290 or head.xcor() < -290 or 
        head.ycor() > 290 or head.ycor() < -290):
        return True
        
    # 檢查是否撞到自己
    for segment in segments:
        if segment.distance(head) < 20:
            return True
    
    return False

def check_food_collision():
    """檢查是否吃到食物"""
    if head.distance(food) < 20:
        # 移動食物到隨機位置
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # 新增身體段落
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(COLORS['green'])
        new_segment.penup()
        segments.append(new_segment)

        # 增加分數
        global score
        score += 10

        # 更新最高分數
        global high_score
        if score > high_score:
            high_score = score

        # 更新分數顯示
        pen.clear()
        pen.write("分數: {}  最高分數: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

def update_segments():
    """更新蛇的身體段落"""
    # 移動身體段落
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # 移動第一個身體段落到蛇頭的位置
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

def game_over():
    """遊戲結束處理"""
    # 顯示遊戲結束訊息
    pen.clear()
    pen.write("遊戲結束！按 Q 離開或 R 重新開始", align="center", font=("Courier", 24, "normal"))
    
    # 等待玩家選擇
    while True:
        tn.update()
        

        
        # 檢查鍵盤輸入
        choice = tn.textinput("選擇", "按 Q 離開或 R 重新開始")
        if choice and choice.lower() == "q":
            tn.bye()
            break
        elif choice and choice.lower() == "r":
            # 重置遊戲
            head.goto(0, 0)
            head.direction = "stop"
            
            # 隱藏身體段落
            for segment in segments:
                segment.goto(1000, 1000)
            
            # 清空身體段落
            segments.clear()
            
            # 重置分數
            global score
            score = 0
            
            # 更新分數顯示
            pen.clear()
            pen.write("分數: {}  最高分數: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            
            # 重新設置鍵盤監聽器
            tn.listen()
            tn.onkeypress(go_up, "Up")
            tn.onkeypress(go_down, "Down")
            tn.onkeypress(go_left, "Left")
            tn.onkeypress(go_right, "Right")
            
            break

def main():
    """遊戲主迴圈"""
    # 設定鍵盤綁定
    tn.listen()
    tn.onkeypress(go_up, "Up")
    tn.onkeypress(go_down, "Down")
    tn.onkeypress(go_left, "Left")
    tn.onkeypress(go_right, "Right")

    # 主要遊戲迴圈
    while True:
        tn.update()

        # 檢查是否吃到食物
        check_food_collision()

        # 更新蛇的身體段落
        update_segments()

        # 移動蛇
        move()

        # 檢查是否撞到牆壁或自己
        if check_collision():
            game_over()

        time.sleep(SNAKE_SPEED)

    # 保持視窗開啟
    tn.mainloop()

if __name__ == "__main__":
    main()
