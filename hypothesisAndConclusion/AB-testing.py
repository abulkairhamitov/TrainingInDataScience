import math
import statisticalHypothesisTesting as st

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * st.normal_probability_above(x, mu, sigma)
    else:
        return 2 * st.normal_probability_below(x, mu, sigma)

# Возьмем пример с выбором рекламой
# Пусть N_A людей видят рекламу А и n_A из них нажимают на нее
# Каждый просмотр рекламы можно представить в виде испытания Бернулли
# Тогда n_A/N_A - приближенно нормальная случайная величина с математическим
# ожиданием p_A и стандартным отклонением sqrt(p_A(1-p_A)/N_A)
# Почему стандартное отклонение выглядит именно так?
# Наша случайная величина состоит из суммы N_A испытаний бернулли, дисперсия которых равна p(1-p)
# Тогда дисперсия = D( (D(x_1) + D(x_2) + D(x_3) + ... +D(x_n))/N_A ) = p(1-p)*N_A/N_A^2 = p(1-p)/N_A

# Аналогино для рекламы B
def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

# Статистика a/b - тестирования
def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistic(1000, 200, 1000, 180)
two_sided_p_value(z) # 0.254 Вероятность наблюдать такую большую разницу

z = a_b_test_statistic(1000, 200, 1000, 150)
two_sided_p_value(z) # 0.003 в этом случае намного меньше






