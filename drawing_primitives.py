import pygame,sys
pygame.init()
display=pygame.display.set_mode((800,800))
display2=display.convert_alpha()
pygame.display.set_caption('DRAWING PRIMITIVES')
AQUA=(0,255,255)
BLUE=(0,0,255)
GREEN=(0,128,0)
OLIVE=(128,128,0)
LIME=(0,255,0)
PURPLE=(128,0,128)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()    
        display2.fill((255,0,255,50))
        display.blit(display2,(0,0))
        pygame.draw.line(display,BLUE,(10,50),(790,50),10)
        pygame.draw.circle(display,GREEN,(150,200),100)
        pygame.draw.ellipse(display,LIME,(400,400,350,200),10)
        pygame.draw.rect(display,OLIVE,(400,150,300,200))
        pygame.draw.rect(display,PURPLE,(100,500,200,200))
        pygame.display.update()
        
'''every pygame.draw function takes first two arguments as the surface on
which you want to display and the second is color.the last argument is always
a width parameter'''
