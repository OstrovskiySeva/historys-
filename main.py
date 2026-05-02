import pygame 
import init
import os
from copy import *

pygame.init()

info_display = pygame.display.Info()

WIDTH = info_display.current_w
HEIGHT = info_display.current_h
running = True

dialog_line = "TEXT "
dialog_lines = [dialog_line]

print_text = ""
num_text = 1
old_fon = init.FONFILE

buttons_rect = []
heros_list = []

class Hero:
        def __init__(self, name, place):
                self.name = name
                self.place = place

        def place_move(self, num_text, texts):
                if int(num_text-1) < len(texts):
                        text_copy = texts[int(num_text-1)]
                        place = text_copy["hero"][2]
                        place = place[0 : len(place)-1]
                        self.place = place

        def pos_place(self, place):
                if place == "left":
                        x = 50
                        y = HEIGHT*0.55-400
                elif place == "top":
                        x = WIDTH*0.4
                        y = HEIGHT*0.55-400
                elif place == "right":
                        x = WIDTH*0.6
                        y = HEIGHT*0.55-400
                return x, y

        def filehero(self, num_text, texts):
              if int(num_text-1) < len(texts):
                text_copy = texts[int(num_text-1)]
                anim = text_copy["hero"][1]
                return anim
        
        def image_hero(self, image):
                file_img = "img/hero/" + str(self.name) + "/" + str(image)
                img_hero = init.hero_init(file_img)
                return img_hero

        def draw_hero(self, screen, num_text, texts):
                image = self.filehero(num_text, texts)
                img_hero = self.image_hero(image)
                img_hero = pygame.transform.smoothscale(img_hero, (300, 500))
                x, y = self.pos_place(self.place)
                return img_hero, x, y

music_end_event = pygame.USEREVENT
pygame.mixer.music.set_endevent(music_end_event)
music_index = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("История")

text_font = pygame.font.SysFont(None, int(WIDTH/30))
        
def fon_import(num_text, fon, texts):
        global old_fon
        if int(num_text-1) < len(texts):
                text_copy = texts[int(num_text-1)]
                if text_copy["fon"]:
                        fon = text_copy["fon"][0]
                        old_fon = fon[0 : len(fon)-1]
                        return fon[0 : len(fon)-1]
                else:
                        return old_fon

def names_text(num_text, texts):
    if int(num_text-1) < len(texts):
        text_copy = texts[int(num_text-1)]
        name = text_copy["name"][0]
        return name[0: len(name)-1]

def copy_text(num_text, texts):
    if int(num_text-1) < len(texts):
        text_copy = texts[int(num_text-1)]
        line = text_copy["lines"][0]
        return line[0 : len(line)-1]
                        

def bool_hero(num_text, texts):
        if int(num_text-1) < len(texts):
                text_copy = texts[int(num_text-1)]
                if text_copy["hero"]:
                        return True
                else:
                        return False

def creat_hero(num_text, texts):
        if int(num_text-1) < len(texts):
                text_copy = texts[int(num_text-1)]
                name = text_copy["hero"][0]
                anim = text_copy["hero"][1]
                place = text_copy["hero"][2]
                place = place[0 : len(place)-1]
                return name, place

def scenas(num_text, texts):
        if int(num_text-1) < len(texts):
                text_copy = texts[int(num_text-1)]
                name = text_copy["scena"][0]
                return name[0: len(name)-1]

def play_sound(num_text, texts):
        if int(num_text-1) < len(texts):
                text_copy = texts[int(num_text-1)]
                if len(text_copy["sound"]) > 0:
                        sound = text_copy["sound"][0]
                        sound = sound[0 : len(sound)-1]
                        file_sound = "music/sound/" + str(sound)
                        pygame.mixer.music.load(file_sound)
                        pygame.mixer.music.set_volume(0.8)
                        pygame.mixer.music.play()

def exits(texts, num_text):
        global running
        if int(num_text-1) < len(texts):
                text_copy = texts[int(num_text-1)]
                if  text_copy["exit"]:
                        bool_exit = text_copy["exit"][0]
                        bool_exit = bool_exit[0 : len(bool_exit)-1]
                        if bool_exit == "exit":
                                running = False
        
