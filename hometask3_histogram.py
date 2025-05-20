# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("cleaned_products.csv", encoding="utf-8")

# Названия столбцов
print("Названия столбцов: ", df.columns)

# Средняя цена
mean_price = df["Цены на диваны"].mean()
print(f"Средняя цена на диваны — {mean_price}")

# Построение гистограммы
plt.hist(df["Цены на диваны"], bins=15, edgecolor = "black", color = "purple")

# Кастомизация гистограммы
plt.xlabel("Цена")
plt.ylabel("Частота")
plt.title("Гистограмма цен на диваны")

plt.grid(True)

# Показать гистограмму
plt.show()