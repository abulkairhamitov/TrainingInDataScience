import random
# Попробуем провести эксперимент с функцией sum_of_squares. Очевидно, что функция минимальна
# при нулевом векторе - притворимся, что не знаем об этом

# Шаг градиента
def step(v, direction, step_size):
    """Двигаться с шаговым размером step_size в направлении от v"""
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]

# Градиент суммы квадратов
def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

# Выбрать произвольную отправную точку
v = [random.randint(-10, 10) for i in range(3)]

tolerance = 0.000000001 # константа точности расчета

# Расстояние между двумя векторами
def distance(v, w):
    return (sum([(v_i - w_i) ** 2 for v_i, w_i in zip(v, w)])) ** 1/2

while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v

# Получим вектор v близкий к нулевому и чем меньше tolerance, тем ближе он будет к [0, 0, 0]
