
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#Entrer dans le 1er frame
driver.switch_to.frame("packageListFrame")
time.sleep(3)

#cliquer sur le lien
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(3)
#sortir du 1er frame et retourner à la page principale
driver.switch_to.default_content()
#Entrer dans le 2éme frame
driver.switch_to.frame("packageFrame")
time.sleep(3)
#cliquer sur le lien
driver.find_element(By.XPATH,"/html/body/main/div/section[1]/ul/li[14]/a/span").click()
time.sleep(3)
#sortir du 2éme frame et retourner à la page principale
driver.switch_to.default_content()
#Entrer dans le 3éme frame
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
time.sleep(3)
driver.quit()