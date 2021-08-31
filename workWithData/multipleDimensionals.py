import matplotlib.pyplot as plt
from typing import List, Callable
from supporting_correlation.correlation import correlation
import random

Vector = List[float]
Matrix = List[List[float]]

# Создание матрицы (entry_fn возвращает требуемое значение элемента с индексами i и j)
def make_matrix(num_rows: int, 
                num_cols: int, 
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def correlation_matrix(data: List[Vector]) -> Matrix:
    """Возвращает матрицу размера len(data) * len(data) 
        , (i, j)-й элемент которой является корреляцией между data[i] и data[j]
    """
    def correlation_ij(i: int, j: int) -> float:
        return correlation(data[i], data[j])

    return make_matrix(len(data), len(data), correlation_ij)

# Визуальный подход, если не так много размерностей, - создать матрицу рассеяний
# Которая показывает все попарные диграммы рассеяния
corr_data = [   [random.randint(0, 100) for _ in range(100)],
                [random.randint(-100, 100) for _ in range(100)],
                [random.randint(0, 300) for _ in range(100)],
                [random.randint(-400, 55) for _ in range(100)]  ]
num_vectors = len(corr_data)
# subplots - позволяет строить подграфики. На вход передается число строк и столбцов
# а на выходе возвращается обьъект figure (который мы не используем) и axes - двумерный массив объектов
# на которых мы и будем строить графики
fig, ax = plt.subplots(num_vectors, num_vectors)
for i in range(num_vectors):
    for j in range(num_vectors):
        if i != j:
            ax[i][j].scatter(corr_data[j], corr_data[i])
        else:
            ax[i][j].annotate("Серия " + str(i), (0.5, 0.5), xycoords='axes fraction', ha="center", va="center")
        
        # Спрятать освевые метки, за исключением левой и нижней диаграмм
        if i < num_vectors - 1:
            ax[i][j].xaxis.set_visible(False)
        if j > 0:
            ax[i][j].yaxis.set_visible(False)

ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_ylim(ax[0][1].get_ylim())
plt.show()
