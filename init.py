import pygame
import os

color_texts = []
hero_color = {}

fon_img = pygame.image.load("img/fon/fon_menu.png")
button_img = pygame.image.load("img/button.png")
button_st_img = pygame.image.load("img/button_st.png")
btn_play_img = pygame.image.load("img/btn_play.png")

with open("date.txt") as file:
        for line in file:
                if line:
                        line = line.rstrip()
                        if line.startswith("num_lvl"):
                                num_lvl = line[8:]
                                #FILENAME = line[9 : ]
                        if line.startswith("fon"):
                                FONFILE = line[6 : ]
                        elif line.startswith("color_text"):
                                lines = line[13:]
                                color_texts = lines.split(",")
                                color_text = ', '.join(color_texts)
                        elif line.startswith("color_h"):
                                lines = line[10:]
                                color_h = lines.split(",")
                                key = color_h[0]
                                color_h = color_h[1:]
                                hero_color[key] = color_h
                                
                                
				

fon = pygame.image.load("img/fon/" + str(FONFILE))

def fons(filefon):
        if filefon:
                filefon = "img/fon/" + str(filefon)
                fon = pygame.image.load(filefon)
                return fon

def hero_init(file_img):
        if file_img:
                hero_img = pygame.image.load(file_img).convert_alpha()
                return hero_img
pygame.mixer.init()
musics = []

with open("date.txt") as file:
        for line in file:
                if line:
                        line = line.rstrip()
                        if line.startswith("music"):
                                filemusic = line[8:]
                                musics.append(filemusic)
papka = "anim1"
def list_fon(papka):
        list_fon = []
        files = os.listdir("img/anim/" + papka)
        for i in files:
                list_fon.append(pygame.image.load("img/anim/" + papka + "/" + i))
        return list_fon

list_fon(papka)

def list_level():
        put = "dialog"
        list_files = os.listdir(put)
        return list_files

def files():
        list_files = list_level()
        FILENAME = "dialog/" + str(list_files[int(num_lvl)-1])
        return FILENAME
