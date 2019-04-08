import pygame,sys
pygame.init()
display=pygame.display.set_mode((200,200))
pygame.mixer.music.load('song2.wav')
pygame.mixer.music.play(-1,0)
pygame.display.set_caption('LET ME LOVE YOU')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
