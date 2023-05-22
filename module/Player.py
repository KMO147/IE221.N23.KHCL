import pygame

class Player:
	def __init__ (self, color, width, height, font):
		self.color = color
		self.width = width
		self.height = height
		self.score = 0
		self.draw_score = font.render(str(self.score), True, (0,0,0))

		if self.color == 'r':
			self.rect = pygame.Rect(13 * width, 13 * height, width, height)
			self.draw_color = 'red'
		elif self.color == 'b':
			self.rect = pygame.Rect(0 * width, 13 * height, width, height)
			self.draw_color = 'blue'
		elif self.color == 'y':
			self.rect = pygame.Rect(0 * width, 0 * height, width, height)
			self.draw_color = 'yellow'
		elif self.color == 'g':
			self.rect = pygame.Rect(13 * width, 0 * height, width, height)
			self.draw_color = 'green'

	def draw(self, screen):
		pygame.draw.rect(screen, self.draw_color, self.rect)

		centering_rect = self.draw_score.get_rect()
		centering_rect.center = self.rect.center
		screen.blit(self.draw_score, centering_rect.topleft)