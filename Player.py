import pygame
import math
from random import randrange
class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.imagectb = pygame.image.load('image/ctbplayer.png')
		self.rect = self.imagectb.get_rect()
		self.rect.x = 0
		self.rect.y = 450
		self.velocity = 70
		self.velocity_dash = 120 + self.velocity 

	def move_right(self):
		print("droite")
		self.rect.x += self.velocity
	def move_left(self):
		self.rect.x -= self.velocity
	def dash_right(self):
		self.rect.x += self.velocity_dash
	def dash_left(self):
		self.rect.x -= self.velocity_dash
