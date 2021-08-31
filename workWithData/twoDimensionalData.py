import matplotlib.pyplot as plt
import random
import math

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

def random_normal():
    """Возвращает случайную выборку из стандартного нормального распределения"""
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [ x + random_normal() / 2 for x in xs]
ys2 = [ -x + random_normal() / 2 for x in xs]

# Если надо было бы выполнить функцию plot_histogram с ys1 и ys2
# то получились бы очень похожие диаграммы
# Но как мы видим они имеют совсем разное совместное распределение
plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')

plt.show()

# Но это разница очевидна, скажем, если посмотреть на корреляцию