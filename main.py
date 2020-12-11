import pygame
import math
from Game import Game
pygame.init()

#generer la fenetre du jeux
pygame.display.set_caption("osu")
screen = pygame.display.set_mode((1280, 720))




#Importer une image
banner = pygame.image.load('image/Menu.jpg')
#modifie la taille de l'image
banner = pygame.transform.scale(banner, (1280, 720))


play_button = pygame.image.load('image/Play_button.png')
play_button=pygame.transform.scale(play_button,(400,350))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3)
play_button_rect.y = math.ceil(screen.get_height()/2)


game = Game()

running = True
while running:
	# appliquer l'arriere plan blit permet d'injecter unne image a endroit specifique de la scene
	screen.blit(banner, (0,0))

	#verifier si le jeux est lancer
	if game.is_playing:
		#lance la partie
		game.update(screen)
	else:
		screen.blit(banner,(0,0))
		screen.blit(play_button,play_button_rect)

	

	#il va mettre a jour la scene 
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if play_button_rect.collidepoint(event.pos):
				print("cest vvrai")
				game.is_playing =True
