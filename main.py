

import pygame
#import player
import tigre

pygame.init()


ancho_ventana = 800
alto_ventana = 480
screen=pygame.display.set_mode([ancho_ventana,alto_ventana])
pygame.display.set_caption ( "gladeadores por siempre")
clock = pygame.time.Clock()
#player = player.Kate((ancho_ventana/2), alto_ventana)
tigre= tigre.Tigre((ancho_ventana/2, alto_ventana/2))
game_over = False


while game_over== False:

	for  event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
	tigre.handle_event(event)
	#player.handle_event(event)
	screen.fill(pygame.Color('gray'))
	#screen.blit(player.image, player.rect)
	screen.blit(tigre.image, tigre.rect)

	pygame.display.flip()
	clock.tick(5)

pygame.quit ()
