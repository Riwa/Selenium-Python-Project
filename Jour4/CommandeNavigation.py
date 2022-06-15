import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
time.sleep(3)
driver.get("https://www.google.com")
time.sleep(3)
#retourne à la page précedante
driver.back()
time.sleep(3)
#aller à la page suivante
driver.forward()
#Actualiser la page
driver.refresh()
time.sleep(3)

driver.quit()
