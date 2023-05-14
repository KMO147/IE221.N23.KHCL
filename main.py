import pygame

from module.Board import Board

pygame.init()

window_size = (700, 700)
screen = pygame.display.set_mode(window_size)

board = Board(window_size[0], window_size[1])

running = True
while running:
	mx, my = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill('white')
	board.draw(screen)
	pygame.display.update()

pygame.quit()