import pygame
from pygame.sprite import Sprite

class Cannon(Sprite):
	"""A class to manage the cannon"""
	
	def __init__(self, ai_game):
		"""Initialize the cannon and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the cannon and get its rect.
		self.image = pygame.image.load('images/cannon.png')
		self.rect = self.image.get_rect()
		
		# Start each new cannon at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom
		
		# Store a decimal value for the cannon's horizontal position.
		self.x = float(self.rect.x)
		
		# Movement flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the cannon's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.cannon_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.cannon_speed
			
		# Update rect object from self.x
		self.rect.x = self.x
		
	def blitme(self):
		"""Draw the cannon at its current location."""
		self.screen.blit(self.image, self.rect)
		
	def center_cannon(self):
		"""Center the cannon on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
