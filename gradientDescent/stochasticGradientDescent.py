import random
# Стохастический градиент применяют для функции вида
# Q(t) = 1/n*sum_i(Q_i(t))
# Дело в том, что функция ошибок имеет свойство аддитивности, т.е.
# прогнозная ошибка на всем наборе данных является суммой прогнозных ошибок для каждой точки
# данных


# Перемешать индексы набора
def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]

# Разность векторов
def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

# Умножение на скаляр
def scalar_multiply(c, v):
    return [v_i * c for v_i in v]

# Стохастическая минимизация
# В качестве примера для понимания можно взять прямую y = t_1 + t_2*x
# У нас есть тренировочный набор (x_i, y_i) и мы хотим аппроксимировать их нашей прямой
# Целевой функцией (функцией потерь) будет использоваться метод наименьших квадратов
# Получим Q(t) = sum_i(t_1 + t_2 * x_i - y_i)
# И смысл стохастического градиента в том, что на каждом шаге выбирается одна часть данных, причем случайно
def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = zip(x, y) # Наш тренировочный набор: с множеством наблюдений и ответов
    theta = theta_0 # Первоначальная гипотеза
    alpha = alpha_0 # Первоначальный размер шага
    min_theta, min_value = None, float(" inf")
    iterations_with_no_improvement = 0

    # остановиться, если достигли 100 итераций без улучшений
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

        if value < min_value:
            # Запоминаем новый минимум
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # Если улучшений нет, то сжимаем шаг
            alpha *= 0.9
            iterations_with_no_improvement += 1

            # И сам шаг градиента
            for x_i, y_i in in_random_order(data):
                gradient_i = gradient_fn(x_i, y_i, theta)
                theta = vector_substract(theta, scalar_multiply(alpha, gradient_i))
        
    return min_theta

# Отрицание результата на выходе
def negate(f):
    return lambda *args, **kwargs: -f(*args, **kwargs)

# Отрицание списка результатов на выходе (Для градиента)
def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

# стохастическая максимизация
def maximize_shochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(negate(target_fn), negate_all(gradient_fn), x, y, theta_0, alpha_0)
