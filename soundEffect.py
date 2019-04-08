import pygame,time,sys
pygame.init()
display=pygame.display.set_mode((500,500))
pygame.display.set_caption('SOUND EFFECT')
sound1=pygame.mixer.Sound('beep1.wav')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sound1.play()
            time.sleep(1)
            pygame.quit()
            sys.exit()
        
    
            
            
            
    
