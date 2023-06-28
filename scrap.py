"""
Film Availability Checker

This program allows you to search for the availability of movies on streaming platforms. 
You can add or remove movie names from a file and the program will search for their availability.

Requirements:
- Selenium: Python library for browser automation
- BeautifulSoup: Python library for web scraping

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def search_google(query):
    """
    Searches for a query on Google and returns the HTML content of the search results page.

    Parameters:
    - query (str): The search query to be used on Google.

    Returns:
    - html (str): The HTML content of the search results page.
    """
    # Configure Chrome options and set up the driver
    chrome_options = Options()
    s = Service('C:/Program Files (x86)/chromedriver')
    driver = webdriver.Chrome(service=s, options=chrome_options)

    # Perform the search on Google
    driver.get("https://www.google.com/search?q=" + query)

    # Handle any required interactions (e.g., accepting cookies) adding a try in case there is no cookie
    driver.implicitly_wait(10)
    try:
        bouton_cookies = driver.find_element(By.ID, "L2AGLb")
        bouton_cookies.click()
    except:
        pass

    # Expand content if necessary 
    # adding a try, if the page dont get the button or the movie title don't return a movie
    driver.implicitly_wait(10)
    try:
        button_xpath = '//g-expandable-content[@role="button" and @tabindex="0" and @jscontroller="Ah7cLd"]'
        button = driver.find_element(By.XPATH, button_xpath)
        button.click()
    except:
        pass

    # Wait for the page to load and retrieve the HTML content
    time.sleep(2)
    html = driver.page_source
    driver.quit()

    return html

def extract_div_elements(html, class_names):
    """
    Extracts div elements from HTML based on the provided class names.

    Parameters:
    - html (str): The HTML content to extract elements from.
    - class_names (list): A list of class names to filter the div elements.

    Returns:
    - results (dict): A dictionary of extracted div elements with titles as keys and descriptions as values.
    """
    soup = BeautifulSoup(html, "html.parser")
    div_elements = soup.find_all("div", class_=class_names)

    results = {}
    for i in range(0, len(div_elements), 2):
        title = div_elements[i].text
        description = div_elements[i+1].text
        results[title] = description

    return results

def filter_results(results):
    """
    Filters the results dictionary to include only desired platform and subscription type.

    Parameters:
    - results (dict): The dictionary of movie results to filter.

    Returns:
    - filtered_results (dict): The filtered dictionary of movie results.
    """
    filtered_results = {}
    desired_keys = ["Amazon Prime Video", "Netflix", "Disney+"]
    desired_service = ["Abonnement", "Abonnement premium"]

    for key, value in results.items():
        if key in desired_keys and value in desired_service:
            filtered_results[key] = value

    return filtered_results

def read_movie_names(file_path):
    """
    Reads movie names from a file.

    Parameters:
    - file_path (str): The path to the file containing movie names.

    Returns:
    - movie_names (list): A list of movie names read from the file.
    """
    with open(file_path, 'r') as file:
        movie_names = [line.strip() for line in file]
    return movie_names

def add_movie_names(file_path):
    """
    Adds movie names to a file.

    Parameters:
    - file_path (str): The path to the file to add movie names.

    """
    while True:
        movie_name = input("Entrez le nom du film à ajouter (ou 'q' pour quitter) : ")
        if movie_name == 'q':
            break
        with open(file_path, 'a') as file:
            file.write(movie_name + '\n')

def remove_movie_names(file_path):
    """
    Removes movie names from a file.

    Parameters:
    - file_path (str): The path to the file to remove movie names from.

    """
    movie_names = read_movie_names(file_path)

    print("Liste des films disponibles :")
    for i, movie_name in enumerate(movie_names, start=1):
        print(f"{i}. {movie_name}")

    while True:
        try:
            index = int(input("Entrez le numéro du film à supprimer (ou '0' pour quitter) : "))
            if index == 0:
                break
            if index < 1 or index > len(movie_names):
                print("Numéro invalide. Veuillez réessayer.")
            else:
                del movie_names[index - 1]
                with open(file_path, 'w') as file:
                    file.write('\n'.join(movie_names))
                print("Film supprimé avec succès.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")

def check_movie_availability(movie_name):
    """
    Checks the availability of a movie on streaming platforms.

    Parameters:
    - movie_name (str): The name of the movie to check availability for.

    """
    search_results = search_google(movie_name)
    results = extract_div_elements(search_results, ["ellip bclEt", "ellip rsj3fb"])

    if not results:
        print(f"Désolé, {movie_name} est incorrect. Veuillez réessayer.")
    else:
        filtered_results = filter_results(results)

        if not filtered_results:
            print(f"Désolé, pour {movie_name} il va falloir attendre.")
        else:
            for key, value in filtered_results.items():
                print(f"{movie_name} est disponible sur la plateforme {key} avec l'abonnement.")

def run_movie_search(movie_file):
    """
    Runs the movie search for all movie names in the specified file.

    Parameters:
    - movie_file (str): The path to the file containing movie names.

    """
    movie_names = read_movie_names(movie_file)

    for movie_name in movie_names:
        check_movie_availability(movie_name)

def main():
    """
    The main function of the program.
    """
    movie_file = "films.txt"
    add_movie_names(movie_file)
    remove_movie_names(movie_file)
    run_movie_search(movie_file)

if __name__ == "__main__":
    main()
