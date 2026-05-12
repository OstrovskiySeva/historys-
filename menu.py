import pygame
import init
import config
import subprocess

pygame.init()

font = pygame.font.SysFont(None, 50)

info_display = pygame.display.Info()

WIDTH = info_display.current_w
HEIGHT = info_display.current_h
running = True

buttons_rect = []
button_x, button_y = 250, 80

list_levels = init.list_level()

vid_menu = "main"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню")

fon_img = pygame.transform.smoothscale(init.fon_img, (WIDTH, HEIGHT))
button_img = pygame.transform.smoothscale(init.button_img, (300, 150))
button_st_right_img = pygame.transform.smoothscale(init.button_st_img, (100, 100))
button_st_left_img = pygame.transform.rotate(button_st_right_img, 180)

btn_play_img = pygame.image.load("img/btn_play.png")
btn_play_img = pygame.transform.smoothscale(btn_play_img, (300, 150))

def draw_fon(screen):
    screen.blit(fon_img, (0, 0))

def rects(x, y):
    global buttons_rect
    for i in range(0, 2):
        button_rect = pygame.Rect((x, y+240*i), (300, 150))
        buttons_rect.append(button_rect)
    for i in range(0, 2):
        button_rect = pygame.Rect((x+400, y+240*i), (300, 150))
        buttons_rect.append(button_rect)

def draw_button(screen, x, y):
    for i in range(0, 2):
        screen.blit(button_img, (x, y+240*i))
    for i in range(0, 2):
        screen.blit(button_img, (x+400, y+240*i))

def draw_text_btn(screen, x, y):
    text_btn = ["Играть", "Настройки", "Запасная", "Выход"]
    for i in range(0, 2):
        input_text = font.render(text_btn[i], True, (255, 255, 255))
        screen.blit(input_text, (x+75, y+240*i+50))
    for i in range(0, 2):
        input_text = font.render(text_btn[i+2], True, (255, 255, 255))
        screen.blit(input_text, (x+475, y+240*i+50))

def draw_fon_surf(screen):
    screen.blit(fon_img, (0, 0))
    screen_surface = pygame.Surface((WIDTH*0.98, HEIGHT*0.97))     
    screen_surface.set_alpha(135)
    screen_surface.fill((155, 155, 30))
    screen.blit(screen_surface, (10, 10))
    return screen_surface

def draw_btn_surf(screen):
    screen.blit(button_st_left_img, (20, HEIGHT*0.4))
    rect_btn_left = pygame.Rect(((20, HEIGHT*0.4)), (100, 100))
    screen.blit(button_st_right_img, (WIDTH-120, HEIGHT*0.4))
    rect_btn_right = pygame.Rect((WIDTH-120, HEIGHT*0.4), (100, 100))
    screen.blit(btn_play_img, (WIDTH*0.5-200, HEIGHT*0.7))
    rect_btn_play = pygame.Rect((WIDTH*0.5-190, HEIGHT*0.7), (300, 150))
    return rect_btn_play, rect_btn_left, rect_btn_right

def draw_game(screen):
    name_level = font.render(list_levels[config.num_lvl-1], True, (255, 255, 255))
    FILENAME = list_levels[config.num_lvl-1]
    screen.blit(name_level, (WIDTH*0.5-170, HEIGHT*0.7-20))

def btn_click(event):
    for i in range(0, len(buttons_rect)):
        if buttons_rect[i].collidepoint((event.pos[0], event.pos[1])):
            return i
    
def logic_click(num_btn_click):
    global running, vid_menu
    if num_btn_click == 3:
        running = False
    elif num_btn_click == 0:
        vid_menu = "play_menu"

def open_files():
    file1 = []
    with open("date.txt") as file:
        for line in file:
            if line.startswith("num_lvl"):
                file1.append('num_lvl ' + str(config.num_lvl))
            else:
                file1.append(line)
    with open("date.txt", "w") as file:
        file1 = "\n".join(file1)
        file.write(file1)

def bool_click_play(event, rect_btn_left, rect_btn_right, list_levels, rect_btn_play):
    if rect_btn_right.collidepoint((event.pos[0], event.pos[1])) and config.num_lvl-1 < len(list_levels)-1:
        config.num_lvl += 1
    elif rect_btn_left.collidepoint((event.pos[0], event.pos[1])) and 0 < config.num_text-1:
        config.num_lvl -= 1
    if rect_btn_play.collidepoint((event.pos[0], event.pos[1])):
        open_files()
        subprocess.run(["python", "main.py"])
    

rects(button_x, button_y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if vid_menu == "main":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    num_btn_click = btn_click(event)
                    logic_click(num_btn_click)
        elif vid_menu == "play_menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bool_click_play(event, rect_btn_left, rect_btn_right, list_levels, rect_btn_play)

    screen.fill((255, 255, 255))

    if vid_menu == "main":
        draw_fon(screen)
        draw_button(screen, button_x, button_y)
        draw_text_btn(screen, button_x, button_y)
    elif vid_menu == "play_menu":
        screen_surf = draw_fon_surf(screen)
        rect_btn_play, rect_btn_left, rect_btn_right = draw_btn_surf(screen)
        draw_game(screen)

    pygame.display.flip()

pygame.quit()
