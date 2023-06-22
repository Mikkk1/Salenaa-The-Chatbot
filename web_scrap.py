import requests
from bs4 import BeautifulSoup


def web_scrap(question):
    search_url = f"https://www.google.com/search?q={question}"
    response = requests.get(search_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    first_result = soup.find("div", class_="BNeawe").get_text()
    return first_result