import pygame

from module.Piece import Piece

class Pawn(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = 'images/' + color + 'P.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 10, board.square_height - 10))

		self.notation = 'P'


	def get_possible_moves(self, board):
		output = []
		moves = []

		# move forward
		if self.color == 'r':
			moves.append((0, -1))
			if not self.has_moved:
				moves.append((0, -2))

		elif self.color == 'b':
			moves.append((1, 0))
			if not self.has_moved:
				moves.append((2, 0))

		elif self.color == 'y':
			moves.append((0, 1))
			if not self.has_moved:
				moves.append((0, 2))

		elif self.color == 'g':
			moves.append((-1, 0))
			if not self.has_moved:
				moves.append((-2, 0))

		for move in moves:
			new_pos = (self.x + move[0], self.y + move[1])
			if new_pos[1] < 14 and new_pos[1] >= 0 and new_pos[0] < 14 and new_pos[1] >= 0 and new_pos not in self.restricted_move:
				output.append(board.get_square_from_pos(new_pos))
		return output


	def get_moves(self, board):
		output = []
		for square in self.get_possible_moves(board):
			if square.occupying_piece != None:
				break
			else:
				output.append(square)

		if self.color == 'r':
			if self.x + 1 < 14 and self.y - 1 >= 0 and (self.x + 1, self.y - 1) not in self.restricted_move:
				square = board.get_square_from_pos(
					(self.x + 1, self.y - 1)
				)
				if square.occupying_piece != None:
					if square.occupying_piece.color != self.color:
						output.append(square)
			if self.x - 1 >= 0 and self.y - 1 >= 0 and (self.x - 1, self.y - 1) not in self.restricted_move:
				square = board.get_square_from_pos(
					(self.x - 1, self.y - 1)
				)
				if square.occupying_piece != None:
					if square.occupying_piece.color != self.color:
						output.append(square)

		elif self.color == 'b':
			if self.x + 1 < 14 and self.y + 1 < 14 and (self.x + 1, self.y + 1) not in self.restricted_move:
				square = board.get_square_from_pos(
					(self.x + 1, self.y + 1)
				)
				if square.occupying_piece != None:
					if square.occupying_piece.color != self.color:
						output.append(square)
			if self.x + 1 < 14 and self.y - 1 >= 0 and (self.x + 1, self.y - 1) not in self.restricted_move:
				square = board.get_square_from_pos(
					(self.x + 1, self.y - 1)
				)
				if square.occupying_piece != None:
					if square.occupying_piece.color != self.color:
						output.append(square)

		elif self.color == 'y':
			if self.x + 1 < 14 and self.y + 1 < 14 and (self.x + 1, self.y + 1) not in self.restricted_move:
				square = board.get_square_from_pos(
					(self.x + 1, self.y + 1)
				)
				if square.occupying_piece != None:
					if square.occupying_piece.color != self.color:
						output.append(square)
			if self.x - 1 >= 0 and self.y + 1 < 14 and (self.x - 1, self.y + 1) not in self.restricted_move:
				square = board.get_square_from_pos(
					(self.x - 1, self.y + 1)
				)
				if square.occupying_piece != None:
					if square.occupying_piece.color != self.color:
						output.append(square)

		elif self.color == 'g':
			if self.x - 1 >= 0 and self.y + 1 < 14 and (self.x - 1, self.y + 1) not in self.restricted_move:
				square = board.get_square_from_pos(
					(self.x - 1, self.y + 1)
				)
				if square.occupying_piece != None:
					if square.occupying_piece.color != self.color:
						output.append(square)
			if self.x - 1 >= 0 and self.y - 1 >= 0 and (self.x - 1, self.y - 1) not in self.restricted_move:
				square = board.get_square_from_pos(
					(self.x - 1, self.y - 1)
				)
				if square.occupying_piece != None:
					if square.occupying_piece.color != self.color:
						output.append(square)
		return output


	def attacking_squares(self, board):
		moves = self.get_moves(board)
		# return the diagonal moves
		if self.color == 'r' or self.color == 'y':
			return [i for i in moves if i.x != self.x]
		else:
			return [i for i in moves if i.y != self.y]