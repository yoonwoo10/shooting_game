
from my_global_var import *
import time
import math

# 클래스들
class Rock:
    def __init__(self):
        self.img = random.choice(rocks)
        self.img = pygame.transform.scale(self.img, (WIDTH//5, WIDTH//5))
        self.rect = self.img.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.img.get_width())
        self.rect.bottom = random.randrange(0, HEIGHT // 4)
        self.dx = 0
        self.dy = game_level + 2
        self.is_moving = True

    def update(self):
        if self.is_moving == True:
            # 이미지의 위치를 업데이트합니다.
            # self.rect.x += self.dx
            self.rect.y += self.dy
        # 화면 밖으로 나갔는지 확인
        if self.rect.top > screen_rect.bottom:
            self.is_moving = False
            del self

    def draw(self):
        if self.is_moving == True:
            # 이미지를 화면에 그립니다.
            screen.blit(self.img, self.rect)

class Missile:
    def __init__(self, fighter_1):
      self.dy = 30
      self.img = missile_image
      width = WIDTH//16
      height = width * 3
      self.img = pygame.transform.scale(self.img, (width, height))
      self.rect = self.img.get_rect()
      self.rect.center = fighter_1.rect.center
      self.is_moving = True
          
    def update(self):
        if self.is_moving == True:
            self.rect.centery -= self.dy
            
        # 화면 밖으로 나갔는지 확인
        if self.rect.bottom < screen_rect.top:
            self.is_moving = False
            del self

    def draw(self):
        if self.is_moving == True:
            screen.blit(self.img, self.rect)


class Fighter:
    def __init__(self):
        self.img = spaceship_image
        width = WIDTH // 4
        height = width
        self.img = pygame.transform.scale(self.img, (width, height))
        self.rect = self.img.get_rect()
        self.rect.center = ((WIDTH // 2, HEIGHT // 3 * 2))
        self.is_moving = True
        self.dx = WIDTH // 48
        self.dy = self.dx

    def draw(self):
        if self.is_moving == True:
            screen.blit(self.img, self.rect)
    
    def update(self):
        if self.is_moving == True:
            keys = pygame.key.get_pressed()
            # 방향키 입력 확인
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.dx
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.dx
            if keys[pygame.K_UP]:
                self.rect.y -= self.dy
            if keys[pygame.K_DOWN]:
                self.rect.y += self.dy
            # 전투기 화면 밖으로 못 나가게 하기
            if self.rect.x < screen_rect.left:
                self.rect.x += self.dx
            if (self.rect.x + self.rect.width) > screen_rect.right:
                self.rect.x -= self.dx
            if self.rect.bottom > screen_rect.bottom:
                self.rect.y -= self.dy
            # 전투기 돌 생성 범위 위로 못 올라가게 하기
            if self.rect.top < HEIGHT//4*1.5:
                self.rect.y += self.dy


class Explosion:
    def __init__(self):
        # 이미지 스케일
        self.img = explosion_image
        self.img = pygame.transform.scale(self.img, (WIDTH//4, WIDTH//4))
        self.is_moving = True

    # 폭발 이미지 출력
    def draw_explode_image(self, obj):
        screen.blit(self.img, obj.rect)

# 함수들
# 텍스트 출력 함수
def draw_text(screen, text: str, pos:tuple = (WIDTH // 2, HEIGHT // 2), font = "nanumgothic", font_size = WIDTH//8, color:tuple = (255, 255, 0)):
    font = pygame.font.SysFont(font, font_size)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = pos
    screen.blit(text_obj, text_rect)
   
# 메뉴 화면 출력 함수
def menu_screen():
    img = background_image
    img = pygame.transform.scale(img, SIZE)
    screen.blit(img, (0, 0))


# 게임 종료 화면 출력
def end_screen():
    img = background_image
    img = pygame.transform.scale(img, SIZE)
    screen.blit(img, (0, 0))
    draw_text(screen, "게임 오버", (WIDTH // 2, HEIGHT // 2), "nanumgothic", 100)
    draw_text(screen, "다시 시작하려면 엔터 키를 누르세요", (WIDTH // 2, HEIGHT // 2 + 30))

# 화면 업데이트 함수
def update(FPS):
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

# 타이머 함수
def timer(start_time, left_time)    -> int:
    current_time = time.time()
    passed_time = current_time - start_time
    if (left_time - passed_time) > 0.5:
        return int(left_time - passed_time)

# 종료 버튼 확인 함수
def end_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# 충돌 확인
def rock_fighter_collision(rock_list, fighter):
    # fighter와 rocks 충돌 감지
    for rock in rock_list:
        if rock.rect.colliderect(fighter.rect):
            rock.is_moving = False
            fighter.is_moving = False
            return True

def missile_rock_collision(missile_list, rock_list):
    # missile과 rocks 충돌 감지
    for missile in missile_list:
        for rock in rock_list:
            if rock.rect.colliderect(missile.rect):
                missile.is_moving = False
                rock.is_moving = False
                Explosion().draw_explode_image(rock)

                # rock과 missile 없애기
                missile_list.remove(missile)
                globals()["dead_rock_list"].append(rock)
                rock_list.remove(rock)
                return True

# The End 출력
def end_text():
    draw_text(screen, "게임 종료", font_size=WIDTH//4.8, color=(0, 255, 0))
