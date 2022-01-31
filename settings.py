import pygame
from pygame.locals import *
class Settings:
	"""Store all settings for Soldier Invasion"""
	
	def __init__(self):
		"""Initialize the games settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.screen = pygame.display.set_mode(
			(self.screen_width, self.screen_height))
		self.bg = pygame.image.load('images/background.png').convert()
		
		# cannon settings
		self.cannon_limit = 3
		
		# Bullet settings
		self.bullet_width = 15
		self.bullet_height = 15
		self.bullet_color = (0, 0, 0)
		
		# Soldier settings
		self.fleet_drop_speed = 15
	
		# How quickly the game speeds up
		self.speedup_scale = 1.3
		
		# Point value increase.
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.cannon_speed = 3.0
		self.bullet_speed = 3.0		
		self.soldier_speed = 1.5
		
		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		
		# Scoring
		self.soldier_points = 50
		
	def increase_speed(self):
		"""Increase speed settings."""
		self.cannon_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.soldier_speed *= self.speedup_scale
		
		self.soldier_points = int(self.soldier_points * self.score_scale)

		
