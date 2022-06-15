
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")
drop_Country = driver.find_element(By.ID,"input-country")
country = Select(drop_Country)
#Selection par texte visible(dynamiq)
# country.select_by_visible_text("Tunisia")
#selection par index(statiq), 1 c le 1er rang
#country.select_by_index(1)
#Selection par valeur(au  niveau de select)
country.select_by_value("167")
#Récup de toutes les options ds Select
all_options = country.options
total_options = len(all_options)
print("Le nombre total d'options :", total_options)
# Afficher toutes les options( les pays) ds la console
# for opt in all_options:
#     print(opt.text)
# selectionner le canada ds Country et cliquer dessus
for opt in all_options:
    if opt.text == "Canada":
        opt.click()
        break






