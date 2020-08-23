#!/usr/bin/env python3

from PIL import Image
import os

def fix_images(image_dir, file_type, width, length):
    #This module roates image 90 degrees, resize image and change image format
    for image in os.listdir(image_dir):
        #unsure if I need to add os.path.abspath
        image_location = os.path.join(image_dir,image)
        base = os.path.splitext(image)[0]
        base = base + file_type
        new_image_type = os.path.join(image_dir, base)
        if os.path.isdir(image_location):
            #ignore directories for now.  can be used to extend the filename in the future and make new directories to map original
            pass
        else:
            #process the image
            im = Image.open(image_location)
            new_im = im.resize((width, length)).convert("RGB").save(new_image_type)


if __name__ == "__main__":
    #state the source and destination of the images and teh new file type
    image_dir = ""
    file_type = ".jpeg"
    #state the degree of rotation and new height and width
    width = 600
    length = 400
    fix_images(image_dir, file_type, width, length)
