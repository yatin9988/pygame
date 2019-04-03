import pygame,sys
pygame.init()
display=pygame.display.set_mode((600,500))
pygame.display.set_caption('ALPHA COLOR EFFECT')
display2=display.convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        display2.fill((255,0,255,198))
        display.blit(display2,(0,0))
        pygame.display.update()

'''remember that in order to use the alpha_color effect we need to generate a
separate surface by the convert_alpha() method on the display surface.
next fill this new surface with color and finally blit it to the original display
surface because pygame.display.update() function is only capable of showing
the state of the original display surface '''
