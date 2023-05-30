import pygame

from module.Square import Square
from module.pieces.Rook import Rook
from module.pieces.Bishop import Bishop
from module.pieces.Knight import Knight
from module.pieces.Queen import Queen
from module.pieces.King import King
from module.pieces.Pawn import Pawn
from module.Player import Player

class Board:
	def __init__(self, width, height, font):
		self.width = width
		self.height = height
		self.square_width = width // 14
		self.square_height = height // 14
		self.font = font
		self.selected_piece = None
		self.teams = ['r', 'b', 'y', 'g']
		self.turn = self.teams[0]
		self.next_turn = self.teams[1]
		self.decode_teams = {'r': 'Red', 'b': 'Blue', 'y': 'Yellow', 'g': 'Green'}

		self.board_matrix = [
			[' ', ' ', ' ', 'yR', 'yN', 'yB', 'yK', 'yQ', 'yB', 'yN', 'yR', ' ', ' ', ' '],
			[' ', ' ', ' ', 'yP', 'yP', 'yP', 'yP', 'yP', 'yP', 'yP', 'yP', ' ', ' ', ' '],
			[' ', ' ', ' ', '', '', '', '', '', '', '', '', ' ', ' ', ' '],
			['bR', 'bP', '', '', '', '', '', '', '', '', '', '', 'gP', 'gR'],
			['bN', 'bP', '', '', '', '', '', '', '', '', '', '', 'gP', 'gN'],
			['bB', 'bP', '', '', '', '', '', '', '', '', '', '', 'gP', 'gB'],
			['bK', 'bP', '', '', '', '', '', '', '', '', '', '', 'gP', 'gQ'],
			['bQ', 'bP', '', '', '', '', '', '', '', '', '', '', 'gP', 'gK'],
			['bB', 'bP', '', '', '', '', '', '', '', '', '', '', 'gP', 'gB'],
			['bN', 'bP', '', '', '', '', '', '', '', '', '', '', 'gP', 'gN'],
			['bR', 'bP', '', '', '', '', '', '', '', '', '', '', 'gP', 'gR'],
			[' ', ' ', ' ', '', '', '', '', '', '', '', '', ' ', ' ', ' '],
			[' ', ' ', ' ', 'rP', 'rP', 'rP', 'rP', 'rP', 'rP', 'rP', 'rP', ' ', ' ', ' '],
			[' ', ' ', ' ', 'rR', 'rN', 'rB', 'rQ', 'rK', 'rB', 'rN', 'rR', ' ', ' ', ' '],
		]

		self.squares = self.generate_squares()
		self.players = self.generate_players()
		self.setup_board()


	def generate_squares(self):
		output = []
		for y, row in enumerate(self.board_matrix):
			for x, piece in enumerate(row):
				if piece != ' ':
					output.append(Square(x, y, self.square_width, self.square_height))
		return output

	def generate_players(self):
		output = []
		for color in self.teams:
			output.append(Player(color, self.square_width, self.square_height, self.font))
		return output

	def setup_board(self):
		for y, row in enumerate(self.board_matrix):
			for x, piece in enumerate(row):
				if piece != ' ' and piece != '':
					square = self.get_square_from_pos((x, y))

					if piece[1] == 'R':
						square.occupying_piece = Rook((x, y), piece[0], self)

					elif piece[1] == 'N':
						square.occupying_piece = Knight((x, y), piece[0], self)

					elif piece[1] == 'B':
						square.occupying_piece = Bishop((x, y), piece[0], self)

					elif piece[1] == 'Q':
						square.occupying_piece = Queen((x, y), piece[0], self)

					elif piece[1] == 'K':
						square.occupying_piece = King((x, y), piece[0], self)

					elif piece[1] == 'P':
						square.occupying_piece = Pawn((x, y), piece[0], self)


	def get_square_from_pos(self, pos):
		for square in self.squares:
			if (square.x, square.y) == (pos[0], pos[1]):
				return square


	def get_piece_from_pos(self, pos):
		return self.get_square_from_pos(pos).occupying_piece


	def get_player_from_color(self, color):
		for player in self.players:
			if player.color == color:
				return player


	def handle_click(self, mouse_x, mouse_y):
		x = mouse_x // self.square_width
		y = mouse_y // self.square_height
		clicked_square = self.get_square_from_pos((x, y))

		if clicked_square is not None:
			if self.selected_piece is None:
				if clicked_square.occupying_piece is not None:
					if clicked_square.occupying_piece.color == self.turn:
						self.selected_piece = clicked_square.occupying_piece

			elif self.selected_piece.move(self, clicked_square):
				cur_turn = self.teams.index(self.turn)
				last_turn = len(self.teams) - 1
				if cur_turn == last_turn:
					self.turn = self.teams[0]
				else:
					self.turn = self.teams[cur_turn + 1]

			elif clicked_square.occupying_piece is not None:
				if clicked_square.occupying_piece.color == self.turn:
					self.selected_piece = clicked_square.occupying_piece


	def is_in_check(self, color, board_change=None):
		output = False
		king_pos = None

		changing_piece = None
		old_square = None
		new_square = None
		new_square_old_piece = None

		if board_change is not None:
			for square in self.squares:
				if square.pos == board_change[0]:
					changing_piece = square.occupying_piece
					old_square = square
					old_square.occupying_piece = None
			for square in self.squares:
				if square.pos == board_change[1]:
					new_square = square
					new_square_old_piece = new_square.occupying_piece
					new_square.occupying_piece = changing_piece

		pieces = [square.occupying_piece for square in self.squares if square.occupying_piece is not None]

		if changing_piece is not None:
			if changing_piece.notation == 'K':
				king_pos = new_square.pos
		if king_pos == None:
			for piece in pieces:
				if piece.notation == 'K':
					if piece.color == color:
						king_pos = piece.pos
		for piece in pieces:
			if piece.color != color and piece.color != 'gr':
				for square in piece.attacking_squares(self):
					if square.pos == king_pos:
						output = True

		if board_change is not None:
			old_square.occupying_piece = changing_piece
			new_square.occupying_piece = new_square_old_piece
						
		return output


	def is_in_checkmate(self, color):
		output = False

		pieces = [square.occupying_piece for square in self.squares]
		for piece in pieces:
			if piece is not None:
				if piece.notation == 'K' and piece.color == color:
					king = piece

		if king.get_valid_moves(self) == []:
			if self.is_in_check(color):
				if self.turn == color:
					self.teams.remove(color)
					for piece in pieces:
						if piece is not None:
							if piece.color == color:
								piece.color = 'gr'
								piece.lose(self)
				output = True

		return output


	def ranking_players(self):
		for i in range(len(self.players) - 1):
			for j in range(i + 1, len(self.players)):
				if self.players[i] > self.players[j]:
					self.players[i], self.players[j] = self.players[j], self.players[i]


	def show_players(self):
		print(self.decode_teams[self.players[0].color] + "Won!")
		for player in self.players:
			print(self.decode_teams[player.color] + ": " + str(player.score))

	def is_end(self):
		output = False

		for team in self.teams:
			self.is_in_checkmate(team)
		if len(self.teams) == 2:
			if abs(self.get_player_from_color(self.teams[0]).score - self.get_player_from_color(self.teams[1])) > 20:
				output = True
				self.ranking_players()
				self.show_players()
		elif len(self.teams) == 1:
			output = True
			self.ranking_players()
			self.show_players

		return output

	def draw(self, screen, mouse_x, mouse_y):
		x = mouse_x // self.square_width
		y = mouse_y // self.square_height
		mouse_square = self.get_square_from_pos((x, y))

		if self.selected_piece is not None:
			self.get_square_from_pos(self.selected_piece.pos).highlight = True
			for square in self.selected_piece.get_valid_moves(self):
				square.highlight = True

		for square in self.squares:
			square.draw(screen)
			if square == mouse_square:
				square.mouse = True
			else:
				square.mouse = False

		for player in self.players:
			player.draw(screen)