import pygame

class Player:
	'''lớp Player dùng để mô tả người chơi bao gồm thuộc màu nào hay đội màu nào,
	độ cao, rộng của ô điểm, điểm số có được, font của điểm số, các quân cờ đã ăn,
	hình chữ nhật và màu của hình chữ nhật chứa điểm của người chơi'''
	def __init__ (self, color, width, height, font):
		self.color = color
		self.width = width
		self.height = height
		self.score = 0
		self.font = font
		self.captured_piece = []

		if self.color == 'r':
			self.rect = pygame.Rect(13 * width, 12 * height, width, height)
			self.draw_color = 'red'
		elif self.color == 'b':
			self.rect = pygame.Rect(0 * width, 12 * height, width, height)
			self.draw_color = 'blue'
		elif self.color == 'y':
			self.rect = pygame.Rect(0 * width, 1 * height, width, height)
			self.draw_color = 'yellow'
		elif self.color == 'g':
			self.rect = pygame.Rect(13 * width, 1 * height, width, height)
			self.draw_color = 'green'

	def draw(self, screen):
		'''Input là màn hình screen của pygame,
		Có chức năng vẽ ô chữ nhật, và điểm số của người trên hình chữ nhật đó,
		và vẽ các quân cờ ăn được
		Output không trả về gì cả'''
		pygame.draw.rect(screen, self.draw_color, self.rect)

		self.draw_score = self.font.render(str(self.score), True, (0,0,0))
		centering_rect = self.draw_score.get_rect()
		centering_rect.center = self.rect.center
		screen.blit(self.draw_score, centering_rect.topleft)

		for idx, piece in enumerate(self.captured_piece):
			captured_piece_img = pygame.transform.scale(piece.img, (20, 20))
			if idx <= 6:
				if self.color == 'r':
					screen.blit(captured_piece_img, (550 + idx * 20 , 680))
				elif self.color == 'b':
					screen.blit(captured_piece_img, (130 - idx * 20, 680))
				elif self.color == 'y':
					screen.blit(captured_piece_img, (130 - idx * 20, 0))
				elif self.color == 'g':
					screen.blit(captured_piece_img, (550 + idx * 20, 0))
			elif idx <= 13:
				if self.color == 'r':
					screen.blit(captured_piece_img, (550 + idx%7 * 20 , 660))
				elif self.color == 'b':
					screen.blit(captured_piece_img, (130 - idx%7 * 20, 660))
				elif self.color == 'y':
					screen.blit(captured_piece_img, (130 - idx%7 * 20, 20))
				elif self.color == 'g':
					screen.blit(captured_piece_img, (550 + idx%7 * 20, 20))
			else:
				if self.color == 'r':
					screen.blit(captured_piece_img, (550 + idx%7 * 20 , 640))
				elif self.color == 'b':
					screen.blit(captured_piece_img, (130 - idx%7 * 20, 640))
				elif self.color == 'y':
					screen.blit(captured_piece_img, (130 - idx%7 * 20, 40))
				elif self.color == 'g':
					screen.blit(captured_piece_img, (550 + idx%7 * 20, 40))