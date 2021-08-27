# Директор по политике в DataSciencester обеспокоен потенциальным регулированием отрасли науки о данных и просит вас квантифицировать, что говорит Конгресс 
# по этой теме. В частности, он хочет, чтобы вы нашли всех представителей, у которых есть пресс-релизы о "данных". 
# На момент публикации имеется страница со ссылками на все веб-сайты членов 
# Палаты представителей по адресу: https://www.house.gov/representatives.

from bs4 import BeautifulSoup
import requests
import re

url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")

all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]
print(len(all_urls)) # Получилось 967

# Фрагмент кода выше вернет слишком много ссылок
# Чтобы найти нужные воспользуемся регулярным выражением
regex = r"^https?://.*\.house\.gov/?$"

assert re.match(regex, "http://joel.house.gov") 
assert re.match(regex, "https://joel.house.gov") 
assert re.match(regex, "http://joel.house.gov/") 
assert re.match(regex, "https://joel.house.gov/") 
assert not re.match(regex, "joel.house.gov") 
assert not re.match(regex, "http://joel.house.com") 
assert not re.match(regex, "https://joel.house.gov/Ьiography")

good_urls = [url for url in all_urls if re.match(regex, url)]
print(len(good_urls)) # 874

# Это все еще слишком много. Но можно заметить на наличие дубликатов, поэтому
# воспользуемся структурой set
good_urls = list(set(good_urls))

print(len(good_urls)) # 437

