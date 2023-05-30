import pygame

class Square:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.abs_x = x * width
		self.abs_y = y * height
		self.abs_pos = (self.abs_x, self.abs_y)
		self.pos = (x, y)
		self.draw_color = 'white' if (x + y) % 2 == 0 else 'gray'
		self.highlight_color = (150, 255, 100) if self.draw_color == 'white' else (50, 220, 0)
		self.mouse_color = (0, 0, 255)
		self.occupying_piece = None
		self.highlight = False
		self.mouse = False
		
		self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)

	def draw(self, screen):
		if self.highlight:
			pygame.draw.rect(screen, self.highlight_color, self.rect)
		else:
			pygame.draw.rect(screen, self.draw_color, self.rect)

		if self.mouse:
			pygame.draw.rect(screen, self.mouse_color, self.rect)

		if self.occupying_piece != None:
			centering_rect = self.occupying_piece.img.get_rect()
			centering_rect.center = self.rect.center
			screen.blit(self.occupying_piece.img, centering_rect.topleft)

