import pygame
import init

pygame.init()

info_display = pygame.display.Info()

WIDTH = info_display.current_w
HEIGHT = info_display.current_h

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
