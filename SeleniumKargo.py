from selenium import webdriver
import time
import unittest

browser= webdriver.Chrome()
url ="http://localhost:8080/"
browser.get(url) #the site link

#------------------------------Ekran 1--------------------------------------------
time.sleep(2)

#eposta hatasi 1
Onayla = browser.find_element_by_id("onayla") 
Onayla.click()
 
time.sleep(5)

Yer = browser.find_element_by_id("yer")
Yer.click()

#-------------------------------Ekran 2-------------------------------------------
time.sleep(3)

Ilce = browser.find_element_by_id("ilce")
Ilce.send_keys("Fatih")
time.sleep(2)

#Ekran 1'e donus
Gonder = browser.find_element_by_id("tamam")
Gonder.click()

time.sleep(2)
#eposta hatasi 2
eposta = browser.find_element_by_id("mail")
eposta.send_keys("aburmail.com")

Onayla = browser.find_element_by_id("onayla")
Onayla.click()
 

time.sleep(2) 
Hizli = browser.find_element_by_id("jetizz") 
Hizli.click()


time.sleep(2) 
Yurtici = browser.find_element_by_id("yurtici")
Yurtici.click()


time.sleep(2) 
Aras = browser.find_element_by_id("aras")
Aras.click()


eposta = browser.find_element_by_id("mail")
eposta.send_keys("akhaciog@gmail.com")

##Assertion
#time.sleep(3)
#Ucretsiz = browser.find_element_by_id("kargoucretsiz")
#assertEqual("Kargonun ucretsiz olabilmesi icin ",Ucretsiz,"ucretsiz kargo icin fiyat tamamlama yok")

time.sleep(2) 
Onayla = browser.find_element_by_id("onayla")
Onayla.click()


#-------------------------------Ekran 3-------------------------------------------
time.sleep(3)

#alani doldur hatasi
sorgu= browser.find_element_by_id("sorgula")
sorgu.click()
time.sleep(1)

#ikisinden biri
eposta = browser.find_element_by_id("kargo_no")
eposta.send_keys("7525734")

# eposta = browser.find_element_by_id("kargo_no")
# eposta.send_keys("4863946")

time.sleep(2)
# time.sleep(12)

sorgu= browser.find_element_by_id("sorgula")
sorgu.click()





#-------------------------------Ekran 4-------------------------------------------

#
#
#


# Varis = browser.find_element_by_id("sure_str")
# #Assertion
# assertEqual("Tahmini Varis Suresi: ",Varis,"Tahmini varis suresi hatali")

#
# 
# 

time.sleep(4)

durum= browser.find_element_by_id("hareket")
durum.click()


# -------------------------------Ekran 5-----------------------------------------
time.sleep(3)

#
#
#
#

browser.back()
time.sleep(2)
browser.back()
time.sleep(3)

sorgu= browser.find_element_by_id("iade")
sorgu.click()
# -------------------------------Ekran 6-----------------------------------------

time.sleep(2)

urun1= browser.find_element_by_id("dell")
urun1.click()

#Bos neden hatasi
talep= browser.find_element_by_id("talep")
talep.click()

time.sleep(2)

#200 karakteri gecmeye calisma
neden = browser.find_element_by_id("neden")
neden.send_keys("uc yuzuk gogun altinda yasayan elf krallarina, yedisi tastan saraylarinda cuce hukumdarla dokuzu olumlu insanlara ,olecekler ne yazik, bir yuzuk golgeler icindeki mordor diyarinda. Kara tahtinda oturan karanliklar efendisine hepsine hukmedecek bir yuzuk, hepsini o bulacak hepsini bir araya getirip karanlikta birbirine baglayacak golgeler icindeki mordor diyarinda")
time.sleep(5)
neden.clear()

neden = browser.find_element_by_id("neden")
neden.send_keys("defolu olarak geldi urun")
time.sleep(3)

talep= browser.find_element_by_id("talep")
talep.click()

# time.sleep(2)
# #Assertion
# suredoldu = browser.find_element_by_id("sureasim")
# assertEqual("Secmis oldugunuz urunun 14 gunluk cayma hakki suresi doldugu icin iade talebi acilmamaktadir !!!",suredoldu,"iade talebi hatasi")

# suredoldu = browser.find_element_by_id("sure")
# assertEqual("Urun iade talebiniz olusturulmustur.",suredoldu,"iade talebi hatasi")

time.sleep(2)

browser.close()


