import pygame
from pygame.sprite import Sprite

class Soldier(Sprite):
	"""A class to represent a single soldier in the fleet."""
	
	def __init__(self, ai_game):
		"""Initialize the soldier and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		# We call screen on every module because each game element
		# needs its own 'surface' to run.
		
		self.settings = ai_game.settings
		
		# Load the soldier image and set its rect attribute.
		self.image = pygame.image.load('images/soldier.png')
		self.rect = self.image.get_rect()
		
		# Start each new soldier near the top left of the screen.
		# Using its own width and height just moves it to a location one away of itself.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# Store the soldier's exact horizontal position.
		self.x = float(self.rect.x)
		
	def check_edges(self):
		"""Return True if soldier is at edge of screen."""
		screen_rect = self.screen.get_rect()
		
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
		
	def update(self):
		"""Move the soldier to the right."""
		self.x += (self.settings.soldier_speed * 
						self.settings.fleet_direction)
		self.rect.x = self.x
	
	
