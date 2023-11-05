from my_global_var import *
from game_assets import *

running = True
clock = pygame.time.Clock()
FPS = 60
total_rocks = []
rock_generated_time = time.time()
rock_to_destroy = int(game_level * 2)
game_duration = 8
fighter = Fighter()

def main():
    globals()["level_adjust_time"] = time.time()
    while running:
        # X버튼 눌렀는지 확인
        end_game()
        # 배경화면 출력
        menu_screen()
        # 파괴해야 할 운석 개수 출력
        draw_text(screen, "남은 운석 : {}".format(rock_to_destroy), (WIDTH // 2, HEIGHT // 9))
        # 남은 시간 출력
        draw_text(screen, "남은 시간 : {}".format(timer(level_adjust_time, game_duration)))
        # 전투기 출력
        fighter.draw()
        fighter.update()
        # 미사일 출력
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            missiles.append(Missile(fighter))
        for missile in missiles:
            missile.draw()
            missile.update()
        # 운석 출력
        if len(total_rocks) <= int(game_level + 2):
            total_rocks.append(Rock())
        for rock in total_rocks:
            rock.update()
            rock.draw()
            print(total_rocks)
                
        update(60)
        
# 게임 시작
while running:
    # 본 게임 시작하기 전
    end_game()
    # 메뉴 화면 출력
    menu_screen()
    draw_text(screen, "환영합니다!", pos = (WIDTH // 2, HEIGHT // 2 - 30), font_size = 80)
    draw_text(screen, "게임을 시작하려면 스페이스 바를 눌러주세요", pos = (WIDTH // 2, HEIGHT // 2 +50), color = (175, 244, 45), font_size=20)
        
    # 화면 업데이트
    update(60)

    # 게임 시작 키를 눌렀는지 확인하기
    while running:
        # X버튼을 눌렀는지 확인
        end_game()
    
        key_pressed = pygame.key.get_pressed()
        if key_pressed[starting_key]:
            break

    # 게임 시작 문구 출력
    while running:
        end_game()
        menu_screen()
        draw_text(screen, "시작!", font_size=50)
        update(60)
        time.sleep(1)
        break
    
# 본격 게임 시작!
    while running:
        main()
