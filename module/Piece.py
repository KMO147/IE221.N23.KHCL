import pygame

class Piece:
	'''lớp Piece dùng để mô tả quân cờ bao gồm vị trí, thuộc đội màu nào, 
	đã di chuyển hay chưa, mô tả cách di chuyển của quân cờ, di chuyển quân cờ
	và đổi màu quân cờ thành xám khi bị chiếu tướng'''
	def __init__(self, pos, color, board):
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.color = color
		self.has_moved = False
		self.restricted_move = [(0,0), (0,1), (0,2), (0,11), (0,12), (0,13), 
								(1,0), (1,1), (1,2), (1,11), (1,12), (1,13),
								(2,0), (2,1), (2,2), (2,11), (2,12), (2,13),
								(11,0), (11,1), (11,2), (11,11), (11,12), (11,13),
								(12,0), (12,1), (12,2), (12,11), (12,12), (12,13),
								(13,0), (13,1), (13,2), (13,11), (13,12), (13,13)]

	def move(self, board, square, force=False):
		'''Input là bàn cờ, ô vương mà quân cờ di chuyển 
		và 1 biến force để xác định đây là nước nhập thành, 
		Output là thay đổi vị trí quân cờ và trả về True hoặc False 
		để xác định quân cờ đã di chuyển hay chưa'''
		for i in board.squares:
			i.highlight = False

		if square in self.get_valid_moves(board) or force:
			prev_square = board.get_square_from_pos(self.pos)
			prev_piece = board.get_piece_from_pos(self.pos)
			
			# Cộng điểm cho người chơi khi đi nước ăn quân đối thủ
			captured_piece = square.occupying_piece
			if captured_piece is not None and captured_piece.color != 'gr':
				if captured_piece.notation == 'P':
					board.get_player_from_color(self.color).score += 1
				elif captured_piece.notation == 'Q':
					if captured_piece.promoted:
						board.get_player_from_color(self.color).score += 1
					else:
						board.get_player_from_color(self.color).score += 9
				elif captured_piece.notation == 'B':
					board.get_player_from_color(self.color).score += 5
				elif captured_piece.notation == 'R':
					board.get_player_from_color(self.color).score += 5
				elif captured_piece.notation == 'N':
					board.get_player_from_color(self.color).score += 3
				board.get_player_from_color(self.color).captured_piece.append(captured_piece)

			# Cập nhật vị trí quân cờ
			self.pos, self.x, self.y = square.pos, square.x, square.y
			prev_square.occupying_piece = None
			square.occupying_piece = self
			board.selected_piece = None
			# Cập nhật biến cờ xác nhận quân cờ đã di chuyển ít nhất 1 lần rồi
			self.has_moved = True

			# Quân tốt thăng cấp thành quân hậu
			if self.notation == 'P':
				if (self.y == 6 and self.color == 'r') or (self.y == 7 and self.color == 'y') or (self.x == 7 and self.color == 'b') or (self.x == 6 and self.color == 'g'):
					from module.pieces.Queen import Queen
					square.occupying_piece = Queen((self.x, self.y), self.color, board, promoted = True)

			# Di chuyển quân xe khi quân vua nhập thành
			if self.notation == 'K':
				if self.color == 'r':
					if prev_square.x - self.x == 2:
						rook = board.get_piece_from_pos((3, self.y))
						rook.move(board, board.get_square_from_pos((6, self.y)), force=True)
					elif prev_square.x - self.x == -2:
						rook = board.get_piece_from_pos((10, self.y))
						rook.move(board, board.get_square_from_pos((8, self.y)), force=True)
				elif self.color == 'b':
					if prev_square.y - self.y == 2:
						rook = board.get_piece_from_pos((self.x, 3))
						rook.move(board, board.get_square_from_pos((self.x, 5)), force=True)
					elif prev_square.y - self.y == -2:
						rook = board.get_piece_from_pos((self.x, 10))
						rook.move(board, board.get_square_from_pos((self.x, 7)), force=True)
				elif self.color == 'y':
					if prev_square.x - self.x == 2:
						rook = board.get_piece_from_pos((3, self.y))
						rook.move(board, board.get_square_from_pos((5, self.y)), force=True)
					elif prev_square.x - self.x == -2:
						rook = board.get_piece_from_pos((10, self.y))
						rook.move(board, board.get_square_from_pos((7, self.y)), force=True)
				elif self.color == 'g':
					if prev_square.y - self.y == 2:
						rook = board.get_piece_from_pos((self.x, 3))
						rook.move(board, board.get_square_from_pos((self.x, 6)), force=True)
					elif prev_square.y - self.y == -2:
						rook = board.get_piece_from_pos((self.x, 10))
						rook.move(board, board.get_square_from_pos((self.x, 8)), force=True)
			return True
		else:
			board.selected_piece = None
			return False

	# Đúng cho mọi quân cờ trừ quân tốt
	def get_moves(self, board):
		'''Input là bàn cờ, 
		Output là các đối tượng Square là các nước đi có thể của quân cờ'''
		output = []
		for move in self.get_possible_moves(board):
			for square in move:
				if square.occupying_piece is not None:
					if square.occupying_piece.color == self.color:
						break
					else:
						output.append(square)
						break
				else:
					output.append(square)
		return output


	def get_valid_moves(self, board):
		'''Input là bàn cờ, 
		Output là các đối tượng Square là các nước đi hợp lệ của quân cờ'''
		output = []
		for square in self.get_moves(board):
			if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
				output.append(square)
		return output


	# Đúng cho mọi quân cờ trừ quân tốt
	def attacking_squares(self, board):
		'''Input là bàn cờ, 
		Output là các đối tượng Square là các nước tấn công vào quân cờ đối thủ của quân cờ'''
		return self.get_moves(board)


	def lose(self, board):
		'''Input là bàn cờ, thực hiện đổi màu và ảnh quân cờ của người chơi bị chiếu tướng,
		Output không trả về gì cả'''
		img_path = 'images/' + self.color + self.notation + '.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 10, board.square_height - 10))