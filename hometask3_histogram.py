# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Загрузка данных из CSV-файла
file_path = 'cleaned_products.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'price'
prices = data['Цены на диваны']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Мы можем изменить количество bin-ов по своему усмотрению

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()