def find_hero(name):
        for hero in heros_list:
                if hero.name == name:
                        return hero
        return None

def init_text():
        name_text = dialog_line
        heroes_data = {}
        with open (init.FILENAME) as file:
            texts = []
            a = False
            for line in file:
                if line:
                    if line.startswith(dialog_line):
                        text = {"name": [], "lines": [], "otvet": [], "fon": [], "hero": [], "exit": [], "sound": [], "scena": [], "go": []}
                        a = True
                    elif line.startswith("SHE "):
                        a = False
                    elif line.startswith("name ") and a:
                        name = line[5 : ]
                        text["name"].append(name)
                    elif line.startswith("END") and a:
                        texts.append(text)
                        text = {"name": [], "lines": [], "otvet": [], "fon": [], "hero": [], "exit": [], "sound": [], "scena": [], "go": []}
                        a = True
                    elif line.startswith("exit"):
                        text["exit"].append(line)
                    elif line.startswith("hero") and a:
                        name_hero, anim, place = line.split(",")
                        text["hero"].append(name_hero[5:])
                        text["hero"].append(anim)
                        text["hero"].append(place)
                        hero_name = name_hero[5:]
                        if hero_name not in heroes_data:
                                heroes_data[hero_name] = place.strip()
                    elif line.startswith("fon") and a:
                        text["fon"].append(line[4:])
                    elif line.startswith("sound") and a:
                        text["sound"].append(line[6:])
                    elif line.startswith("scena") and a:
                        text["scena"].append(line[6:])
                    elif line.startswith("go") and a:
                        vilka, text_v = line[3:].split(",")
                        if not vilka in dialog_lines:
                                dialog_lines.append(vilka)
                        dop = (vilka, text_v)
                        text["go"].append(dop)
                    elif a:
                        text["lines"].append(line)

        for hero_name, hero_place in heroes_data.items():
                if not find_hero(hero_name):
                        new_hero = Hero(hero_name, hero_place)
                        heros_list.append(new_hero)
                
        return texts

def btn_click(event):
     for i in range(0, len(buttons_rect)):
        if buttons_rect[i].collidepoint((event.pos[0], event.pos[1])):
            return i   

def app_rects(x, y):
        button_rect = pygame.Rect((x, y), (500, 30))
        buttons_rect.append(button_rect)

def draws_variant(texts, screen, num_text, color_text):
        if int(num_text-1) < len(texts):
                text_copy = texts[int(num_text-1)]
                variant = text_copy["go"]
                for i in range(0, len(variant)):
                        line = variant[i][1]
                        line = line[0 : len(line)-1]
                        pusmo = text_font.render(line, True, color_text)
                        screen.blit(pusmo, (WIDTH*0.4+40*i, HEIGHT*0.4+40*i))
                        app_rects(WIDTH*0.4+40*i, HEIGHT*0.4+40*i)
                
                        
        

def draw_dealog(texts, screen, num_text, color_text, scena):
    if int(num_text-1) < len(texts):
        text_copy = texts[int(num_text-1)]
        if len(text_copy["lines"]) <= 2:
                line = text_copy["lines"][0]
                line = line[0 : len(line)-1]
                pusmo = text_font.render(line, True, color_text)
                if scena == "dialod":
                        screen.blit(pusmo, (30, HEIGHT*0.55+10))
                elif scena == "infa":
                        screen.blit(pusmo, (WIDTH*0.01+10, HEIGHT*0.01+10))
        else:
                for i in range(0, len(text_copy["lines"])):
                        line = text_copy["lines"][i]
                        line = line[0 : len(line)-1]
                        pusmo = text_font.render(line, True, color_text)
                        if scena == "dialod":
                                screen.blit(pusmo, (30, HEIGHT*0.55+10+40*i))
                        elif scena == "infa":
                                screen.blit(pusmo, (WIDTH*0.01+10, HEIGHT*0.01+10+40*i))

