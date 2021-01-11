import pygame
#c'est en fait le mode osu std
from pygame import mixer
from random import randrange
class taiko(pygame.sprite.Sprite):
	"""docstring for Fruit"""
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('image/circle.png')
		self.rect = self.image.get_rect()
		self.rect.x = 720
		self.rect.y = 200
		self.velocity = 1
		self.score = 0
		self.pourcent = 0
		self.fail = 5
		self.x = 1100
		self.y = 200

		#fait tomber le cercle
	def fall(self):
		print(self.rect)
		self.rect.x -= self.velocity
		if self.rect.x <= 0:
			self.fail -=1
			self.rect.y = self.y
			self.rect.x = self.x
			self.velocity += 1

	def WhenYouTouch(self):
		self.velocity += 0.5
		self.score += 1
		self.rect.y = self.y
		self.rect.x = self.x

	def add_pourcent(self):
		self.pourcent +=1
		#recommence toutes les stats
	def reset(self):
		self.velocity = 10
		self.score = 0
		self.pourcent = 0
		self.fail = 5
		#ajoute de la musique
	def song(self):
		file = 'musique/theme.wav'
		mixer.music.load('musique/theme.wav')
		mixer.music.play(-1)
		