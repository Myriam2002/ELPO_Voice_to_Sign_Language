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
        pathword = "images" + "/" + word
        files = os.listdir(pathword)
        
        # Filter out files containing ".DS_Store"
        files = [file for file in files if ".DS_Store" not in file]
        
        if not files:
            return None  # Return None if there are no valid image files
        
        random_file = random.choice(files)
        imgpath = os.path.join(pathword, random_file)

        image_paths.append(imgpath)
       
    return image_paths

#imgDisplay(text)