def dialogs(screen):
    name_surface = pygame.Surface((WIDTH*0.25, 50))     
    name_surface.set_alpha(135)
    text_surface = pygame.Surface((WIDTH*0.97, 300))
    text_surface.set_alpha(125)
    color_text = pygame.Color(int(init.color_texts[0]), int(init.color_texts[1]), int(init.color_texts[2]))
            
    screen.blit(fon, (0, 0))

    screen.blit(img_hero, (x, y))
    
    screen.blit(name_surface, (20, HEIGHT*0.55-50))
    screen.blit(text_surface, (20, HEIGHT*0.55))

    
    ima_text = text_font.render(name_text, True, color_text)
    screen.blit(ima_text, (30, HEIGHT*0.55-40))
    draw_dealog(texts, screen, num_text, color_text, scena)

def draws_infa(screen):
    screen.blit(fon, (0, 0))
        
    text_surface = pygame.Surface((WIDTH*0.98, HEIGHT*0.98))
    text_surface.set_alpha(200)
    color_text = pygame.Color(int(init.color_texts[0]), int(init.color_texts[1]), int(init.color_texts[2]))
    screen.blit(text_surface, (WIDTH*0.01, HEIGHT*0.01))

    draw_dealog(texts, screen, num_text, color_text, scena)

def draws_choice(screen):
    screen.blit(fon, (0, 0))
        
    text_surface = pygame.Surface((WIDTH*0.98, HEIGHT*0.98))
    text_surface.set_alpha(200)
    color_text = pygame.Color(int(init.color_texts[0]), int(init.color_texts[1]), int(init.color_texts[2]))
    screen.blit(text_surface, (WIDTH*0.01, HEIGHT*0.01))

    draws_variant(texts, screen, num_text, color_text)

def var_dialog(var, num_text, texts):
    if int(num_text-1) < len(texts):
        text_copy = texts[int(num_text-1)]
        variant = text_copy["go"]
        line = variant[var][0]
        return line

fon = init.fon
texts = init_text()
name_text = names_text(num_text, texts)                 
print_text = copy_text(num_text, texts)

name, place = creat_hero(num_text, texts)
heros = find_hero(name)
if not heros:
        heros = Hero(name, place)
        heros_list.append(heros)

img_hero, x, y = heros.draw_hero(screen, num_text, texts)
scena = scenas(num_text, texts)

pygame.mixer.music.load(init.musics[music_index])
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play()
music_index += 1
if music_index > len(init.musics):
        music_index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if scena == "dialod":
                        num_text = int(num_text) + int(1)
                        texts = init_text()
                        exits(texts, num_text)
                        scena = scenas(num_text, texts)
                        if len(texts[num_text-1]['sound']) != 0:
                                play_sound(num_text, texts)
                        if scena == "dialod":
                                name_text = names_text(num_text, texts)
                                filefon = fon_import(num_text, fon, texts)
                                fon = init.fons(filefon)
                                if bool_hero(num_text, texts):
                                        name, place = creat_hero(num_text, texts)
                                        heros = find_hero(name)
                                        if heros:
                                                heros.place_move(num_text, texts)
                                                img_hero, x, y = heros.draw_hero(screen, num_text, texts)
                elif scena == "choice":
                        var = btn_click(event)
                        old_dialog_line = dialog_line
                        dialog_line = var_dialog(var, num_text, texts)
                        if not dialog_line in dialog_lines:
                                dialog_lines.append(dialog_line)
                        num_text = int(num_text) + int(1)
                        if old_dialog_line != dialog_line:
                                num_text = 1
                        texts = init_text()
                        scena = scenas(num_text, texts)
                        name_text = names_text(num_text, texts)
                        if bool_hero(num_text, texts):
                                        name, place = creat_hero(num_text, texts)
                                        heros = find_hero(name)
                                        if heros:
                                                heros.place_move(num_text, texts)
                                                img_hero, x, y = heros.draw_hero(screen, num_text, texts)
                elif scena == "infa":
                        pass
        elif event.type == music_end_event:
                pygame.mixer.music.load(init.musics[music_index])
                pygame.mixer.music.set_volume(0.8)
                pygame.mixer.music.play()
                music_index += 1
                if music_index > len(init.musics):
                        music_index = 0
                
                
                
    
    screen.fill((255, 255, 255))
    
    if scena == "dialod":
            dialogs(screen)
    elif scena == "infa":
            draws_infa(screen)
    elif scena == "choice":
            draws_choice(screen)

    
    pygame.display.flip()
    
pygame.quit()
