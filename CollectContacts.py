# -*- coding: utf-8 -*- TEST
"""
Created on Mon Jan  4 20:12:30 2021
"""

#This code collects the contact data, then generates \n
#writes to csvs and charts histogram
#Be sure to have the browser configured correctly to this code, or modify the \n
#code to work with browser

import pandas as pd
from selenium.webdriver import Edge
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import matplotlib.pylab as plt
import seaborn as sns
from ctypes import windll
import datetime
from datetime import datetime
import time
import os
#Clear clipboard
if windll.user32.OpenClipboard(None):
    windll.user32.EmptyClipboard()
    windll.user32.CloseClipboard()

#Specify date (mmddyy)
date = datetime.now()
date = date.strftime("%m%d%Y")

#Path to write data
path = ''
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(path)

#open edge browser, if not running on local computer, provide path to Microsoft \n
#Edge driver
#You may need to periodically update this driver, see \n
#https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
driver = Edge('')
#create series for alarm groups
alarm_group = ('')
alarm_group = pd.Series(alarm_group)
#URL location of alarm groups
alarm_group_list = ''
#search alarm_group_list in browser
driver.get(alarm_group_list)
#input username and pw into login page

#select all text on alarm group page, copy to clipboard
driver.find_element_by_partial_link_text('#').send_keys(Keys.CONTROL + "a")
driver.find_element_by_partial_link_text('#').send_keys(Keys.CONTROL + "c")
#create dataframe with data from clipboard
test = pd.read_clipboard('\r\t')
#trim excess data from dataframe
test = test.iloc[7:40]
test = test[2::3]
#trim " Members" from the number of alarm contacts, convert string to int
test = test.replace({' Members':''}, regex = True)
test = test.astype(int)
#name column Members
test.columns = ['Members']
#reset index
test = test.reset_index(drop=True)
#sum all alerts to get total signups
alert_total = test.sum()
alert_total = str(test.sum())
#remove text from total signups
alert_total = alert_total.replace ("Members", "")
alert_total = alert_total.replace ("dtype: int64", "")
alert_total = alert_total.replace ("    ", "")
#concantenate alarm group series with alarm group members data
result = pd.concat([alarm_group,test], axis=1)
#rearrange dataframe so alarm groups are in numerical order
idx = result.index.tolist()
idx.pop(1)
idx.pop(1)
result = result.reindex(idx +[1]+[2])
result = result.reset_index(drop=True)
#rename columns
result.columns = ['Alarm Group','Members']
#create histogram of contacts for each alarm group
plot = sns.barplot(x=result['Alarm Group'], y=result['Members'], color = 'b')
plot.set_xticklabels(plot.get_xticklabels(), rotation=90)
plot = sns.barplot(x=result['Alarm Group'], y=result['Members'], color = 'b')
txt="Created at"+" "+datetime.now().strftime("%m-%d-%Y_%I:%M_%p")
txt1="Total Gage Signups:"+str(alert_total)
# align text
plot.text(.5, -180, txt, ha='center')
plot.text(5, 180, txt1, ha='center')
plt.savefig(path+"/"+'FloodWarningSystem'+date+".png", bbox_inches = "tight")
#create list of alarm group urls
alarm_url = [""]
#create list of alarm group names
group_name = ['']
#iterate throught the alarm group urls, creating one dataframe of contacts for each alarm group
for i, j in zip(alarm_url, group_name):
    driver.get(i)
    #filter contacts who are subscribed, ctrl+a, ctrl+c (aka copy all data, paste to dataframe)
    driver.find_element_by_id("dropdown-button-filter-enabled").click()
    driver.find_element_by_link_text("Yes").click()
    driver.find_element_by_partial_link_text('@').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_partial_link_text('@').send_keys(Keys.CONTROL + "c")
    #create dataframe using data from clipboard
    data = pd.read_clipboard('\r\t')
    #trim excess data
    data = data.iloc[21:-1]
    #create column with emails and names, and separate those joined by semicolon
    df1 = (data.assign(semi_colon = data['Search'].str.split(';')).explode('semi_colon')
         .reset_index(drop=True))
    #create column with emails and names, and separate those joined by comma
    df1 = (df1.assign(comma = df1['semi_colon'].str.split(','))
         .explode('comma').reset_index(drop=True))
    #create column of boolean values if string contrains email address
    df1['email'] = df1['comma'].str.contains("@")
    #create column for where boolean = True for containing an email address
    df1['email_address'] = df1['comma'].where(df1['email'] == True)
    #create column where boolean = False therefore it must be a name
    df1['name'] = df1['comma'].where(df1['email'] == False)
    df1 = df1.drop(['email','Search','semi_colon'],1)
    df1.columns = ['Contact','email_address','name']
    df1['email_address'] = df1['email_address'].str.replace(r"Email","")
    df1['unique_email'] = df1['email_address'].nunique()
    df1['unique_name'] = df1['name'].nunique()
    #save each dataframe to csv
    df1.to_csv(path+"/"+j+".csv")
#create empty list for all csvs     
dfs = []
#iterate through alarm group csvs, create one dataframe for contacts of all alarm groups
for k in group_name:
    df2 = pd.read_csv(path+"/"+k+".csv", index_col=None, header=0)
    df2['station'] = k
    dfs.append(df2)
#concat the dataframes together in dataframe, "Frame"    
frame = pd.concat(dfs)
frame = frame.reset_index(drop = True)
#Count the number of unique email addresses and names
frame['unique_email'] = frame['email_address'].nunique()
frame['unique_name'] = frame['name'].nunique()
#save this dataframe to Summary.csv
frame.to_csv(path+"/"+"Summary"+date+".csv")

