from dataclasses import dataclass
import datetime

# dataclasses - что-то похожее на namedTuple из прошлого примера, но 
# первое - регулярные классы Python
# второе - представляет собой компактные данные, как кортежи
@dataclass
class StockPrice2:
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'AAPL']

price2 = StockPrice2('MSFT', datetime.date(2018, 12, 14), 106.03)

assert price2.symbol == 'MSFT'
assert price2.closing_price == 106.03
assert price2.is_high_tech()

# И главное различие, что мы можем модифицировать значения экземпляра класса
price2.closing_price /= 2
assert price2.closing_price == 53.015
