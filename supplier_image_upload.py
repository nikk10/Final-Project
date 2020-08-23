#!/usr/bin/env python3

import os
import concurrent.futures
import requests

#state directory for image files and url for posting
image_dir = ""
url = ""

def upload_images(image):
    file_full_path = os.path.join(image_dir, image)
    with open (file_full_path, "rb") as opened:
        r = requests.post(url, files = {"file":opened})



if __name__ == "__main__":
    #state the source and destination of the images and teh new file type
    #need to read into list before using pooling
    images = []
    for image in os.listdir(image_dir):
        if (os.path.splitext(image)[1]) == ".jpeg":
            images.append(image)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(upload_images, images)
