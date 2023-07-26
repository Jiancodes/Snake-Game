import pygame
import random

pygame.init()

# 游戏窗口大小和背景颜色
window_width, window_height = 800, 600
background_color = (0, 0, 0)

# 蛇和食物大小和颜色
snake_block = 10
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

# 设置游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇游戏')

# 显示得分
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def show_score(score):
    score_text = score_font.render("得分: " + str(score), True, (255, 255, 255))
    window.blit(score_text, [10, 10])

def our_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, snake_color, [x, y, snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False

    # 初始化蛇的位置和移动方向
    snake_x, snake_y = window_width / 2, window_height / 2
    snake_x_change, snake_y_change = 0, 0

    # 初始化蛇的位置和移动方向
    snake_list = []
    length_of_snake = 1

    # 随机生成食物的位置
    food_x, food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    snake_speed = 15
    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            window.fill(background_color)
            game_over_text = font_style.render("游戏结束, 按Q退出或C重新开始", True, (255, 255, 255))
            window.blit(game_over_text, [window_width / 6, window_height / 3])
            show_score(length_of_snake - 1)
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
                if event.key == pygame.K_LEFT and snake_x_change == 0:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT and snake_x_change == 0:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP and snake_y_change == 0:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN and snake_y_change == 0:
                    snake_y_change = snake_block
                    snake_x_change = 0

        # 碰撞检测
        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_close = True

        # 更新蛇的位置
        snake_x += snake_x_change
        snake_y += snake_y_change
        window.fill(background_color)

        # 画食物
        pygame.draw.rect(window, food_color, [food_x, food_y, snake_block, snake_block])

        # 将蛇的位置添加到蛇列表中
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        # 限制蛇的长度
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # 碰撞检测
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # 画蛇
        our_snake(snake_block, snake_list)

        # 显示得分
        show_score(length_of_snake - 1)

        # 更新显示
        pygame.display.update()

        # 吃到食物时增加蛇的长度，重新生成食物
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
