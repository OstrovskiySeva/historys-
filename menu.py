import pygame

pygame.init()

font = pygame.font.SysFont(None, 50)

info_display = pygame.display.Info()

WIDTH = info_display.current_w
HEIGHT = info_display.current_h
running = True

buttons_rect = []
button_x, button_y = 250, 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню")

fon_img = pygame.image.load("img/fon/fon_menu.png")
fon_img = pygame.transform.smoothscale(fon_img, (WIDTH, HEIGHT))

button_img = pygame.image.load("img/button.png")
button_img = pygame.transform.smoothscale(button_img, (300, 150))

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

def btn_click(event):
    for i in range(0, len(buttons_rect)):
        if buttons_rect[i].collidepoint((event.pos[0], event.pos[1])):
            return i
    
def logic_click(num_btn_click):
    global running
    if num_btn_click == 3:
        running = False
    elif num_btn_click == 0:
        import main.py

rects(button_x, button_y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                num_btn_click = btn_click(event)
                logic_click(num_btn_click)

    screen.fill((255, 255, 255))
    
    draw_fon(screen)
    draw_button(screen, button_x, button_y)
    draw_text_btn(screen, button_x, button_y)

    pygame.display.flip()

pygame.quit()
