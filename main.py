import pygame

from module.Board import Board

pygame.init()

window_size = (700, 750)
screen = pygame.display.set_mode(window_size)

font = pygame.font.Font(None, 50)

board = Board(window_size[0], window_size[1], font)

running = True
while running:
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				board.handle_click(mouse_x, mouse_y)

		if board.is_end():
			board.ranking_player()
			board.show_winner()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				board.reset()

	screen.fill((63,63,63))
	board.draw(screen)
	pygame.display.update()

pygame.quit()