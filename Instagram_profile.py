#!/usr/bin/env python
# coding: utf-8

# In[32]:


#1) Módulos de importe/librerias
import os
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import warnings
warnings.filterwarnings('ignore')

#Configuración del webdriver
os.environ["PATH"] += os.pathsep + r'C:\SeleniumDrivers';
driver= webdriver.Chrome();
driver.get('https://www.instagram.com/')
page_detailed = driver.page_source


#login
time.sleep(5)
username = driver.find_element_by_css_selector("input[name='username']")
password = driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("#user")
password.send_keys("#Password")
time.sleep(5)
login = driver.find_element_by_css_selector("button[type='submit']").click()

#save your login info?
time.sleep(10)
notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(10)
notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()


# In[33]:


profile_insta=[]
post_insta=[]
followers_insta=[]
following_insta=[]
name_insta=[]


profile=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/div[1]/h2')
profile_insta.append(profile.text)
post= driver.find_element_by_class_name('g47SY')
post_insta.append(post.text)


# In[34]:


print(profile_insta)
print(post_insta)
print(followers_insta)


# In[ ]:





# In[ ]:





# In[ ]:



  


# In[ ]:





# In[ ]:




