from typing import List, Dict
from collections import Counter
import math
import matplotlib.pyplot as plt
import random

def bucketize(point: float, bucket_size: float) -> float:
    """Округлить точку до следующего наименьшего кратного размера интервала bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points: List[float], bucket_size: float) -> Dict[float, int]:
    """Разбивает точки на интервалы и подсчитывает их количество в каждом интервале"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points: List[float], bucket_size: float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(list(histogram.keys()), list(histogram.values()), width=bucket_size)
    plt.title(title)
    plt.show()

# Нормальное распределение
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# Обратная ИФР нормального распределения
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    # Используем двоичный поиск
    if mu !=0 or sigma != 1:
        return mu + sigma*inverse_normal_cdf(p, tolerance=tolerance)
    
    hi_z, low_z = 10, -10

    while hi_z - low_z > tolerance:
        mid_z = (hi_z + low_z) / 2
        mid_p = normal_cdf(mid_z)

        if mid_p < p:
            low_z = mid_z
        elif mid_p > p:
            hi_z = mid_z
        else:
            break
    
    return mid_z

# Рассмотрим пример
random.seed(0)

# Рассмотрим два набора данных с одним и тем же среднеквадратичным отклонением и средним
# но гистограммы показывают насколько они разные
# Равномерное распределение между -100 и 100
uniform = [200 * random.random() - 100 for _ in range(10000)]

# Нормальное со средним 0 и стандартным отклонением 57
normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]

plot_histogram(uniform, 10, "Равномерная гистрограмма")
plot_histogram(normal, 10, "Нормальная гистограмма")
