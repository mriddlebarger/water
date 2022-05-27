# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:19:52 2021

"""

#This code archives webcam images
#the code is configured to gather the last 32 days of images

import pandas as pd
from selenium.webdriver import Edge
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import matplotlib.pylab as plt
from ctypes import windll
import datetime
from datetime import datetime
import time
from datetime import datetime, timedelta
import shutil, os
#Clears clipboard
if windll.user32.OpenClipboard(None):
    windll.user32.EmptyClipboard()
    windll.user32.CloseClipboard()
    
downloads = ""
image_date = datetime.today()
image_date = image_date.strftime("%m.%d.%Y")

#make folders
os.mkdir("")
os.mkdir("")

dir1 = ""
dir2 = ""

#opens edge browser, if you do not have the driver, download it here: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
#save the .exe locally and set the variable "driver" to the path
driver = Edge('')

#create series for alarm groups
webcams = ('')
webcams = pd.Series(webcams)
#URL for camera homepage
webcam_page = ''
#search for camera homepage in browser
driver.get(webcam_page)
#input user and pw into login page

#URL for each webcam
webcam1 = ""
webcam2 = ""

#navigate to webcam1
driver.get(webcam1)
#define start date for download window
start = datetime.today() - timedelta(days=4)
date1 = start.strftime("%Y-%m-%d %H:%M:%S")
driver.find_element_by_id("start").send_keys(Keys.CONTROL+"a")
driver.find_element_by_id("start").send_keys(Keys.DELETE)
driver.find_element_by_id("start").send_keys(date1)
driver.find_element_by_class_name('topbar').click()
driver.find_element_by_class_name("download").click()
time.sleep(10)
#for the past 32 days, space start date and end date 4 days apart, download images, iterate to next 4 day period
for i in range(1,9):
    try:
        d1 = timedelta(days=(4*i))
        d1 = start - d1
        date1 = d1.strftime("%Y-%m-%d %H:%M:%S")
        d2 = d1 + timedelta(days=4)
        date2 = d2.strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_id("end").send_keys(Keys.CONTROL+"a")
        driver.find_element_by_id("end").send_keys(Keys.DELETE)
        driver.find_element_by_id("end").send_keys(date2)
        time.sleep(5)
        #refresh webpage
        driver.find_element_by_class_name('topbar').click()
        driver.find_element_by_id("start").send_keys(Keys.CONTROL+"a")
        driver.find_element_by_id("start").send_keys(Keys.DELETE)
        driver.find_element_by_id("start").send_keys(date1)
        #refresh webpage (to enfore the updated image query)
        driver.find_element_by_class_name('topbar').click()
        driver.find_element_by_class_name("download").click()
        time.sleep(20)
    except NoSuchElementException:
            continue
    except ElementClickInterceptedException():
            continue

#path name to downloaded image zip files
zip_files1 = ['']

#copy downloaded image zip files and paste them to dir1
for c in zip_files1:
    shutil.copy(c, dir1)

#navigate to webcam2
driver.get(webcam2)
#define start time 
start = datetime.today() - timedelta(days=10)
date1 = start.strftime("%Y-%m-%d %H:%M:%S")
driver.find_element_by_id("start").send_keys(Keys.CONTROL+"a")
driver.find_element_by_id("start").send_keys(Keys.DELETE)
driver.find_element_by_id("start").send_keys(date1)
driver.find_element_by_class_name('topbar').click()
driver.find_element_by_class_name("download").click()
time.sleep(10)
#for the past 30 days, space start date and end date 4 days apart, download images, iterate to next 4 day period
for i in range(1,4):
    try:
        d1 = timedelta(days=(10*i))
        d1 = start - d1
        date1 = d1.strftime("%Y-%m-%d %H:%M:%S")
        d2 = d1 + timedelta(days=10)
        date2 = d2.strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_id("end").send_keys(Keys.CONTROL+"a")
        driver.find_element_by_id("end").send_keys(Keys.DELETE)
        driver.find_element_by_id("end").send_keys(date2)
        time.sleep(5)
        #refresh webpage
        driver.find_element_by_class_name('topbar').click()
        driver.find_element_by_id("start").send_keys(Keys.CONTROL+"a")
        driver.find_element_by_id("start").send_keys(Keys.DELETE)
        driver.find_element_by_id("start").send_keys(date1)
        #refresh webpage (to enfore the updated image query)
        driver.find_element_by_class_name('topbar').click()
        driver.find_element_by_class_name("download").click()
        time.sleep(20)
    except NoSuchElementException:
            continue
    except ElementClickInterceptedException():
            continue

#path name to downloaded image zip files
zip_files2 = ['']

#copy downloaded image zip files and paste them to dir2
for d in zip_files2:
    shutil.copy(d, dir2)



