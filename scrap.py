
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def search_google(query):
    chrome_options = Options()
    s = Service('C:/Program Files (x86)/chromedriver')
    driver = webdriver.Chrome(service = s,options=chrome_options)
    driver.get("https://www.google.com/search?q=" + query)

    # Utilisez Selenium pour simuler l'appui sur la touche "Enter" afin d'effectuer la recherche
    #search_box = driver.find_element(By.NAME,"q")
    #search_box.send_keys(Keys.RETURN)
    
    driver.implicitly_wait(10)
    bouton_cookies = driver.find_element(By.ID, "L2AGLb")
    bouton_cookies.click()

    driver.implicitly_wait(10)
    button_xpath = '//g-expandable-content[@role="button" and @tabindex="0" and @jscontroller="Ah7cLd"]'
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()
    
  
    
    # Récupérez le contenu HTML après que les contenus cachés soient disponibles
    time.sleep(2)
    html = driver.page_source
    
    driver.quit()  # Fermez le navigateur
    
    return html


def extract_div_elements(html, class_names):
    soup = BeautifulSoup(html, "html.parser")
    div_elements = soup.find_all("div", class_=class_names)
    
    for div in div_elements:
        print(div.text)


# Demande à l'utilisateur de saisir le terme de recherche
query = input("Entrez votre recherche : ")

# Envoie la requête de recherche et récupère les résultats
search_results = search_google(query)

# Extrait les éléments <div> ayant la classe "ellip bclEt"
extract_div_elements(search_results, ["ellip bclEt", "ellip rsj3fb"])