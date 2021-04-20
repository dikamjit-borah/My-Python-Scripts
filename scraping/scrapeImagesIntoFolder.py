from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
import random
#from urllib import urlopen

import os
import requests

from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


products = ["Photo Frame", "Press Machine", "Printing Machine", "Mobile Cover", "Cutting Machine", "Badge Printing Machine", "Heat Press Machines", "Sublimation T Shirts", "Sublimation Cushion", "Sublimation Mugs", "Mug Printing Machine", "Customised Clock", "T Shirt Printing Machine", "Sublimation Paper", "Vinyl cutting plotter", "Uv Printing Machine", "Wall Clock", "T-SHIRT VINYLS AND ALL TYPES OF VINYLS", "Momentos", "mobile cover print machine", "Sublimation Mobile Blank Covers", "Lanyard Machine", "ID Card and Paper Cutter", "Photo on Plate", "MOBILE COVER PRINTING MACHINE", "badge-machine", "ST-420 Heat Press Transfer Machine", "Face Mask And Surgical Gown", "Sublimation Pop Socket Mobile", "Lamination Machine", "Mobile Cover Mould", "Sublinova Sublimation Ink", "Sub Hardboard Sheets", "B WCHB Clock", "Sublimation Cosmetic Mirrors", "Cushion", "SUBLIMATION TILES", "Pencil Pouch", "New Items"]

#products = ["Photo Frame"]

product_endPoints = []


def makeValidEndPoint():
    for product in products:

        product = product.lower().replace(" ", "-")

        product_endPoints.append(product)


def sleep(t):
    time.sleep(t)


if __name__ == "__main__":

    BASE_URL = "https://www.bengalphoto.in/"
    parent_dir = "E:/Programming/BengalPhoto/photos"
   # open_Browser = webdriver.Chrome(ChromeDriverManager().install())
    makeValidEndPoint()

    for endPoint in product_endPoints:
        folder_name = ""+endPoint
        path = os.path.join(parent_dir, folder_name)
        try:
            os.mkdir(path)
        except:
            pass

        url = ""+BASE_URL+endPoint+".html"
        print(""+url)
        # open_Browser.get(url)
        sleep(2)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        try:
            mydivs = soup.find_all("img", {"class": "max-hw"})
            imgs = []
            try:
                count = 0
                for div in mydivs:
                    imgs.append(mydivs[count]['data-bimg'])
                    count = count + 1
            except:
                print(imgs[0])
                pass

            try:
                count = 0
                
                for img in imgs:
                    name_of_file ="" + endPoint + str(count) + "" 
                    print(name_of_file)
                    filePath = os.path.join(path, name_of_file+".jpg")  
                    print(filePath)  
                 

                    f = open(filePath, 'wb')
                    f.write(requests.get(img).content)
                    f.close()
                    count = count+1
            except:
                 print("Something's wrong, downloading and writing image")
        except:
            print("Something's wrong, main for loop")
            continue

    print("Going to next page")

# open_Browser.get(BASE_URL)
sleep(random.randint(3, 6))
