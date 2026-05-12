import pygame
import init

pygame.init()

info_display = pygame.display.Info()

WIDTH = info_display.current_w
HEIGHT = info_display.current_h

class Anim_fon:
        def __init__(self, Anim_fon):
                self.papka = Anim_fon

        def inits_img(self):
                self.an = init.list_fon(self.papka)
                image = init.list_fon(self.papka)
                return image

        def draw_fon(self, num):
            if num <= len(self.inits_img()):
                image = self.inits_img()[num]
                return image
