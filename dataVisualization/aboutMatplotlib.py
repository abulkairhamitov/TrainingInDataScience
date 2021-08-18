# Matplotlib - инструмент визуалиазации данных
from matplotlib import pyplot as plt
import collections

# --------------------
# Обыкновенная линейная диаграмма
# --------------------

# # Создадим искусственные данные
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.5, 1075.9, 2862, 5976, 10289, 14900]

# # Передадим pyplot значения на оси абсцисс и ординат
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# plt.title("ВВП")
# plt.ylabel("Млрд долларов")
# plt.show()
# --------------------
# Обыкновенная линейная диаграмма
# --------------------

# --------------------
# Столбчатые диаграммы
# --------------------

# students = ["Adam", "Abu", "Ahmad", "Smith", "Sasha"]
# numberOfFives = [4, 15, 6, 2, 19]

# # Координаты расположение столбцов
# xs = [i for i, _ in enumerate(students)]

# # Передача координат столбцам
# plt.bar(xs, numberOfFives)

# plt.ylabel("Количество пятерок")
# plt.title("Успеваемость")

# # Метки на оси абсцисс
# plt.xticks([i for i, _ in enumerate(students)], students)

# plt.show()

# --------------------
# Столбчатые диаграммы
# --------------------

# --------------------
# Гистограммы
# --------------------

# grades = [80, 90, 94, 84, 70, 0, 85, 94, 120, 34, 66, 99, 0]
# decile = lambda grade: grade // 10 * 10
# histogram = collections.Counter(decile(grade) for grade in grades)

# # 3-й аргумент отвечает за ширину столбцов
# plt.bar([x for x in histogram.keys()], histogram.values(), 6)

# # Указывает длину оси Х и У
# plt.axis([-5, 130, 0, 5])

# plt.xticks([10 * i for i in range(14)])
# plt.show()

# --------------------
# Гистограммы
# --------------------

# --------------------
# Точечные диаграммы
# --------------------

friends = [80, 65, 93, 23, 75, 63, 56, 76, 56]
minutes = [185, 150, 205, 120, 220, 130, 105, 145, 202]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# Добавим метки labels для каждой точки
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, 
    xy = (friend_count, minute_count), # Указываем координаты для метки
    xytext=(5, -5), # Смещаем
    textcoords= 'offset points')

plt.show()

# --------------------
# Точечные диаграммы
# --------------------