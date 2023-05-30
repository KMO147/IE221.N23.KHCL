import pygame

from module.Piece import Piece

class Knight(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = 'images/' + color + 'N.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 10, board.square_height - 10))

		self.notation = 'N'


	def get_possible_moves(self, board):
		output = []
		moves = [
			(1, -2),
			(2, -1),
			(2, 1),
			(1, 2),
			(-1, 2),
			(-2, 1),
			(-2, -1),
			(-1, -2)
		]

		for move in moves:
			new_pos = (self.x + move[0], self.y + move[1])
			if (
				new_pos[0] < 14 and
				new_pos[0] >= 0 and 
				new_pos[1] < 14 and 
				new_pos[1] >= 0 and
				new_pos not in self.restricted_move
			):
				output.append([board.get_square_from_pos(new_pos)])
		return output