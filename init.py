import pygame

with open("date.txt") as file:
	for line in file:
		if line:
			line = line.rstrip()
			if line.startswith("dialog"):
				FILENAME = line[9 : ]
			elif line.startswith("fon"):
				FONFILE = line[6 : ]
				

fon = pygame.image.load(FONFILE)