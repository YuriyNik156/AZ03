# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.
# import numpy as np
# random_array = np.random.rand(5)  # массив из 5 случайных чисел
# print(random_array)

import matplotlib.pyplot as plt
import numpy as np

# Создание двух наборов случайных данных
random_array_x = np.random.rand(50) # Массив из 5 случайных чисел по оси x
random_array_y = np.random.rand(50) # Массив из 5 случайных чисел по оси y

# Создание диаграммы
plt.scatter(random_array_x, random_array_y)

# Кастомизация графика
plt.xlabel("Ось x")
plt.ylabel("Ось y")
plt.title("Диаграмма рассеяния для двух наборов случайных данных")

# Вывод диаграммы
plt.show()
