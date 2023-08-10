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
    """
    This function takes the list of words and finds the matching image for it

    returns:
    the image paths of the words to be displayed
    """
    image_paths = []
    for word in text:
        
        # pathword = "images" + "/" + word
        # files = os.listdir(pathword)
        # #print(files)
        # d=random.choice(files)
        # imgpath = pathword+"/"+d
        
        # image_paths.append(imgpath)

        pathword = "images" + "/" + word
        files = os.listdir(pathword)
        
        # Filter out files containing ".DS_Store"
        files = [file for file in files if ".DS_Store" not in file]
        
        if not files:
            return None  # Return None if there are no valid image files
        
        random_file = random.choice(files)
        imgpath = os.path.join(pathword, random_file)

        image_paths.append(imgpath)
        
        # #printing images: 
        # image = mpimg.imread(pathword+"/"+d)
        # plt.imshow(image)
        # plt.axis('off')
        # plt.show()

        #displaying images with wait second = 3
        # frame = cv2.imread(imgpath, 0)
        # cv2.imshow(word, frame)
        # key = cv2.waitKey(3000)#pauses for 3 seconds before fetching next image
        # cv2.destroyAllWindows()
        
        # if key == 27:#if ESC is pressed, exit loop
        #     cv2.destroyAllWindows()
        #     break
    return image_paths

#imgDisplay(text)