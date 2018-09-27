import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
from pygame.locals import * 

pygame.init()
screen = pygame.display.set_mode([320, 240]) 

quit = False
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
	
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[K_UP]:
                GPIO.output(16, False)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, True) 
                print ("FORWARD Pressed")
		    		    
            elif key[K_DOWN]:
                print ("BACKWARD Pressed")
                GPIO.output(16, True)
                GPIO.output(11, True)
                GPIO.output(13, False)
                GPIO.output(15, False)
                                         
            elif key[K_LEFT]:
                print ("LEFT Pressed")
                GPIO.output(16, False)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
                    
            elif key[K_RIGHT]: 
                print ("RIGHT Pressed")
                GPIO.output(16, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, True)    

            elif key[K_SPACE]:
                print ("Stop")
                GPIO.output(16, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)

        elif event.type == pygame.KEYUP:
            if event.key == K_UP:
                GPIO.output(16, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
            elif event.key == K_DOWN:
                GPIO.output(16, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
            elif event.key == K_LEFT:
                GPIO.output(16, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
            elif event.key == K_RIGHT:
                GPIO.output(16, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
                

                
pygame.display.quit()
pygame.quit()
