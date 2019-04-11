import pygame,sys
pygame.init()
display=pygame.display.set_mode((400,300))
pygame.display.set_caption('HELLO WORLD')
font=pygame.font.Font('freesansbold.ttf',32)
text=font.render('HELLO WORLD',False,(255,0,0))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        display.blit(text,(100,150))
        pygame.display.update()
