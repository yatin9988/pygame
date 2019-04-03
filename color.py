import pygame,sys
pygame.init()
display=pygame.display.set_mode((600,500))
pygame.display.set_caption('ALPHA COLOR')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        display.fill((255,0,255))    
        pygame.display.update()    
