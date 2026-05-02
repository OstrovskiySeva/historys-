import pygame

color_texts = []

with open("date.txt") as file:
        for line in file:
                if line:
                        line = line.rstrip()
                        if line.startswith("dialog"):
                                FILENAME = line[9 : ]
                        elif line.startswith("fon"):
                                FONFILE = line[6 : ]
                        elif line.startswith("color_text"):
                                lines = line[13:]
                                color_texts = lines.split(",")
                                color_text = ', '.join(color_texts)
                                
                                
				

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
