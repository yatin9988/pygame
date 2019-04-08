import pygame,sys,time
pygame.init()
display=pygame.display.set_mode((500,500))
pygame.display.set_caption('SOUND AND MUSIC')
sound=pygame.mixer.Sound('beep1.wav')
pygame.mixer.music.load('song2.wav')
pygame.mixer.music.play(1,0.0)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sound.play()
            time.sleep(1)
            pygame.quit()
            sys.exit()
