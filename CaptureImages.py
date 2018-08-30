
import FD4LIB
import time
import pygame,sys
from pygame.locals import *
import pygame.camera
 

#Wait til network is ready to start the demo 
#FD4LIB.check_internet()

print("Motor started")
#FD4LIB.motor("Start")
            
Product ="Blue"
Orientation = "000"
imagetype="Good"
abc=""

srno = 1
while True:
        
        action = input('Waiting for next image..   Press Enter once ready.. ');
        srno += 1
        #srno.zfill(3)
        #FD4LIB.capture("start")
        
        iname = "images" +"/"+ Product + imagetype + Orientation + str(srno).rjust(4,'0')+".jpg"
        #print("imagename")
        #print(Product, image)
        
        pygame.init()
        pygame.camera.init()
        cam = pygame.camera.Camera("/dev/video0",(512,512))
        cam.start()
        image= cam.get_image()
        pygame.image.save(image,iname)
        cam.stop()
        
        
        print("Image clicked - stored as ",  iname)
        #time.sleep(2)

       
        

        


        

    


