import pygame

class Square:
	'''lớp Square dùng để mô tả ô vuông trên bàn cờ bao gồm vị trí, độ dài, rộng của ô vuông,
	vị trí trên màn hình pygame, màu của ô vuông khi vẽ và khi hiển thị các nước đi của quân cờ,
	quân cờ đang ở ô vuông, hình chữ nhật của pygame'''
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
		self.occupying_piece = None
		self.highlight = False
		
		self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)

	def draw(self, screen):
		'''Input là màn hình screen của pygame,
		Có chức năng vẽ các ô vuông và quân cờ trên ô vuông đó,
		Output không trả về gì cả'''
		if self.highlight:
			pygame.draw.rect(screen, self.highlight_color, self.rect)
		else:
			pygame.draw.rect(screen, self.draw_color, self.rect)

		if self.occupying_piece != None:
			centering_rect = self.occupying_piece.img.get_rect()
			centering_rect.center = self.rect.center
			screen.blit(self.occupying_piece.img, centering_rect.topleft)

