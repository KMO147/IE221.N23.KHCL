import pygame

from module.Piece import Piece

class Rook(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = 'images/' + color + 'R.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 10, board.square_height - 10))

		self.notation = 'R'


	def get_possible_moves(self, board):
		output = []

		moves_north = []
		for y in range(self.y)[::-1]:
			if (self.x, y) not in self.restricted_move:
				moves_north.append(board.get_square_from_pos(
					(self.x, y)
				))
		output.append(moves_north)

		moves_east = []
		for x in range(self.x + 1, 14):
			if (x, self.y) not in self.restricted_move:
				moves_east.append(board.get_square_from_pos(
					(x, self.y)
				))
		output.append(moves_east)

		moves_south = []
		for y in range(self.y + 1, 14):
			if (self.x, y) not in self.restricted_move:
				moves_south.append(board.get_square_from_pos(
					(self.x, y)
				))
		output.append(moves_south)

		moves_west = []
		for x in range(self.x)[::-1]:
			if (x, self.y) not in self.restricted_move:
				moves_west.append(board.get_square_from_pos(
					(x, self.y)
				))
		output.append(moves_west)

		return output