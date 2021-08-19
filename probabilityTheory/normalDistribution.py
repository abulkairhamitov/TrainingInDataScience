import math
import random
from typing import Counter
from matplotlib import pyplot as plt
# Дифференциальная функция распределения (ДФР)
# или плотность вероятности
# нормального распределения
def normal_pdf(x, mu=0, sigma=1):
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2)/(math.sqrt(2 * math.pi)*sigma))

# Некоторые примеры
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x) for x in xs], '-')
plt.plot(xs, [normal_pdf(x, sigma = 2) for x in xs], '--')
plt.plot(xs, [normal_pdf(x, sigma = 0.5) for x in xs], ':')
plt.plot(xs, [normal_pdf(x, mu = -1) for x in xs], '-.')
plt.show()

# Интегральная функция распределения (ИФР)
# или функция распределения
# нормального распределения
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# Некоторые примеры
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x) for x in xs], '-')
plt.plot(xs, [normal_cdf(x, sigma = 2) for x in xs], '--')
plt.plot(xs, [normal_cdf(x, sigma = 0.5) for x in xs], ':')
plt.plot(xs, [normal_cdf(x, mu = -1) for x in xs], '-.')
plt.show()

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

# -----------------
# Центральная предельная теорема
#-----------------

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

# Биномиальное распределение
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

# Гистограмма
def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]

    histogram = Counter(data)
    plt.bar([x for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')
        
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # Линейный график
    xs = range(min(data), max(data) + 1)
    ys = [normal_pdf(i, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.show()
make_hist(0.75, 100, 10000)
# -----------------
# Центральная предельная теорема
#-----------------