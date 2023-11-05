import pygame
import random
import time
import math
import os

pygame.init()

def relative_path(image_path):
    current_dir = os.getcwd()
    image_path = os.path.join(current_dir, image_path)
    return image_path

# 이미지 파일들 호출
# rocks
rock_1 = pygame.image.load(relative_path(".\이미지 파일\Rock_1.png"))
rock_2 = pygame.image.load(relative_path(".\이미지 파일\Rock_2.png"))
rock_3 = pygame.image.load(relative_path(".\이미지 파일\Rock_3.png"))
rock_4 = pygame.image.load(relative_path(".\이미지 파일\Rock_4.png"))

# 배경
background_image = pygame.image.load(relative_path(".\이미지 파일\space.png"))

# 우주선
spaceship_image = pygame.image.load(relative_path(".\이미지 파일\spaceship.png"))    # 비율이 1:1

# 미사일
missile_image = pygame.image.load(relative_path(".\이미지 파일\missile.png"))

# 체력
hp_image = pygame.image.load(relative_path(".\이미지 파일\hp.png"))

# 폭발
explosion_image = pygame.image.load(relative_path(".\이미지 파일\explosion_1.png"))

# 화면 생성
WIDTH = 480
HEIGHT = 720
SIZE = WIDTH, HEIGHT
screen = pygame.display.set_mode(SIZE)
screen_rect = screen.get_rect()
pygame.display.set_caption("shooting game")

# rocks 스케일
rock_1 = pygame.transform.scale(rock_1, ( screen.get_width() // 6, screen.get_height() // 6 ))
rock_2 = pygame.transform.scale(rock_2, ( screen.get_width() // 6, screen.get_height() // 6 ))
rock_3 = pygame.transform.scale(rock_3, ( screen.get_width() // 6, screen.get_height() // 6 ))
rock_4 = pygame.transform.scale(rock_4, ( screen.get_width() // 6, screen.get_height() // 6 ))
rocks = [rock_1, rock_2, rock_3, rock_4]

# 난이도
game_level = 0.5
level_adjust_time = time.time()

# 암석 출현 빈도
rock_prob = 10
# 암석 갯수
rock_pcs = game_level + 1
total_rocks = []

# 남은 시간
left_time = 10

# 지구 상태
earth_status = 0

# 게임 시작 키
starting_key = pygame.K_SPACE

# FPS
FPS = 60

# 미사일 리스트
missiles = []

# 죽은 객체들
dead_rock_list = []  # 돌들

# 남은 운석 개수
rock_to_destroy = 0