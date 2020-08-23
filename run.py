#!/usr/bin/env python3

import os
import concurrent.futures
import requests
import locale
import json

#print statements provide additional debugging as needed

#state directory for text files and url for posting
fruits_dir = ""
url = ""

fruits_list = []

def upload_fruit(fruit):
    #print(fruit)
    fruit_dict = {}
    file = os.path.join(fruits_dir, fruit)
    #print(file)
    with open(file) as f:
        fruit_dict["name"] = f.readline().strip()
        fruit_dict["weight"] = int(f.readline().strip("lbs\n"))
        fruit_dict["description"] = " ".join(f.readlines()).replace("\n", "")
        base = os.path.splitext(fruit)[0]
        base = base + ".jpeg"
        fruit_dict["image"] = base
        print(fruit_dict)
        fruits_list.append(fruit_dict)
        post = requests.post(url, data=fruit_dict)


if __name__ == "__main__":
    #state the source and destination of the images and the new file type
    #need to read into list before using pooling
    fruits = os.listdir(fruits_dir)
    #print(fruits)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(upload_fruit, fruits)

output_location = os.path.join(fruits_dir, "fruit_data.json")
with open(output_location, 'w') as outfile:
    json.dump(fruits_list, outfile)
"""
with open(output_location) as json_file:
    sales = json.load(json_file)
    print(sales)
"""
