import pygame,sys
pygame.init()
display=pygame.display.set_mode((400,300))
pygame.display.set_caption('HELLO WORLD')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()    
