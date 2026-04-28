import pygame 
import init
from copy import *

pygame.init()

WIDTH = 2700
HEIGHT = 1400
running = True

print_text = ""
num_text = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("История")

text_font = pygame.font.SysFont(None, 30)

def names_text(num_text):
	texts = init_text()
	if int(num_text-1) < len(texts):
		text_copy = texts[int(num_text-1)]
		return text_copy["name"][0]

def copy_text(num_text):
	texts = init_text()
	if int(num_text-1) < len(texts):
		text_copy = texts[int(num_text-1)]
		return text_copy["lines"][0]

def init_text():
	name_text = "TEXT "
	with open (init.FILENAME) as file:
		texts = []
		for line in file:
			if line:
				if line.startswith(name_text):
					text = {"name": [], "lines": [], "otvet": [], "fon": []}
				elif line.startswith("name "):
					name = line[5 : ]
					text["name"].append(name)
				elif line.startswith("END"):
					texts.append(text)
				elif line.startswith("fon"):
					text["fon"].append(line[4:])
				else:
					text["lines"].append(line)
			
	return texts				

					
print_text = copy_text(num_text)	

while running:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		running = False
    	elif event.type == pygame.MOUSEBUTTONDOWN:
    		if event.button == 1:
    			num_text = int(num_text) + int(1)
    			print_text = copy_text(num_text)
    			names_text = names_text(num_text)
    
    screen.fill((255, 255, 255))
    
    name_surface = pygame.Surface((200, 50))		
    name_surface.set_alpha(135)
    text_surface = pygame.Surface((WIDTH*0.7, 300))
    text_surface.set_alpha(125)
    		
    screen.blit(init.fon, (0, 0))
    screen.blit(name_surface, (20, HEIGHT*0.55-50))
    screen.blit(text_surface, (20, HEIGHT*0.55))
    
    pusmo = text_font.render(names_text, True, (255, 0, 0))
    screen.blit(pusmo, (30, HEIGHT*0.55+10))
    
    pygame.display.flip()
    
pygame.quit()