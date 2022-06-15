import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
# obtenir l'url de la page  :création variable url_page qui va récupérer (ligne7)l' et l'afficher(ligne8)
url_page = driver.current_url
print(url_page)
# obtenir le title :
titre_page = driver.title
print(titre_page)
# obtenir le code source de la page
source_page = driver.page_source
print(source_page)

time.sleep(3)
driver.close()
