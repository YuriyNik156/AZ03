# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу с диванами
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(5)

price_text = driver.find_elements(By.CLASS_NAME, "ui-LD-ZU")

# Создание и открытие CSV-файла для записи
with open("products.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Цены на диваны"])  # Указываем заголовок столбца

    # Запись данных в файл
    for price in price_text:
        writer.writerow([price.text])

print("Данные успешно сохранены в файл products.csv")

# Закрытие браузера
driver.quit()
