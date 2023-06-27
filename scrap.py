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

    driver.implicitly_wait(10)
    try :
        bouton_cookies = driver.find_element(By.ID, "L2AGLb")
        bouton_cookies.click()
    except:
        pass
    driver.implicitly_wait(10)
    try:
        button_xpath = '//g-expandable-content[@role="button" and @tabindex="0" and @jscontroller="Ah7cLd"]'
        button = driver.find_element(By.XPATH, button_xpath)
        button.click()
    except:
        pass

    time.sleep(2)
    html = driver.page_source
    driver.quit()  
    
    return html

def extract_div_elements(html, class_names):
    soup = BeautifulSoup(html, "html.parser")
    div_elements = soup.find_all("div", class_=class_names)

    results = {}
    for i in range(0, len(div_elements), 2):
        title = div_elements[i].text
        description = div_elements[i+1].text
        results[title] = description

    return results

def filter_results(results):
    filtered_results = {}
    desired_keys = ["Amazon Prime Video", "Netflix", "Disney+"]

    for key, value in results.items():
        if key in desired_keys and value == "Abonnement":
            filtered_results[key] = value

    return filtered_results

query = input("Entrez votre recherche : ")
search_results = search_google(query)
results = extract_div_elements(search_results, ["ellip bclEt", "ellip rsj3fb"])
filtered_results = filter_results(results)


if not filtered_results:
    print("Désolé, il va falloir attendre.")
else:
    for key, value in filtered_results.items():
        print(f"Ce film est disponible sur la plateforme {key} avec l'abonnement.")