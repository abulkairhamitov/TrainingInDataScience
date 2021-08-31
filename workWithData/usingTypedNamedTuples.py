from typing import Dict
# Для представления данных общепринято использовать словари
import datetime

stock_price = { 'closing_price': 102.06,
                'date': datetime.date(2014, 8, 29),
                'symbol': 'AAPL'}

# Есть нескольки причин, почему это далеко не идеальный вариант
# Во-первых, незначительное соображение, что словарь при больших данных
# будет использовать больше памяти чем нужно
# Во-вторых, крупная проблема заключается в том, что доступ к элементам
# по ключу подвержен ошибкам. Следующий код будет работать без ошибок
# и работать неправильно

# Опечатка!
stock_price['cosing_price'] = 103.06

# Наконец, в отличие от единообразных словарей, которые мы можем аннотировать
# типами
prices: Dict[datetime.date, float] = {}
# Нет полезного способа аннотировать словари как данные, которые имеют множество
# разных типов значений

# Python в качестве альтернативы предлагает класс именованных кортежей
# namedtuple, который похож на кортеж, но с именованными слотами
from collections import namedtuple

StockPrice = namedtuple('StockPrice', ['symbol', 'date', 'closing_price'])
price = StockPrice('MSFT', datetime.date(2018, 12, 14), 106.03)

assert price.symbol == 'MSFT'
assert price.closing_price == 106.03

# Также большой плюс именнованых кортежей от обыкновенных, что к его элементам
# можно обращаться по индексу

# Аннотирование происходит следующим образом
from typing import NamedTuple

class StockPrice(NamedTuple):
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """Это класс, поэтому имы также можем добавлять методы"""
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'AAPL']

price = StockPrice('MSFT', datetime.date(2018, 12, 14), 106.03)

assert price.symbol == 'MSFT'
assert price.closing_price == 106.03
assert price.is_high_tech()