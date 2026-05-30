import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('h3')
    print("Список назв книг з першої сторінки:")
    for index, book in enumerate(books, 1):
        title = book.find('a')['title']
        print(f"{index}. {title}")
else:
    print(f"Не вдалося завантажити сторінку помилка: {response.status_code}")