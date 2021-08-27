# Библиотека импортируемая ниже строит дерево их раснообразных элементов
# , расположенных на странице, и для доступа к ним предоставляет простой интерфейс
from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.google.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p') # Найдет первый тег

first_paragraph_texts = soup.p.text         # Текст первого параграфа
first_paragraph_words = soup.p.text.split() # Слова первого параграфа

# Вызове keyError, если id отсутствует
# first_paragraph_id = soup.p['id']

# Возвращает None, если id отсутствует
# first_paragraph_id2 = soup.p.get('id')

all_paragraphs = soup.find_all('p') # Или просто soup('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p') if 'important' in p.get('class', [])]

# Предположим нам нужно найти каждый span, содержащийся внутри <div>
spans_inside_divs = [span for div in soup('div') for span in div('span')]

