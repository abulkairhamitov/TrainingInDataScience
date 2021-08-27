# Многие веб-сайты предоставляют интерфейсы программирования приложений
# которые позволяют явным образом запрашивать данные в структурированном формате

import json
serialized = """{ "title" : "Data Science Book", 
"author" : "Joel Grus", 
"publicationYear" : 2019, 
"topics" : [ "data", "science", "data science"] } """ 

# Разобрать JSON, создав Руthоn'овский словарь 
deserialized = json.loads(serialized) 

assert deserialized["publicationYear"] == 2019 
assert "data science" in deserialized["topics"] 

# Иногда поставщик API вас ненавидит и предоставляет ответы только в формате
# XML
# <Book> 
# <Title>Data Science Book</Title> 
# <Author>Joel Grus</Author> 
# <PublicationYear>2014</PublicationYear> 
# <Topics> 
# <Topic>data</Topic> 
# <Topic>science</Topic> 
# <Topic>data science</Topic> 
# </Topics> 
# </Book> 

# Но для получения данных из XML можно воспользоваться BeautifulSoup аналогиноч тому
# как она применялась для получения из HTML