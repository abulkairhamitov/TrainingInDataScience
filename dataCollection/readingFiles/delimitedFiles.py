# # Часто поля содержат запятые, символы табуляции и новой строки
# # По этой причине следует использовать модуль csv (или pandas)

import csv

# # Предположим, что есть файл с курсами акций, где значения разделены символом табуляции
# # 6/20/2014 APPL    90.91
# # 6/20/2014 MSFT    41.67
# # ...
# # По техническим причинами после 'r' или 'w' всегда нужно дописывать b (двоичный режим)
# with open('tab_delimited_stock_prices.txt', 'rb') as f:
#     reader = csv.reader(f, delimiter='\t')
#     for row in reader:
#         date = row[0]
#         symbol = row[1]
#         closing_price = float(row[2])
#         # process(date, symbol, closing_price)

# # Если же файл содержит заголовки
# # date:symbol:closing_price
# # 6/20/2014:APPL:90.91
# # ...

# # То можно пропустить строку заголовков (вызвав вначале метод reader.next()) либо
# # воспользоваться читающим объектом csv.DictReader, чтобы получить строки в виде словаря
# # dict (где ключами являются заголовки)
# with open('colon_delimited_stock_prices.txt', 'rb') as f:
#     reader = csv.DictReader(f, delimiter=':')
#     for row in reader:
#         date = row["date"]
#         symbol = row["symbol"]
#         closing_price = row['closing_price']
#         # process(date, symbol, closing_price)

# Даже если в файле нет заголовков, то в DictReader можно передать ключи

# Запись данных с разделителями в файл выполняется аналогичным образом при помощи
# пишущего объекта csv.writer:
today_prices = {'APPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5 }

with open('comma_delimited_stock_prices.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])