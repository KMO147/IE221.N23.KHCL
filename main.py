import pygame

from module.Board import Board

pygame.init()

window_size = (700, 700)
screen = pygame.display.set_mode(window_size)

font = pygame.font.Font(None, 50)

board = Board(window_size[0], window_size[1], font)

running = True
while running:
	mx, my = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((63,63,63))
	board.draw(screen)
	pygame.display.update()

pygame.quit()