import pygame
import math
from random import randrange
class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('image/circle.png')
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

		