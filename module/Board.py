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
		self.teams = ['r', 'b', 'y', 'g']

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


	def draw(self, screen):
		for square in self.squares:
			square.draw(screen)
		for player in self.players:
			player.draw(screen)