import math

# ИФР и ДФР нормального распрделения
def normal_pdf(x, mu=0, sigma=1):
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2)/(math.sqrt(2 * math.pi)*sigma))

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# Обратная к ИФР
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

# Рассмотрим пример бросании монеты
# Выдвинем нулевую гипотезу H0, что монета уравновешена, т.е. p = 0.5.
# Сопоставим альтернативную H1, т.е. p != 0.5

# Проверять нулевую гипотезу будем подсчетом количества орлов в n бросках, т.е.
# получим биномиальную случайную величину, которую можно выразить при помощи нормального распределения

# Аппроксимация биномиальной случайной величины нормальным распределением
def normal_approximation_to_binomial(n, p):
    mu = p*n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# Вероятность, что значение нормальной случайной величины лежит
# ниже норогового значение
normal_probability_below = normal_cdf

# Оно выше порогового значения, если оно не ниже порового значения
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# Лежит между
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# Лежит за пределами
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

# Проделаем тоже самое, но границы не вероятности, а значения

def normal_upper_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    tail_probability = (1 - probability) / 2

    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

# Пусть решено сделать 1000 бросков, тогда случайная велечина должна
# быть распределена приближенно со средним значением (500)
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# Следующий этап - принять решение об уровне значимости, т.е. насколько мы
# готовы в результате проверки совершить ошибку первого рода ("ложноположительность")
# Возьмем 5%
normal_two_sided_bounds(0.95, mu_0, sigma_0) # (469, 531)

# Полезно знать мощность проверки, т.е. вероятность не сделать ошибку второго рода
# Проверим, что случится, если на самом деле p = 0.55 - альтернативная H1 гипотеза
# Вычислим мощность проверки следующим образом:
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# Фактический mu и sigma при p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# Мы вычисляем вероятность
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability # мощность = 0.887, что мне вообще говоря удивило

# Теперь возьмем H0 <= 0.5

# Верхняя граница нормальной случайной величины
hi = normal_upper_bound(0.95, mu_0, sigma_0)

# Вероятность ошибки второго рода
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability # 0.936

# Вместого того, чтобы отвергать нулевую гипотезу, когда X ниже 469, что вряд ли произойдет
# если альтернативная гипотеза верна
# Отвергаем нулевую гипотезу, когда Х лежит между 526 и 531, что вполне может произойти, когда H1 правильная


