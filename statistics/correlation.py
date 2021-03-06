from collections import Counter
# Нужно понимать, что корреляция устанавливает определенный тип зависимости: зная о соотношении
# переменной со средним, можно получить информацию о таком же соотношении второй переменной. Поэтому для
# очевидно зависимых переменных корреляция может выдывать нулевую корреляцию. 

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

# вектор отклонений от среднего
def de_mean(x):
    x_bar = sum(x) / len(x)
    return [x_i - x_bar for x_i in x]

# Скалярное произведение
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# Ковариация - совместное отклонение двух переменных от своих средних (дисперсия для двух выборок)
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
# В случае, если элементы векторов x и y оба одновременно выше или ниже своих средних, в сумму входит положительное число
# Это значит, что если ковариация достаточно не близка к нулю, то можно говорить о взаимосвязи x и y, что бы это не значило

# Корреляция лучший аналог ковариации в том смысле, что она безразмерна и лежит на отрезке от -1 до 1
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_y / stdev_x
    else :
        return 0

