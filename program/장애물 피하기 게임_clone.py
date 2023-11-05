import pygame
import random

# pygame 초기화
pygame.init()

# 게임 창 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("장애물 피하기 게임")

# FPS 설정
clock = pygame.time.Clock()

# 색상 설정
black = (255, 255, 255)
white = (0, 0, 0)
red = (255, 0, 0)

# 플레이어 초기 설정(크기, 위치, 속도)
player_width = 50
player_height = 50
player_color = white
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height
player_speed = 5

# 장애물 초기 설정(크기, 위치, 속도)
obstacle_width = 50
obstacle_height = 50
obstacle_color = red
obstacle_x = random.randint(0, screen_width - player_width)
obstacle_y = 0
obstacle_speed = 3

# 장애물 리스트 초기화
obstacles = []

# 게임 루프 시작
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # 플레이어 이동 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("move_left")

    # 화면 업데이트
    pygame.display.update()
    clock.tick(60)

    # 게임 종료

