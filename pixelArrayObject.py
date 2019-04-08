import pygame,sys,time
pygame.init()
display=pygame.display.set_mode((600,600))
pygame.display.set_caption('PIXEL ARRAY OBJECT')
pixel=pygame.PixelArray(display)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
l=[RED,GREEN,BLUE]
# locks the surface so that no more items like images can be blitted on the surface.
# but drawing functions can still be called on it.
posx=300
posy=0
i=0
while(posy!=600):
    pixel[posx][posy]=l[i%3]
    posy+=10
    i+=1
    time.sleep(1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()    
del pixel
# surface unlocked for blitting

