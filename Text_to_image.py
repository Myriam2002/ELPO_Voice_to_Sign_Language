#imports
import random
import os
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg


#test input to function

text = ["hello", "love"]

#files = os.listdir(path)
#print(files)


#Function to display images from input text
def imgDisplay(text):
    for word in text:
        pathword = "images" + "/" + word
        files = os.listdir(pathword)
        #print(files)
        d=random.choice(files)
        imgpath = pathword+"/"+d

        #printing images: 
        image = mpimg.imread(pathword+"/"+d)
        plt.imshow(image)
        plt.axis('off')
        plt.show()

        #displaying images with wait second = 3

        frame = cv2.imread(imgpath, 0)
        cv2.imshow(word, frame)
        key = cv2.waitKey(3000)#pauses for 3 seconds before fetching next image
        cv2.destroyAllWindows()
        
        if key == 27:#if ESC is pressed, exit loop
            cv2.destroyAllWindows()
            break

#imgDisplay(text)