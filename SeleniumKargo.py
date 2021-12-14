from selenium import webdriver
import time
browser= webdriver.Chrome()

url ="https://www.imusiparis.com"

browser.get(url) #the site link

#------------------------------Ekran 1---------------------------------------
time.sleep(5)
 
Hizli = browser.find_element_by_xpath("")
Hizli.click()

Yurtici = browser.find_element_by_xpath("")
Yurtici.click()

Aras = browser.find_element_by_xpath("")
Aras.click()

Teslim = browser.find_element_by_xpath("")
Teslim.click()

#-------------------------------Ekran 2---------------------------------------
time.sleep(5)

Ilce = browser.find_element_by_xpath("")
Ilce.click()
#...İlçe seçim işlemi

Gonder = browser.find_element_by_xpath("")
Gonder.click()

#-------------------------------Ekran 3---------------------------------------
time.sleep(5)

kargo_no = browser.find_element_by_name("takip")
kargo_no.send_keys("12345678")
#Uygunsuz kargo no hatası

kargo_no = browser.find_element_by_name("takip")
kargo_no.send_keys("1234567")

sorgu= browser.find_element_by_xpath("")
sorgu.click()

#-------------------------------Ekran 4---------------------------------------
time.sleep(5)

takip= browser.find_element_by_xpath("")
takip.click()

#-------------------------------Ekran 5---------------------------------------
time.sleep(5)

browser.close()