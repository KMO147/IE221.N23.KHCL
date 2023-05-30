import pygame

from module.Piece import Piece

class King(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = 'images/' + color + 'K.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 10, board.square_height - 10))

		self.notation = 'K'


	def get_possible_moves(self, board):
		output = []
		moves = [
			(0,-1), # north
			(1, -1), # ne
			(1, 0), # east
			(1, 1), # se
			(0, 1), # south
			(-1, 1), # sw
			(-1, 0), # west
			(-1, -1), # nw
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


	def can_castle(self, board):
		if not self.has_moved:

			if self.color == 'r':
				queenside_rook = board.get_piece_from_pos((3, 13))
				kingside_rook = board.get_piece_from_pos((10, 13))
				if queenside_rook != None:
					if not queenside_rook.has_moved:
						if [board.get_piece_from_pos((i, 13)) for i in range(4, 7)] == [None, None, None]:
							return 'queenside'
				if kingside_rook != None:
					if not kingside_rook.has_moved:
						if [board.get_piece_from_pos((i, 13)) for i in range(8, 10)] == [None, None]:
							return 'kingside'

			elif self.color == 'b':
				queenside_rook = board.get_piece_from_pos((0, 10))
				kingside_rook = board.get_piece_from_pos((0, 4))
				if queenside_rook != None:
					if not queenside_rook.has_moved:
						if [board.get_piece_from_pos((0, i)) for i in range(7, 10)] == [None, None, None]:
							return 'queenside'
				if kingside_rook != None:
					if not kingside_rook.has_moved:
						if [board.get_piece_from_pos((0, i)) for i in range(4, 6)] == [None, None]:
							return 'kingside'

			elif self.color == 'y':
				queenside_rook = board.get_piece_from_pos((10, 0))
				kingside_rook = board.get_piece_from_pos((3, 0))
				if queenside_rook != None:
					if not queenside_rook.has_moved:
						if [board.get_piece_from_pos((i, 0)) for i in range(7, 10)] == [None, None, None]:
							return 'queenside'
				if kingside_rook != None:
					if not kingside_rook.has_moved:
						if [board.get_piece_from_pos((i, 0)) for i in range(4, 6)] == [None, None]:
							return 'kingside'

			elif self.color == 'g':
				queenside_rook = board.get_piece_from_pos((13, 3))
				kingside_rook = board.get_piece_from_pos((13, 10))
				if queenside_rook != None:
					if not queenside_rook.has_moved:
						if [board.get_piece_from_pos((13, i)) for i in range(4, 7)] == [None, None, None]:
							return 'queenside'
				if kingside_rook != None:
					if not kingside_rook.has_moved:
						if [board.get_piece_from_pos((13, i)) for i in range(8, 10)] == [None, None]:
							return 'kingside'


	def get_valid_moves(self, board):
		output = []
		for square in self.get_moves(board):
			if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
				output.append(square)
		if self.color == 'r':
			if self.can_castle(board) == 'queenside':
				output.append(board.get_square_from_pos((self.x - 2, self.y)))
			if self.can_castle(board) == 'kingside':
				output.append(board.get_square_from_pos((self.x + 2, self.y)))
		elif self.color == 'b':
			if self.can_castle(board) == 'queenside':
				output.append(board.get_square_from_pos((self.x, self.y + 2)))
			if self.can_castle(board) == 'kingside':
				output.append(board.get_square_from_pos((self.x, self.y - 2)))
		elif self.color == 'y':
			if self.can_castle(board) == 'queenside':
				output.append(board.get_square_from_pos((self.x + 2, self.y)))
			if self.can_castle(board) == 'kingside':
				output.append(board.get_square_from_pos((self.x - 2, self.y)))
		elif self.color == 'g':
			if self.can_castle(board) == 'queenside':
				output.append(board.get_square_from_pos((self.x, self.y - 2)))
			if self.can_castle(board) == 'kingside':
				output.append(board.get_square_from_pos((self.x, self.y + 2)))
		return output