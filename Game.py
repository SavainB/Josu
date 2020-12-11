import pygame
from Player import Player
import time
from random import randrange
class Game():
	def __init__(self):
		self.player = Player()
		self.is_playing = False
		


	def update(self,screen):
		merde = 0
		#je dois mettre le code du jeux ici 
		background = pygame.image.load('image/menu.jpg')
		background = pygame.transform.scale(background, (1280, 720))
		screen.blit(background,(0,0))
		while merde<1:
			time_in_sec=int(0.9)
			for times in range(time_in_sec):
				time.sleep(1)
			print("Time is up")
			screen.blit(self.player.image, self.player.rect)
			self.player.rect.x = randrange(500)
			self.player.rect.y = randrange(500)
			merde +=1
		
