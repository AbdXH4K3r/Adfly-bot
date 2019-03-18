from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random,time,re,names,time

def Prox():
	link = input("Adfly Link : ")
        driver = webdriver.Firefox()
	driver.get(link)
	time.sleep(5)
	adnext = driver.find_element_by_id("skip_bu2tton")
	adnext.click()
	time.sleep(2)
	i = i+1
	i = str(i)
	print("Click Number "+i+" ! ")

Prox()
