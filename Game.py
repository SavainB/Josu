import pygame
from Player import Player
import time, threading
from random import randrange
from Mode_ctb import Fruit
from Mode_osu import std
from pygame import mixer
from Mode_taiko import taiko
import math
class Game():
	def __init__(self):
		self.player = Player()
		self.std = std()
		self.fruit = Fruit()
		self.taiko = taiko()
		self.pressed = {}
		self.is_playing = False
		self.is_playing_ctb = False
		self.std.song()	

		#autre mode de jeux ên construction
	def update_ctb(self,screen):
		#ajoute du texte
			font = pygame.font.Font("freesansbold.ttf", 50)
			textScore = font.render("CTBscore :"+str(self.std.score),True,(255,255,255))
			textVie = font.render("Vie :"+str(self.std.fail),True,(255,255,255))
			#pour la boucle en bas
			boucle = True

			background = pygame.image.load('image/menu.jpg')
			background = pygame.transform.scale(background, (1280, 720))

			screen.blit(background,(0,0))

			screen.blit(self.player.imagectb,self.player.rect)

			#recupere les touche si droite ou gauche
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT:
						self.player.move_right()
						screen.blit(self.player.imagectb,self.player.rect)
					if event.key == pygame.K_LEFT:
						self.player.move_left()
						screen.blit(self.player.imagectb,self.player.rect)
						

			while boucle:
				#lorsque le perso est en contact avec lobjet tombant
				if self.player.rect.colliderect(self.std.rect):
					self.std.WhenYouTouch()
							
				screen.blit(textScore, (0, 0))
				screen.blit(textVie, (0, 50))
				if self.std.fail <=0:
					#change d'interface
					self.update_Defaite(screen)
					break

				self.std.fall()
				screen.blit(self.std.image, self.std.rect)
				boucle = False
			
			#le mode ctb 
	def update(self,screen):
			#ajoute du texte
			font = pygame.font.Font("freesansbold.ttf", 50)
			textScore = font.render("OSUScore :"+str(self.std.score),True,(255,255,255))
			textVie = font.render("Vie :"+str(self.std.fail),True,(255,255,255))
			#pour la boucle en bas
			boucle = True

			background = pygame.image.load('image/menu.jpg')
			background = pygame.transform.scale(background, (1280, 720))
			screen.blit(background,(0,0))

			#lorsque le joueur touche un cercle
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.std.rect.collidepoint(event.pos):
						self.std.WhenYouTouch()
						print("ta gagner un point vous avez ["+str(self.std.score)+"] de point")

			while boucle:
				screen.blit(textScore, (0, 0))
				screen.blit(textVie, (0, 50))
				if self.std.fail <=0:
					#change d'interface
					self.update_Defaite(screen)
					break

				self.std.fall()
				screen.blit(self.std.image, self.std.rect)
				boucle = False

	#interface defaite 			
	def update_Defaite(self,screen):
		#charge une image
		boutonQuit = pygame.image.load('image/bouton_quit.png')
		#modifie la taille de l'image (x y)
		boutonQuit=pygame.transform.scale(boutonQuit,(200,70))
		#
		boutonQuitRect = boutonQuit.get_rect()
		#place l'image dans la fenetre
		boutonQuitRect.x = math.ceil(screen.get_width()/2.5)
		boutonQuitRect.y = math.ceil(screen.get_height()/3)
		screen.blit(boutonQuit,boutonQuitRect)	
		pygame.display.flip()
		#si j'appui sur le bouton quit
		for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if boutonQuitRect.collidepoint(event.pos):
						self.is_playing = False
						self.is_playing_ctb = False
						self.std.reset()
						self.std.song()
	def update_taiko(self,screen):
			#ajoute du texte
			font = pygame.font.Font("freesansbold.ttf", 50)
			textScore = font.render("TaikScore :"+str(self.taiko.score),True,(255,255,255))
			textVie = font.render("Vie :"+str(self.taiko.fail),True,(255,255,255))
			#pour la boucle en bas
			boucle = True

			background = pygame.image.load('image/menu.jpg')
			background = pygame.transform.scale(background, (1280, 720))
			screen.blit(background,(0,0))
			#lorsque le joueur touche un cercle
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.taiko.rect.collidepoint(event.pos):
						self.taiko.WhenYouTouch()
						print("ta gagner un point vous avez ["+str(self.taiko.score)+"] de point")

			while boucle:
				screen.blit(textScore, (0, 0))
				screen.blit(textVie, (0, 50))
				if self.taiko.fail <=0:
					#change d'interface
					self.update_Defaite(screen)
					break

				self.taiko.fall()
				screen.blit(self.taiko.image, self.taiko.rect)
				boucle = False
