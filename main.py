# Import  Neccesary Libraries
import pygame
#Initialise required modules
pygame.init()
#Setup window geometry
screen=pygame.display.set_mode((800,700))
#Create a loop to run till the game is quit by the user
done = False
while not done:
    #Clear the event queue
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    #Make the changes visible 
    pygame.display.flip()      
screen.mainloop() 
        