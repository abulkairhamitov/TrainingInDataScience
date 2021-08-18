# Здесь стоит вопрос описательного анализа
from collections import Counter

# --------------------
# Показатели центра распределения
# --------------------

# Полезно знать среднее значение данных, но он чувствителен к выбросам


def mean(x):
    return sum(x) / len(x)

# не так как медиана
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        return (sorted_v[midpoint - 1] + sorted_v[midpoint]) / 2

# Обобщением медианы - квантиль (значение, меньше которого расположен определенный процент данных)
def quantile(p, x):
    n = len(x)
    p_index = int(n * p)

    return sorted(x)[p_index]

# Реже применяется мода - значение или значения, которые встречаются наиболее часто
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]

# --------------------
# Показатели центра распределения
# --------------------

# --------------------
# Показатели вариации отражают меру изменчивости данных
# --------------------

# Самый простой показатель - размах
def data_range(x):
    return max(x) - min(x)

# Знаменитая дисперсия, но с n-1 в знаменателе (в среднем это оправдано)
def variance(x):
    x_bar = mean(x)
    return sum([(x_i - x_bar) ** 2 for x_i in x]) / (len(x) - 1)

# Для простоты работы с единицами измерения используется стандартное отклонение
def standard_deviation(x):
    return variance(x) ** 2

# Но все это также чувствительно к выбросам
# Размах можно заменить на интерквартильный размах
def interquantile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

# --------------------
# Показатели вариации
# --------------------

