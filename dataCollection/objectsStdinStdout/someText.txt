from functools import reduce

# Векторы можно реализовывать как списки, но с последующей реализацией арифмитических операций

# Сумма векторов
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

# Разность векторов
def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

# # Сумма нескольких векторов
# def vector_sum(vectors):
#     result = vectors[0]
#     for vector in vectors[1:]:
#         result = vector_add(result, vector)
#     return result

# Сумма нескольких векторов
def vector_sum(vectors):
    return reduce(vector_add, vectors)

# Умножение на скаляр
def scalar_multiply(c, v):
    return [v_i * c for v_i in v]

# Среднее векторов
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

# Скалярное произведение
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# Сумма квадратов вектора
def sum_of_squares(v):
    return dot(v, v)

# Длина вектора
def magnitude(v):
    sum_of_squares(v, v) ** 1/2

# Расстояние между двумя векторами
def distance(v, w):
    return magnitude(vector_substract(v, w))
