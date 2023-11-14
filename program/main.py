from my_global_var import *
from game_assets import *

running = True
clock = pygame.time.Clock()
FPS = 60
total_rocks = []
rock_generated_time = time.time()
mgt = time.time()   #missile_generated_time
rdt = 3-game_level    #rock_delay_time 암석 생성 지연
m_duration = 0.3

def main():
    global missiles, rock_generated_time
    fighter = Fighter()
    while running:
        end_game()
        # 배경 출력
        menu_screen()
        # 남은 파괴해야 할 운석 개수
        draw_text(screen, "남은 운석 : {}".format(int(globals()["game_level"]*2 - len(globals()["dead_rock_list"]))))
        # 남은 시간 출력하기
        level_adjust_timer = timer(globals()["level_adjust_time"], int(globals()["game_level"] * 2 + 15))
        if level_adjust_timer != None:
            draw_text(screen, "남은 시간 : {}".format(level_adjust_timer), (WIDTH // 2, HEIGHT // 10 * 9), font_size=WIDTH//12, color=(255, 0, 0))
        # 게임 종료
        else:
            while running:
                end_game()
                menu_screen()
                end_text()    
                update(10)
        # 레벨 출력하기
        draw_text(screen, "level{}".format(int(globals()["game_level"] * 2)), (WIDTH // 2, HEIGHT // 8))

        # 레벨 올리기
        if len(dead_rock_list) >= (globals()["game_level"]*2):
            globals()["game_level"] += 0.5
            globals()["dead_rock_list"].clear()
            print("cleared")

        # 전투기 출력
        fighter.update()
        fighter.draw()            

        # 미사일 missiles 리스트에 추가
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if time.time() - globals()["mgt"] > 0.3:    # 미사일 생성 제한시간
                missiles.append(Missile(fighter))
                globals()["mgt"] = time.time()
                
        # 미사일 업데이트
        for missile in missiles:
            missile.update()
            missile.draw()
        
        # 운석 랜덤 출력하기
        if len(globals()["dead_rock_list"]) < (globals()["game_level"] * 2):
            if globals()["rdt"] > 0.3:
                if (time.time() - rock_generated_time) > (3 - game_level):
                    total_rocks.append(Rock())
                    rock_generated_time = time.time()
                    globals()["m_duration"] -= 0.03
            else:
                globals()["rdt"] = 0.3

        # rock 충돌 감지
        # 게임 종료 조건
        if rock_fighter_collision(total_rocks, fighter) == True:
            while running:
                end_game()
                menu_screen()
                end_text()
                update(10)

        missile_rock_collision(missiles, total_rocks)            
        # rock 업데이트
        for rock in total_rocks:
            rock.update()
            rock.draw()

        update(120)

# 게임 시작
while running:
    # 본 게임 시작하기 전
    end_game()
    # 메뉴 화면 출력
    menu_screen()
    draw_text(screen, "환영합니다!", pos = (WIDTH // 2, HEIGHT // 2 - 30), font_size=WIDTH//10)
    draw_text(screen, "게임을 시작하려면 스페이스 바를 눌러주세요", pos = (WIDTH // 2, HEIGHT // 2 + HEIGHT//14.4), font_size=WIDTH//20, color = (175, 244, 45))
        
    # 화면 업데이트
    update(60)

    # 게임 시작 키를 눌렀는지 확인하기
    while running:
        # X버튼을 눌렀는지 확인
        end_game()
    
        key_pressed = pygame.key.get_pressed()
        if key_pressed[starting_key]:
            break
    
    # 타이머 재료
    start_time = time.time()
        
    # 게임 시작 전 카운트다운
    while running:
        end_game()
        # 메뉴 화면 출력
        menu_screen()

        # 타이머 출력
        timer_1 = timer(start_time, 3)
        draw_text(screen, str(timer_1))

        # 타이머 종료 조건
        if timer_1 == None:
            running = False
        
        update(60)
    
    running = True
    # 게임 시작 문구 출력
    while running:
        end_game()
        menu_screen()
        draw_text(screen, "시작!", font_size=WIDTH//8)
        update(60)
        time.sleep(1)
        break
    
# 본격 게임 시작!
    while running:
        main()
