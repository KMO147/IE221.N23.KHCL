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
	'''lớp Board dùng để mô tả game cờ vua, bao gồm độ cao, rộng của màn hình game,
	cao, rộng của ô vuông, thông báo ở dưới và font của thông báo, quân cờ đang được chọn, 
	số người chơi còn lại, lượt của người chơi hiện tại, các ô vuông của bàn cờ 
	và bàn cờ khởi tạo ở dạng mảng'''
	def __init__(self, width, height, font):
		self.width = width
		self.height = height
		self.square_width = 50
		self.square_height = 50
		self.font = font
		self.selected_piece = None
		self.teams = ['r', 'b', 'y', 'g']
		self.turn = self.teams[0]
		self.decode_teams = {'r': 'Red', 'b': 'Blue', 'y': 'Yellow', 'g': 'Green'}
		self.message = 'Red turn'
		self.message_rect = pygame.Rect(0, 700, 700, 50)
		self.message_rect_color = 'black'

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
		'''Input không có, 
		Ouput là mảng các đối tượng Square'''
		output = []
		for y, row in enumerate(self.board_matrix):
			for x, piece in enumerate(row):
				if piece != ' ':
					output.append(Square(x, y, self.square_width, self.square_height))
		return output

	def generate_players(self):
		'''Input không có, 
		Ouput là mảng các đối tượng Player'''
		output = []
		for color in self.teams:
			output.append(Player(color, self.square_width, self.square_height, self.font))
		return output

	def setup_board(self):
		'''Input và Output không có, 
		Có chức năng khởi tạo các quân cờ và gán quân cờ cho ô vuông tương ứng
		dựa theo bàn cờ khởi tạo ở dạng ma trận'''
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
		'''Input là 1 vị trí (x,y), 
		Ouput là đối tượng Square tương ứng với vị trí (x,y)'''
		for square in self.squares:
			if (square.x, square.y) == (pos[0], pos[1]):
				return square


	def get_piece_from_pos(self, pos):
		'''Input là 1 cặp vị trí (x,y), 
		Ouput là đối tượng quân cờ tương ứng với vị trí (x,y)'''
		return self.get_square_from_pos(pos).occupying_piece


	def get_player_from_color(self, color):
		'''Input là màu của người chơi, 
		Ouput là đối tượng người chơi tướng ứng với màu'''
		for player in self.players:
			if player.color == color:
				return player


	def handle_click(self, mouse_x, mouse_y):
		'''Input là vị trị x,y của chuột khi nhấp chuột trái,
		đây là phương thức dùng để xử lí tác vụ chuột, có thể thực hiện chọn quân cờ,
		và di chuyển quân cờ, 
		Ouput không có'''
		x = mouse_x // self.square_width
		y = mouse_y // self.square_height
		clicked_square = self.get_square_from_pos((x, y))

		if clicked_square is not None:
			if self.selected_piece is None:
				if clicked_square.occupying_piece is not None:
					if clicked_square.occupying_piece.color == self.turn:
						self.selected_piece = clicked_square.occupying_piece

			elif self.selected_piece.move(self, clicked_square):
				self.turn = self.get_next_turn()
				self.message = self.decode_teams[self.turn] + ' turn'

			elif clicked_square.occupying_piece is not None:
				if clicked_square.occupying_piece.color == self.turn:
					self.selected_piece = clicked_square.occupying_piece


	def get_next_turn(self):
		'''Input không có, 
		Output là trả về lượt của người chơi tiếp theo'''
		output = None
		cur_turn = self.teams.index(self.turn)
		last_turn = len(self.teams) - 1
		if cur_turn == last_turn:
			output = self.teams[0]
		else:
			output = self.teams[cur_turn + 1]
		return output


	def get_previous_turn(self):
		'''Input không có, 
		Output là trả về lượt của người chơi trước đó'''
		output = None
		cur_turn = self.teams.index(self.turn)
		last_turn = len(self.teams) - 1
		if cur_turn == 0:
			output = self.teams[last_turn]
		else:
			output = self.teams[cur_turn - 1]
		return output



	def is_in_check(self, color, board_change=None):
		'''Đây là phương thức kiểm tra xe quân vua có đang bị chiếu hay không,
		Input là màu của quân vua hay là của người chơi đang xét, và board_change
		là mảng chứa 2 vị trí [(x1, y1), (x2, y2)], 
		Ouput là True khi quân vua bị chiếu hoặc False khi quân vua không bị chiếu'''
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


	def can_protect_king(self, pieces, color):
		'''Input là mảng các đối tượng Piece và màu của quân đó,
		dùng để xác định xem là các quân cờ có thể bảo vệ quân vua được hay không, 
		Ouput là True khi các quân cờ bảo vệ được quân vua, ngược lại là False'''
		output = False
		for piece in pieces:
			if piece is not None:
				if piece.color == color:
					if piece.get_valid_moves(self) != []:
						output = True
						return output
		return output


	def is_in_checkmate(self, color):
		'''Input màu của người chơi đang xét có bị chiếu tướng hay không, 
		Ouput là True khi người chơi bị chiếu tướng, ngược lại là False'''
		output = False
		pieces = [square.occupying_piece for square in self.squares]
		for piece in pieces:
			if piece is not None:
				if piece.notation == 'K' and piece.color == color:
					king = piece

		if king.get_valid_moves(self) == [] and not self.can_protect_king(pieces, color):
			if self.is_in_check(color):
				# cộng điểm cho người chơi khi chiếu tướng
				self.get_player_from_color(self.get_previous_turn()).score += 20

				if self.turn == color:
					self.turn = self.get_next_turn()
					self.message = self.decode_teams[self.turn] + ' turn'
				# Đổi màu của quân cờ thành xám
				for piece in pieces:
					if piece is not None:
						if piece.color == color:
							piece.color = 'gr'
							piece.lose(self)
				# Loại bỏ team bị chiếu tướng
				self.teams.remove(color)
				output = True

		return output


	def ranking_players(self):
		'''Input và Output không có, 
		đây là phương thức dùng để sắp xếp người chơi theo số điểm từ lớn đến nhỏ'''
		for i in range(len(self.players) - 1):
			for j in range(i + 1, len(self.players)):
				if self.players[i].score < self.players[j].score:
					self.players[i], self.players[j] = self.players[j], self.players[i]


	def show_winner(self):
		'''Input và Output không có, 
		đây là phương thức để thông báo người chiến thắng'''
		self.message = self.decode_teams[self.players[0].color] + " Won!" + " Press Space to restart!"
		self.teams = []
		self.turn = None

	def is_end(self):
		'''Input không có, 
		Ouput là True khi kết thúc game và xác định được người chiến thắng,
		ngượi lại là False'''
		output = False
		self.ranking_players()
		for team in self.teams:
			self.is_in_checkmate(team)
		if len(self.teams) == 2:
			if abs(self.get_player_from_color(self.teams[0]).score - self.get_player_from_color(self.teams[1]).score) > 20:
				output = True
		elif len(self.teams) == 1:
			output = True
		return output


	def draw(self, screen):
		'''Input là màn hình screen của pygame,
		phương thức để vẽ nước đi hợp lệ của quân cờ được chọn, vẽ các ô vuông,
		vẽ điểm và quân cờ ăn được của người chơi và vẽ thông báo ở dưới màn hình, 
		Ouput không có'''
		if self.selected_piece is not None:
			self.get_square_from_pos(self.selected_piece.pos).highlight = True
			for square in self.selected_piece.get_valid_moves(self):
				square.highlight = True

		for square in self.squares:
			square.draw(screen)

		for player in self.players:
			player.draw(screen)

		pygame.draw.rect(screen, self.message_rect_color, self.message_rect)
		self.draw_message = self.font.render(self.message, True, (255,255,255))
		screen.blit(self.draw_message, (0,710))


	def reset(self):
		'''Input và Output không có, 
		đây là phương thức để làm mới lại trò chơi sau khi game kết thúc'''
		self.teams = ['r', 'b', 'y', 'g']
		self.turn = self.teams[0]
		self.message = 'Red turn'
		self.squares = self.generate_squares()
		self.players = self.generate_players()
		self.setup_board()