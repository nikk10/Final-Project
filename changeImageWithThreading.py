#!/usr/bin/env python3

from PIL import Image
import os
import concurrent.futures
import time

#state image source
image_dir = ""

def fix_images(image):
    #This module resizes the image and changes image format
    old_image_type = os.path.join(image_dir, image)
    #print(old_image_type)
    base = os.path.splitext(image)[0]
    base = base + ".jpeg"
    new_image_type = os.path.join(image_dir, base)
    #print(new_image_type)
    #process the image
    im = Image.open(old_image_type)
    new_im = im.resize((600, 400)).convert("RGB").save(new_image_type)


if __name__ == "__main__":
    #state the source and destination of the images and teh new file type
    #need to read into list before using pooling
    images = os.listdir(image_dir)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(fix_images, images)
    #fix_images(image_dir, file_type, width, length)
