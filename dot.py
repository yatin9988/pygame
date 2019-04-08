import pygame,sys
pygame.init()
display=pygame.display.set_mode((500,500))
pygame.display.set_caption('SPOT THE DOT')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()    
        pygame.draw.line(display,(255,255,255),(250,250),(250,250),1)
        pygame.display.update()
