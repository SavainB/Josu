import pygame
import math
from Game import Game
from pygame import mixer
pygame.init()


#generer la fenetre du jeux
pygame.display.set_caption("osu")
#defini la taille de l'image
screen = pygame.display.set_mode((1280, 720))




#Importer une image
banner = pygame.image.load('image/Menu.jpg')
#modifie la taille de l'image
banner = pygame.transform.scale(banner, (1280, 720))

#charge une image
play_button = pygame.image.load('image/Play_button.png')
#modifie la taille de l'image (x y)
play_button=pygame.transform.scale(play_button,(400,350))
#
play_button_rect = play_button.get_rect()
#place l'image dans la fenetre
play_button_rect.x = math.ceil(screen.get_width()/3)
play_button_rect.y = math.ceil(screen.get_height()/2)

#charge une image
play_ctb = pygame.image.load('image/Play_ctb.png')
#modifie la taille de l'image (x y)
play_ctb=pygame.transform.scale(play_ctb,(400,350))
#
play_ctb_rect = play_button.get_rect()
#place l'image dans la fenetre
play_ctb_rect.x = math.ceil(screen.get_width()/6)
play_ctb_rect.y = math.ceil(screen.get_height()/2)




game = Game()

running = True
while running:

	
	# appliquer l'arriere plan blit permet d'injecter unne image a endroit specifique de la scene
	screen.blit(banner, (0,0))

	#verifier si le jeux est lancer
	if game.is_playing:
		game.update(screen)
	elif game.is_playing_ctb:
		#lance la partie
		game.update_ctb(screen)
	else:
		screen.blit(banner,(0,0))
		screen.blit(play_button,play_button_rect)
		screen.blit(play_ctb,play_ctb_rect)

	

	#il va mettre a jour la scene 
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#si j'appui sur un bouton 
			if play_button_rect.collidepoint(event.pos):
				if game.is_playing_ctb == False:
					game.is_playing = True
			elif play_ctb_rect.collidepoint(event.pos):
				if game.is_playing == False:
					game.is_playing_ctb = True
