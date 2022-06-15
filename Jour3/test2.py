# Test case
# 1 lancer le navigateur
# # 2 accéder à l'adresse https://demo.nopcommerce.com/
# # 3 cliquer sur le lien register
# # 4 remplir le formulaire
# # 5 cliquer sur le bouton Register
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.CLASS_NAME,"ico-login").click()
driver.find_element(By.CLASS_NAME,"email").send_keys("arwa@gmail.com")
driver.find_element(By.ID, "Password").send_keys("123456")
driver.find_element(By.XPATH,"(//button[@type='submit'])[2]").click()

time.sleep(4)
driver.close()


