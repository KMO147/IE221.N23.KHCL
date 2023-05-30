import pygame

from module.Piece import Piece

class Queen(Piece):
	def __init__(self, pos, color, board, promoted=False):
		super().__init__(pos, color, board)

		img_path = 'images/' + color + 'Q.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 10, board.square_height - 10))

		self.notation = 'Q'
		self.promoted = promoted

	def get_possible_moves(self, board):
		output = []

		moves_north = []
		for y in range(self.y)[::-1]:
			if (self.x, y) not in self.restricted_move:
				moves_north.append(board.get_square_from_pos(
					(self.x, y)
				))
		output.append(moves_north)

		moves_ne = []
		for i in range(1, 14):
			if self.x + i > 13 or self.y - i < 0 or (self.x + i, self.y - i) in self.restricted_move:
				break
			moves_ne.append(board.get_square_from_pos(
				(self.x + i, self.y - i)
			))
		output.append(moves_ne)

		moves_east = []
		for x in range(self.x + 1, 14):
			if (x, self.y) not in self.restricted_move:
				moves_east.append(board.get_square_from_pos(
					(x, self.y)
				))
		output.append(moves_east)

		moves_se = []
		for i in range(1, 14):
			if self.x + i > 13 or self.y + i > 13 or (self.x + i, self.y + i) in self.restricted_move:
				break
			moves_se.append(board.get_square_from_pos(
				(self.x + i, self.y + i)
			))
		output.append(moves_se)

		moves_south = []
		for y in range(self.y + 1, 14):
			if (self.x, y) not in self.restricted_move:
				moves_south.append(board.get_square_from_pos(
					(self.x, y)
				))
		output.append(moves_south)

		moves_sw = []
		for i in range(1, 14):
			if self.x - i < 0 or self.y + i > 13 or (self.x - i, self.y + i) in self.restricted_move:
				break
			moves_sw.append(board.get_square_from_pos(
				(self.x - i, self.y + i)
			))
		output.append(moves_sw)

		moves_west = []
		for x in range(self.x)[::-1]:
			if (x, self.y) not in self.restricted_move:
				moves_west.append(board.get_square_from_pos(
					(x, self.y)
				))
		output.append(moves_west)

		moves_nw = []
		for i in range(1, 14):
			if self.x - i < 0 or self.y - i < 0 or (self.x - i, self.y - i) in self.restricted_move:
				break
			moves_nw.append(board.get_square_from_pos(
				(self.x - i, self.y - i)
			))
		output.append(moves_nw)

		return output